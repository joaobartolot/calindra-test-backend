from flask_restful import Resource, reqparse

from src.service.endereco import EnderecoService


class DistanciaEuclidianaResource(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('endereco', type=str)

        endereco = parser.parse_args()['endereco']

        endereco_service = EnderecoService()

        lista_end_str = endereco.split(';')

        if len(lista_end_str) > 1:
            lista_end = list()

            for end_str in lista_end_str:

                try:
                    end_model = endereco_service.get_geocoding(end_str)
                except Exception as e:
                    return {'status': f'{e}'}

                lista_end.append(end_model)

            lista_distancias = endereco_service.calcular_distancia_cidades(
                lista_end, True)

            retorno = [distancia.to_json() for distancia in lista_distancias]

            return sorted(retorno, key=lambda d: d['distancia'], reverse=True)

        return "Porfavor adicione dois ou mais enderecos separados por ';'"
