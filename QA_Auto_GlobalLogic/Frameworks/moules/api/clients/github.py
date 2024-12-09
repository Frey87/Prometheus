import request


class GitHub:

  def get_user(self, username):
    r = request.get('https://api.github.com/users/{username}')
    body = r.json
    
    return body
    
