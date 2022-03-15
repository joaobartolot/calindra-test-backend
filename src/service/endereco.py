import requests
from ..model.distancia import DistanciaModel

from utils.geometria import calcular_distancia_euclidiana

from ..model.endereco import EnderecoModel


class EnderecoService():
    def get_geocoding(self, endereco_str: str) -> list[EnderecoModel]:
        maps_api_response = requests.get(
            url=f"https://maps.googleapis.com/maps/api/geocode/json?address={endereco_str}&key=AIzaSyAWfWpIZRcmCZiXKAK0P113A_2Bf86Hqv4").json()

        result = maps_api_response['results'][0]

        # TODO: implement error handling
        location = result['geometry']['location']

        endereco = EnderecoModel(
            endereco_str, location['lat'], location['lng'])

        return endereco

    def calcular_distancia_cidades(self, cidades: list[EnderecoModel]) -> list[DistanciaModel]:
        distancias: list[DistanciaModel] = list()

        for i in range(len(cidades)):
            distancia = DistanciaModel(cidades[i])
            for j in range(i + 1, len(cidades)):
                distancia.endereco_b = cidades[j]
                distancia.calcular_distancia()

                distancias.append(distancia)

        return distancias
