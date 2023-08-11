# config                    
from flask import Flask
app = Flask(__name__)

# Index route
@app.route('/')
def index():
    return 'Hello, this is PetFax!'

# Pets Index Route
@app.route('/pets')
def pets_index():
    return 'These are our pets available for adoption!'
