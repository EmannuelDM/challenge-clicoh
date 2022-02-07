import pytest
from applications.users.models import User

@pytest.mark.django_db #para dar acceso a la base de datos
def test_user_creation():

    user = User.objects.create_user(
        email="testing@gmail.com",
        password="Test_1234"
    )

    assert user.email == "testing@gmail.com"


@pytest.mark.django_db 
def test_user_creation_fail():
    with pytest.raises(Exception):
        user = User.objects.create_user(
            password="Test_pass_fail"
        )
