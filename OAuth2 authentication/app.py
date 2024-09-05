from flask import Flask, redirect, url_for, session
from flask_dance.contrib.google import make_google_blueprint, google
from flask_dance.contrib.facebook import make_facebook_blueprint, facebook
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = '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'

# OAuth2 Client Setup
app.config['GOOGLE_CLIENT_ID'] = 'your_google_client_id'
app.config['GOOGLE_CLIENT_SECRET'] = 'your_google_client_secret'
app.config['FACEBOOK_CLIENT_ID'] = 'your_facebook_app_id'
app.config['FACEBOOK_CLIENT_SECRET'] = 'your_facebook_app_secret'

# Flask-Login Setup
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

class User(UserMixin):
    def __init__(self, id_, name, email, profile_pic):
        self.id = id_
        self.name = name
        self.email = email
        self.profile_pic = profile_pic

# In-memory user store (replace with database in a production app)
users = {}

@login_manager.user_loader
def load_user(user_id):
    return users.get(user_id)

# Google OAuth Blueprint
google_bp = make_google_blueprint(client_id=app.config['GOOGLE_CLIENT_ID'],
                                  client_secret=app.config['GOOGLE_CLIENT_SECRET'],
                                  redirect_to='google_login')
app.register_blueprint(google_bp, url_prefix="/login")

# Facebook OAuth Blueprint
facebook_bp = make_facebook_blueprint(client_id=app.config['FACEBOOK_CLIENT_ID'],
                                      client_secret=app.config['FACEBOOK_CLIENT_SECRET'],
                                      redirect_to='facebook_login')
app.register_blueprint(facebook_bp, url_prefix="/login")

@app.route('/')
@login_required
def home():
    return f'Welcome {current_user.name}! <br><a href="/logout">Logout</a>'

@app.route('/login')
def login():
    return '''
        <a href="/login/google">Login with Google</a><br>
        <a href="/login/facebook">Login with Facebook</a>
    '''

@app.route('/login/google')
def google_login():
    if not google.authorized:
        return redirect(url_for('google.login'))
    resp = google.get('/oauth2/v1/userinfo')
    user_info = resp.json()
    user = User(user_info['id'], user_info['name'], user_info['email'], user_info['picture'])
    users[user_info['id']] = user
    login_user(user)
    return redirect(url_for('home'))

@app.route('/login/facebook')
def facebook_login():
    if not facebook.authorized:
        return redirect(url_for('facebook.login'))
    resp = facebook.get('/me?fields=id,name,email')
    user_info = resp.json()
    user = User(user_info['id'], user_info['name'], user_info['email'], None)
    users[user_info['id']] = user
    login_user(user)
    return redirect(url_for('home'))

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
