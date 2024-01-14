from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/run_python_code', methods=['POST'])
def run_python_code():
    data = request.get_json()
    python_code = data['code']

    try:
        result = subprocess.check_output(['python', '-c', python_code], stderr=subprocess.STDOUT, text=True)
        response = {'output': result}
    except subprocess.CalledProcessError as e:
        response = {'output': f'Error: {e.output}'}

    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
