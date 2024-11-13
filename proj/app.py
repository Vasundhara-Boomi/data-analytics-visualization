from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_interests = request.form['user_interests']
    result = subprocess.check_output(['python', 'recommendation.py', user_interests]).decode('utf-8')
    print(result)
    return render_template('index.html', user_interests=user_interests, recommendations=result)

if __name__ == '__main__':
    app.run(debug=True)
