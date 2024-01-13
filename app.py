from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def welcome():
    return 'Welcome to the Flask App!'

@app.route('/hello')
def hello():
    # Get the 'age' parameter from the query string
    age = request.args.get('age', 'Unknown')
    
    # Display a welcome message with the provided age
    return f'Hello! Your age is {age} years.'

if __name__ == '__main__':
    app.run(debug=True)
