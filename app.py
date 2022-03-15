from flask import Flask
from flask_restful import Api


from src.controller.distancia import DistanciaResource
from src.controller.distancia_euclidiana import DistanciaEuclidianaResource

app = Flask(__name__)
api = Api(app)

api.add_resource(DistanciaResource, '/api/distancia')
api.add_resource(DistanciaEuclidianaResource, '/api/distancia-euclidiana')


if __name__ == '__main__':
    app.run(debug=True)
