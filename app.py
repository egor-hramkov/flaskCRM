from flask import Flask

from users.views import users_bp
from flasgger import Swagger

app = Flask(__name__)
app.register_blueprint(users_bp)

Swagger(app)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
