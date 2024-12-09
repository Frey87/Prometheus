import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
  api = GitHub()
  user = github_api.get_user_defunkt()
  assert user['login'] == 'defunkt'
  
@pytest.mark.api
def test_user_not_exists(github_api):
  api = GitHub()
  r = github_api.get_non_exist_user()
  assert r['message'] == 'Not Found'
