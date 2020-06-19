from flask import Flask


app = Flask(__name__)
@app.route("/")
def test():
    return "Hello, Flask"

@app.route("/home")
def next():
    return 'This is the next page'

if __name__ == '__main__':
    
    app.run(debug = True, port = 9092)
    