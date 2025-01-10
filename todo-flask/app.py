from flask import Flask, request  #import Flask from flask
from models import Schema
from services import ToDoService



app = Flask(__name__) # creating an app instance 

"""
These are some basic operations on flask which are required before creating a todo app
""" 

@app.route('/') #at the end poin '/' call method hello which returns "Hello world!"
def hello():
    return "Hello, World!"

@app.route("/name/<name>") 
def hello_name(name):
    return 'Hello, ' + name


@app.route('/todo', methods=["POST","GET"])
def create_todo():
    service = ToDoService()  # Create an instance of ToDoService
    todo_id = service.create(request.get_json())  # Call the instance method
    return {"id": todo_id}, 201  # Return a valid JSON response with a status code


if __name__ == '__main__':  # on running python app.py , run the flask app
    Schema()
    app.run(debug=True) #debug=True is only added only on the development enviroment which helps the server to restart as we add new code to the app


