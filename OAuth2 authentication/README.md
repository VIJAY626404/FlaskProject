# OAuth 2.0 Authentication with Flask
This project demonstrates how to implement OAuth 2.0 authentication using Flask. The application allows users to log in using their Google or Facebook accounts and manages user sessions using Flask-Login.

## Project Overview
This Flask application showcases the integration of Google and Facebook OAuth 2.0 for user authentication. The project is a simple demonstration of how to implement social logins in a web application. Users can log in using either their Google or Facebook accounts, and their session is managed by Flask-Login.

## Features
- OAuth 2.0 authentication with Google and Facebook.
- User session management using Flask-Login.
- User information retrieval from Google and Facebook APIs.
- Simple home page that greets the user after login.
- Logout functionality.
## Project Structure
- app.py: The main application file that handles routing, user authentication, and session management.
## Prerequisites
Before you begin, ensure you have met the following requirements:
- Python 3.6+
- Flask
- Flask-Dance
- Flask-Login
- ## Installation
  1. **Clone the repository:**
  ``` base
  git clone https://github.com/your-username/oauth2-authentication-flask.git
  cd oauth2-authentication-flask
  ```
2. **Install the required Python packages:**
  ``` base
 pip install -r requirements.txt
```
3. **Set up your OAuth credentials:**

- For Google: Create a project in the Google Developer Console, and obtain your GOOGLE_CLIENT_ID and GOOGLE_CLIENT_SECRET.
- For Facebook: Create an app in the Facebook Developer Console, and obtain your FACEBOOK_CLIENT_ID and FACEBOOK_CLIENT_SECRET.
4. **Add your credentials to the app.py file:**
  ``` base
  app.config['GOOGLE_CLIENT_ID'] = 'your_google_client_id'
  app.config['GOOGLE_CLIENT_SECRET'] = 'your_google_client_secret'
  app.config['FACEBOOK_CLIENT_ID'] = 'your_facebook_app_id'
  app.config['FACEBOOK_CLIENT_SECRET'] = 'your_facebook_app_secret'
  ```
5. Run the application:
   ``` base
   python app.py
   ```
## Usage
- To log in, visit the /login route and choose to log in with either Google or Facebook.
- Once authenticated, you will be redirected to the home page where your name will be displayed.
- You can log out by visiting the /logout route.
  
## Future Enhancements
- Database Integration: Replace the in-memory user store with a database such as SQLite or PostgreSQL.
- Enhanced User Profiles: Store additional user information and allow users to update their profiles.
- Security Improvements: Implement additional security measures like HTTPS and CSRF protection.
## Suggested Project Names
If you prefer to use a different project name, here are some suggestions:

- Social Authenticator: A more descriptive name focusing on the integration with social login platforms.
- Flask OAuth Gateway: Highlighting the OAuth 2.0 implementation in Flask.
- Social Media Login System: Emphasizing the use of social media for authentication.
## License
This project is licensed under the MIT License. See the LICENSE file for more details.
