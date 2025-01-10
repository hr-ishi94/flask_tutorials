import sqlite3


"""The lines in the ToDoModel are kept this way for the tutorial purposes. In future blogs, we will be switching to an ORMs where you don’t have to write SQL Queries at all. Not using an ORM may result in SQLInjections."""

class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('todo.db') #creating a connection to database
        self.create_user_table()
        self.create_todo_table()

    def create_todo_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Todo"(
        id INTEGER PRIMARY KEY,
        Title TEXT,
        Description TEXT,
        _is_done boolean,
        _is_deleted boolean,
        CreatedOn Date DEFAULT CURRENT_DATE,
        DueDate Date,
        UserId INTEGER FOREIGNKEY REFERENCES User(_id)); 
        """

        self.conn.execute(query)
    
    def create_user_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "User"(
        id INTEGER PRIMARY KEY,
        Name TEXT,
        Email TEXT
        );
        """

        self.conn.execute(query)


class TodoModel:
    TABLENAME = "TODO"

    def __init__(self):
        self.conn = sqlite3.connect('todo.db')

    def create(self, text, description):
        query = f'INSERT INTO {self.TABLENAME} (Title, Description) VALUES (?, ?)'
        result = self.conn.execute(query, (text, description))
        return result.lastrowid