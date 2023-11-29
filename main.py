from flask import Flask

app = Flask('lab1')

@app.route('/api/v1/hello-world-14', methods=['GET'])
def hello_world():
    return "Hello World 14"
