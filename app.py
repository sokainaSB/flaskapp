# app.py
from flask import Flask, render_template, request
from buttonrunscript import main as run_script

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('webappsou.html', output=None)

@app.route('/run_script', methods=['POST'])
def execute_script():
    if 'url' in request.form:
        url = request.form['url']

        # Call the main function from buttonrunscript.py
        output = run_script(url)

        return render_template('webappsou.html', output=output)

    return render_template('webappsou.html', output=None)

if __name__ == '__main__':
    app.run(debug=True)
