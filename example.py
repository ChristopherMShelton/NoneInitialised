from sqlalchemy import create_engine

from flask import Flask, request, jsonify
app = Flask(__name__)

import uuid

from sqlalchemy.orm import sessionmaker

from person import Person

import json

@app.route("/")
def hello():
    return_value = ''
    result = execute_sql("select * from noodles")
    for row in result:
        return_value += row['stuff']
        return_value += '\n'
    return return_value
  
@app.route("/test/<stuff>")
def test(stuff):
    result = execute_sql(f"insert into noodles values('{uuid.uuid4()}','{stuff}')")
    return "Inserted."
  
@app.route("/testtwo/<id>/<stuff>")
def testtwo(id, stuff):
    result = execute_sql(f"update noodles set stuff = '{stuff}' where id = '{id}'")
    return "Updated."
  
@app.route("/testthree/<id>")
def testthree(id):
    result = execute_sql(f"delete from noodles where id = '{id}'")
    return "Deleted."
  
@app.route("/testfour", methods=['POST'])
def testfour():
    firstname = request.form['firstname']
    surname = request.form['surname']
    birthday = request.form['birthday']
    result = execute_sql(f"insert into noodles (id, firstname, surname, birthday) values('{uuid.uuid4()}','{firstname}','{surname}','{birthday}')")
    return "Done."
  
@app.route("/testfive", methods=['POST','GET'])
def testfive():
  database_uri='postgres://postgres:secret@localhost:5432'
  engine = create_engine(database_uri)
  Session = sessionmaker(bind=engine)
  fred = Person(firstname='fred',surname='bloggs',birthday='18th August',id=uuid.uuid4())
  session = Session()
  session.add(fred)
  session.commit()
  return 'done it fam'
  
@app.route("/person/<id>")
def get_person(id):
  database_uri='postgres://postgres:secret@localhost:5432'
  engine = create_engine(database_uri)
  Session = sessionmaker(bind=engine)
  session = Session()
  the_person = session.query(Person).filter_by(id=id).first()
  session.commit()
  return json.dumps(the_person.to_dict())
  #return jsonify(the_person)
  
def execute_sql(sql_string=None, database_uri='postgres://postgres:secret@localhost:5432'):
    engine = create_engine(database_uri)
    connection = engine.connect()
    trans = connection.begin()
    sql = sql_string
    response = connection.execute(sql)
    trans.commit()
    return response