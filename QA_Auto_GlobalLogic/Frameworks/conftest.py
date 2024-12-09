import pytest


class User:
  
  def __init__(self) -> None:
    self.name = None
    slf.second_name = None

  def create(self):
    self.name = "Sergii"
    self.second_name = "Butenko"

  def remove(self):
    self.name = ""
    self.second_name = ""


@pytest.fixture
def user():
  user = User()
  user.create()

  yield user
  
  user.remove()

@pytest.fixture
def github_api():
  api = GitHub()
  yield api
