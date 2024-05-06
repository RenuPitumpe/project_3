# Import the dependencies.
import numpy as np
import pandas as pd
import datetime as dt

# Python SQL toolkit and Object Relational Mapper
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, text

from flask import Flask, jsonify, request
import json


#################################################
# Database Setup
#################################################

# Create engine using the `hawaii.sqlite` database file
engine = create_engine("sqlite:///data/movies.db")

 # Create connection
connection = engine.connect()

# Execute a SQL query
query = text("SELECT * FROM movies_table")
result = connection.execute(query)

# Fetch and print the results
for row in result:
    print(row)

# Close the connection
connection.close()

# Assign the measurement class to a variable called `Measurement` and
# the station class to a variable called `Station`
# Measurement = Base.classes.measurement
# Station = Base.classes.station

# Create a session
# session = Session(engine)