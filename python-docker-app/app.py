from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define the basic route
@app.route('/')
def hello_world():
    return 'sample image is to deploy in docker, inside the image {Hello, World!.}'

# Start the server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
