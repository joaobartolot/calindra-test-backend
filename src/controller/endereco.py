from flask import jsonify
from flask_restful import Resource, reqparse

from src.service.endereco import EnderecoService


class EnderecoResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('endereco', type=str)

        endereco = parser.parse_args()['endereco']

        endereco_service = EnderecoService()

        lista_end_str = endereco.split(';')

        lista_end = list()

        for end_str in lista_end_str:
            print()
            lista_end.append(endereco_service.get_geocoding(end_str))

        lista_distancias = endereco_service.calcular_distancia_cidades(
            lista_end)

        retorno = [distancia.to_json() for distancia in lista_distancias]

        return sorted(retorno, key=lambda d: d['distancia'], reverse=True)
