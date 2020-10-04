import os
from flask import Flask, request, render_template
from src.controller.search_controller import second

app = Flask(__name__)
app.register_blueprint(second)

# Blueprints & Using Multiple Python Files
# https://www.youtube.com/watch?v=WteIH6J9v64&ab_channel=TechWithTim

if __name__ == "__main__":
    # app.run(debug=True, port=8080)
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)