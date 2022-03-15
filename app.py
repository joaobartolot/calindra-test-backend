from flask import Flask
from flask_restful import Api


from src.controller.endereco import EnderecoResource

app = Flask(__name__)
api = Api(app)


api.add_resource(EnderecoResource, '/api')


if __name__ == '__main__':
    app.run(debug=True)
