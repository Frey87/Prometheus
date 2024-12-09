import request


class GitHub:

  def get_user_defunkt(self):
    r = request.get('https://api.github.com/users/defunkt')
    body = r.json

    return body

  def get_non_exist_user(self):
    r = request.get('https://api.github.com/users/butenkosergii')
    body = r.json

    return body
    
