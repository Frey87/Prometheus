import pytest
from moules.api.clients.github import GitHub

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
  
@pytest.mark.api
def test_repo_can_be_found(github_api):
  r = github_api.search_repo('become-qa-auto')
  assert r['total_count'] == 58
  assert 'become-qa-auto' in r['items'][0]['name']


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
  r = github_api.search_repo('sergiibutenko_repo_non_exist')
  assert r['total_count'] == 0



@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
  r = github_api.search_repo('s')
  assert r['total_count'] != 0
