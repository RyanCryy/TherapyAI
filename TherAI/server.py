from flask import Flask, render_template, request

##GEMINI IMPORT SETUPS##############################################################################
import pathlib
import textwrap
import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
####################################################################################################

## API KEY SETUPS ###################################################################################
def to_markdown(text):
  text = text.replace('•', '  *')
  return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

# API key is AIzaSyBmBD7-9uzZ29LF7bQeZ7XPrjfSZhIxXzY
# Or use `os.getenv('GOOGLE_API_KEY')` to fetch an environment variable.
GOOGLE_API_KEY= "AIzaSyBmBD7-9uzZ29LF7bQeZ7XPrjfSZhIxXzY"

genai.configure(api_key=GOOGLE_API_KEY)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/login')
def login():  
    #MySQL DB retrieval 
    #checking of the password and username if it matches
    #after login redirect to therapy. 
    return render_template("login.html" )

@app.route('/signup')
def signup():  
    #adds username and password to the MySQL DB 
    #After Signup, redirect to Login
    #add disclaimer checbox 
    return render_template("signup.html" )

@app.route('/about') ##last part
def about():  
    return render_template("about.html" )


@app.route('/therapy') 
def therapy():  
    return render_template("therapy.html" )


app.run(debug=True,port=5000)