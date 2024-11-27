import pytest


class User:
  
  def __init__(self) -> None:
    self.name = None
    slf.secon_name = None

  def create(self):
    self.name = "Sergii"
    self.secon_name = "Butenko"

  def remove(self):
    self.name = ""
    self.secon_name = ""


@pytest.fixture
def user():
  user = User()
  user.create()

  yield user
  
  user.remove()


def test_change_name(user):
  assert user.name == "Sergii"


def test_change_second_name(user):
  assert user.second_name == "Butenko"
