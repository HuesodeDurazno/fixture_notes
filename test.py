# los markadores son una forma de "anotar" los test , nos sirven para separar los test 

# Existen buildin y custom

#Utiles

# @pytest.mark.parametrize()
# • @pytest.mark.skip()
# • @pytest.mark.skipif()
# • @pytest.mark.xfail()


##uso de skip y skipif

# Se usan para SALTAR la ejecucion de un test, skipif lo hace teniendo en cuenta en
# Para poder ver las rasones al final del log de ejecucion ocupar -ra. 

import pytest
import sys
from calculadora import Calculadora

@pytest.fixture
def calc():
    return Calculadora()

@pytest.mark.skip(reason="Esta prueba está omitida temporalmente")
def test_sumar(calc):
    assert calc.sumar(1, 2) == 3

def test_restar(calc):
    assert calc.restar(5, 3) == 2

@pytest.mark.skip(reason="Esta prueba está omitida porque la división por cero será tratada más tarde")
def test_dividir_por_cero(calc):
    with pytest.raises(ValueError):
        calc.dividir(1, 0)

def test_multiplicar(calc):
    assert calc.multiplicar(2, 3) == 6

def test_dividir(calc):
    assert calc.dividir(10, 2) == 5

# Ejemplo de uso de skipif para omitir prueba en Windows
@pytest.mark.skipif(sys.platform.startswith("win"), reason="Esta prueba no se ejecuta en sistemas Windows")
def test_raiz_cuadrada(calc):
    assert calc.raiz_cuadrada(9) == 3

# Ejemplo de uso de skipif para omitir prueba si Python es menor que 3.8
@pytest.mark.skipif(sys.version_info < (3, 8), reason="Esta prueba requiere Python 3.8 o superior")
def test_raiz_cuadrada_negativo(calc):
    with pytest.raises(ValueError):
        calc.raiz_cuadrada(-4)


## X fail

#usado para correr todos los test , sabiendo que alguno de ellos va a fallar 
# Por default el test se va a ejecutar pero podemos controlar esto con xfail
# raises indica una exception que queremos que se cataloge como  un xfail
# stric inca que si un test marcado con xfail pasa sea maracado como xpass o Failed



# Ejemplo de uso de xfail con una condición y el atributo raises
@pytest.mark.xfail(sys.version_info < (3, 9), reason="Esta prueba requiere Python 3.9 o superior", raises=ValueError)
def test_potencia_negativa(calc):
    assert calc.potencia(2, -1) == 0.5

# Ejemplo de uso de xfail con el parámetro run
@pytest.mark.xfail(run=False, reason="Esta prueba debería manejar exponentes fraccionarios, pero no lo hace",strict=False)
def test_potencia_fraccionaria(calc):
    assert calc.potencia(9, 0.5) == 3

# Ejemplo de uso de xfail sin condición
@pytest.mark.xfail(reason="Esta prueba está marcada como xfail sin condiciones específicas")
def test_potencia(calc):
    assert calc.potencia(2, 3) == 8
    
#Razones para xfail:

# estas ocupando test-driven-development 
# Dejar de marcar como fallidos para fixear el test

# Razones para no ocupar:

# como pruebas de una feature aun no implementada


