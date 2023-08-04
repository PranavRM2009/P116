# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Pranav" # write your name
    age = "5" # write your age

    return render_template('index.html' , name = name , age = age)

@app.route("/father")
def father():

    name = "Rakesh" # write your name
    age = "25" # write your age

    return render_template('father.html' , name = name , age = age)

@app.route("/friend")
def friend():

    name = "Prithvi" # write your name
    age = "5" # write your age

    return render_template('friend.html' , name = name , age = age) 
    
@app.route("/mother")
def mother():

    name = "Maby" # write your name
    age = "23" # write your age

    return render_template('mother.html' , name = name , age = age)




# add other routes, if you want




# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
