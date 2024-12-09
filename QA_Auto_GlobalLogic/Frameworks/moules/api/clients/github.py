import request


class GitHub:

  def get_user_defunkt(self):
    r = request.get('https://api.github.com/users/defunkt')
    body = r.json

    return body
