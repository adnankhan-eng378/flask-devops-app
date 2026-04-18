from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello DevOps World IAM ADNAN KHAN  add rollback in this AJ project 🚀"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)