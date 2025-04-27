# app.py
from flask import Flask, render_template, request, redirect, url_for
from login import login # Import the login function

app = Flask(__name__)
app.secret_key = 'your_secret_key_here' # Needed for flashing messages or sessions

# Simple "database" check (replace with actual logic)
def check_credentials(username, password):
    return login(username, password)

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login_route():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        if check_credentials(username, password):
            # In a real app, you'd set a session cookie here
            return redirect(url_for('dashboard'))
        else:
            # In a real app, you'd flash an error message
            error = "Invalid username or password"
            return render_template('login.html', error=error)

    # GET request
    return render_template('login.html', error=None)

@app.route('/dashboard')
def dashboard():
    # In a real app, you'd check if the user is authenticated
    # For this example, we just show the success page if they reach here
    return render_template('dashboard.html')

if __name__ == '__main__':
    # This is for running the app manually
    app.run(debug=True)