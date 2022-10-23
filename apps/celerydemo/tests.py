import pytest
from django.contrib.auth.models import User






@pytest.fixture
def function_fixture():
   print('Fixture for each test')
   return 1


@pytest.fixture(scope='module')
def module_fixture():
   print('Fixture for module')
   return 2

@pytest.fixture
def simple_yield_fixture():
   print('setUp part')
   yield 3
   print('tearDown part')


@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
  assert User.objects.count() == 1