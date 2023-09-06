from flask import Flask
from flask import request
from flask import jsonify
from flask_sqlalchemy import SQLAlchemy  # Import SQLAlchemy

app = Flask(__name__)

# Configure SQLAlchemy to use an SQLite database (in-memory for this example)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///employees.db'  # SQLite in-memory database
db = SQLAlchemy(app)  # Create a SQLAlchemy instance

# Define a database model for the Employee entity
class Employee(db.Model):
    employeeId = db.Column(db.String(20), primary_key=True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(100))

# Create the database tables (you need to run this once)
db.create_all()
