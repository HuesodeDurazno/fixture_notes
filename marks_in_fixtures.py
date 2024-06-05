import pytest

# Definimos una clase Card para representar una tarjeta
class Card:
    def __init__(self, summary, owner):
        self.summary = summary
        self.owner = owner

# Creamos un accesorio (fixture) para generar una lista de cartas
@pytest.fixture(scope="function")
def cards_db(request):
    cards = []

    # Obtenemos el parámetro `num_cards` del marcador `@pytest.mark.num_cards`
    num_cards = request.node.get_closest_marker("num_cards").args[0]

    # Iteramos y agregamos cartas a la lista
    for i in range(num_cards):
        # Creamos instancias de Card con datos simples
        card = Card(summary=f"Summary {i}", owner=f"Owner {i}")
        cards.append(card)

    return cards

# Definimos una prueba que use la lista de cartas
@pytest.mark.num_cards(3)
def test_cards(cards_db):
    assert len(cards_db) == 3


# Obtener información sobre la prueba actual: Puedes obtener información sobre la función de prueba actual, el módulo de prueba, los marcadores, los parámetros pasados a la prueba, entre otros.

# Obtener marcadores (markers) específicos: Puedes obtener los marcadores asociados con la función de prueba actual usando request.node.iter_markers(). Esto es útil para personalizar el comportamiento de una prueba según los marcadores aplicados.

# Obtener argumentos de un marcador específico: Puedes obtener los argumentos pasados a un marcador específico usando request.node.get_closest_marker("nombre_del_marcador").args.

# Interactuar con el contexto de la prueba: Puedes acceder al contexto de la prueba actual, como el nombre de la función de prueba, el nombre del módulo, entre otros.