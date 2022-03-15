from math import radians, cos, sin, asin, sqrt


def haversine(ponto_a: set, ponto_b: set):
    """
    Calcular distancia entre dois pontos na terra usando a formula de Haversine
    """
    # conversao de graus para raios
    lng_a, lat_a, lng_b, lat_b = map(
        radians, [ponto_a[1], ponto_a[0], ponto_b[1], ponto_b[0]])

    # formula de haversine
    dlon = lng_b - lng_a
    dlat = lat_b - lat_a
    a = sin(dlat/2)**2 + cos(lat_a) * cos(lat_b) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Raio da terra
    return c * r


def calcular_distancia_euclidiana(ponto_a: set, ponto_b: set):
    return round(sqrt((((ponto_a[0] - ponto_b[0])**2) + ((ponto_a[1] - ponto_b[1])**2))), 10)
