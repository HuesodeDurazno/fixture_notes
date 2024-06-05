



## ========= Custom markers

# Pdemos clasificar test con custom markers

# para correr solo ciertas etiquetas ocupar -m 
# si no configuramos los custom markers obtendremos un warning , se configuran en pytest.ini , al registrar nuestros markers evitamos errores tipograficos indeseados



import pytest
from users import UserManagement

# podemos ocupar pytestmark para marcar todos los test con un custom marker
#tambien puede ser una lista
# importante : si agregamos tags sobre las funciones se tomara el tag mas especifico
pystestmark = pytest.mark.global_test

@pytest.mark.admin
def test_register_admin():
    user_mgmt = UserManagement()
    user_mgmt.register_user("admin", "admin123", "admin")
    assert "admin" in user_mgmt.users

@pytest.mark.user
def test_register_user():
    user_mgmt = UserManagement()
    user_mgmt.register_user("user", "user123", "user")
    assert "user" in user_mgmt.users

@pytest.mark.admin
def test_login_admin():
    user_mgmt = UserManagement()
    user_mgmt.register_user("admin", "admin123", "admin")
    assert user_mgmt.login("admin", "admin123")



@pytest.mark.admin
def test_find_admins():
    user_mgmt = UserManagement()
    user_mgmt.register_user("admin", "admin123", "admin")
    user_mgmt.register_user("user", "user123", "user")
    assert "admin" in user_mgmt.find_users_by_role("admin")



#podemos decorar clases

@pytest.mark.class_test
class TestClass:
    
    @pytest.mark.user
    def test_login_user(self):
        user_mgmt = UserManagement()
        user_mgmt.register_user("user", "user123", "user")
        assert user_mgmt.login("user", "user123")

    @pytest.mark.user
    def test_find_users(self):
        user_mgmt = UserManagement()
        user_mgmt.register_user("admin", "admin123", "admin")
        user_mgmt.register_user("user", "user123", "user")
        assert "user" in user_mgmt.find_users_by_role("user")


# Podemos agregar mark en una parametrizacion
# Puedes ocupar una lista en marks para diferentes marcas

@pytest.mark.parametrize("start_state", [
    "todo",
    pytest.param("in prog", marks=pytest.mark.param_normal),
    "done",
])
def test_register_user(start_state):
    user_mgmt = UserManagement()
    username = f"user_{start_state}"
    password = "password123"
    role = start_state
    user_mgmt.register_user(username, password, role)
    assert start_state in ["todo", "in prog", "done"]
    

# Podemos generar tambien un fixture

import pytest

@pytest.fixture(params=[
    "todo",
    pytest.param("in prog", marks=pytest.mark.param_fixture),
    "done",
])
def user_state(request):
    return request.param

def test_user_state(user_state):
    user_mgmt = UserManagement()
    username = f"user_{user_state}"
    password = "password123"
    role = user_state
    user_mgmt.register_user(username, password, role)
    assert user_mgmt.find_users_by_role(role) == [username]
    
# Para solicitar una ejecucion con varios tipos de tag puedes ocupar () , and , or , la condicion debe ir con ""
# Pdemos combinarlas con -k  para encontrar palabras cables

# pytest -m "param_fixture and param_normal"  .\custom_markers.py -v

# si queremos que el filtrado por tag sea estricto y en caso de no encontrar tags configurados lance un error ocupar  --strict-markers 
# tambien se puede configurar en el ini para tomar como default
# addopts = 
#    --strict-markers