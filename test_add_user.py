from model.user import User
from conftest import app

def test_add_user(app):
    new_user = User.random_valid()
    app.add_user(new_user)
    assert app.is_logged_in()
    #app.logout()
    #assert app.is_not_logged_in()
    app.delete_user()
