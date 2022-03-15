from ..model.endereco import EnderecoModel
from utils.geometria import calcular_distancia_euclidiana, haversine


class DistanciaModel:
    def __init__(self, endereco_a: EnderecoModel, endereco_b: EnderecoModel = None, distancia: int = None):
        self.endereco_a = endereco_a
        self.endereco_b = endereco_b
        self.distancia = distancia

    def calcular_distancia(self, euclidiana: bool = False):
        if not euclidiana:
            self.distancia = haversine(
                self.endereco_a.ponto_cartesiano(), self.endereco_b.ponto_cartesiano())
        else:
            self.distancia = calcular_distancia_euclidiana(
                self.endereco_a.ponto_cartesiano(), self.endereco_b.ponto_cartesiano())

    def to_json(self):
        return {
            'endereco_a': self.endereco_a.to_json(),
            'endereco_b': self.endereco_b.to_json(),
            'distancia': self.distancia,
        }
