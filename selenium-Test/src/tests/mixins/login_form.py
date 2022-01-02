class LoginPageMixin:
  
  def get_login_form_data(self, 
  username="standard_user", 
  password="secret_sauce", 
  ):
    return {
      "username": username, 
      "password": password
    }
  