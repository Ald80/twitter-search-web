import os
from flask import Flask
from routes import second

app = Flask(__name__)
app.register_blueprint(second)

if __name__ == "__main__":
    app.run(debug=True, port=8080)
    # port = int(os.environ.get("PORT", 5000))
    # app.run(host='0.0.0.0', port=port)