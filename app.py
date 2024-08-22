from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from general_sentiments import analyze_general_sentiment
from fine_grain_sentiments import analyze_fine_grain_sentiment

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Set a secret key for session management

# Dummy user database for demonstration purposes
users = {
    'john': 'password1',
    'jane': 'password2',
    'Praneeth': 'praneeth',
    'Bhanu': 'bhanu',
    'Yaswanth': 'yaswanth'
}

@app.route('/')
def index():
    if 'username' in session:
        return render_template('index.html', username=session['username'])
    else:
        return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        if username in users and users[username] == password:
            session['username'] = username
            return redirect(url_for('index'))
        else:
            return 'Invalid username or password'

    # If it's a GET request, render the login form
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

@app.route('/general_sentiments', methods=['GET', 'POST'])
def general_sentiments():
    if request.method == 'POST':
        text = request.form['text']
        sentiment = analyze_general_sentiment(text)
        return render_template('general_sentiments.html', input_text=text, sentiment=sentiment)
    else:
        return render_template('general_sentiments.html')

@app.route('/fine_grain_sentiments', methods=['GET', 'POST'])
def fine_grain_sentiments():
    if request.method == 'POST':
        text = request.form['text']
        sentiment = analyze_fine_grain_sentiment(text)
        return render_template('fine_grain_sentiments.html', input_text=text, sentiment=sentiment)
    else:
        return render_template('fine_grain_sentiments.html')

if __name__ == '__main__':
    app.run(debug=True)
