# app.py
from flask import Flask, render_template, request, redirect, url_for, session
import os # Import os for secret key

app = Flask(__name__)
# Use a secret key from environment or default for example
# THIS IS CRITICAL FOR SESSIONS
app.secret_key = os.environ.get('SECRET_KEY', 'a_very_secret_key_for_testing_purposes_only')

# Simple "database" check (replace with actual logic)
def check_credentials(username, password):
    return login(username, password) # Assumes login function is imported from login.py

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if check_credentials(username, password):
            # Set a session variable upon successful login
            session['logged_in'] = True
            session['username'] = username # Optional: store username
            return redirect(url_for('dashboard'))
        else:
            error = "Invalid username or password"
            return render_template('login.html', error=error)

    # GET request
    # If already logged in, redirect to dashboard
    if session.get('logged_in'):
         return redirect(url_for('dashboard'))

    return render_template('login.html', error=None)

@app.route('/dashboard')
def dashboard():
    # Protect this route: check if the user is authenticated
    if not session.get('logged_in'):
        # If not logged in, redirect to login page
        return redirect(url_for('login_route'))

    # If logged in, show the dashboard
    username = session.get('username', 'User') # Get username from session if available
    return render_template('dashboard.html', username=username)


# Add a logout route
@app.route('/logout')
def logout_route():
    # Remove session variables to log the user out
    session.pop('logged_in', None)
    session.pop('username', None) # Clear username if stored

    # Redirect to the login page after logout
    return redirect(url_for('login_route'))


# Assuming login.py exists in the same directory or package
try:
    from login import login
except ImportError:
     print("Error: Could not import 'login' function from login.py")
     # You might want to handle this error more robustly in a real app
     # For this example, we'll assume login.py is present.
     pass # Or sys.exit(1)

if __name__ == '__main__':
    # This is for running the app manually
    app.run(debug=True)