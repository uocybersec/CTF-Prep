from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html'), 200  

@app.route('/get-rating', methods=['POST'])
def add_rating():
    name = request.form.get('name')
    output = subprocess.check_output(f'cat ratings.txt | grep -i "{name}"', shell=True).decode()
    return output

if __name__ == '__main__':
    app.run("0.0.0.0", 1337, debug=False)