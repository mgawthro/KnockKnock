from flask import Flask, render_template, request, jsonify, make_response, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/potential')
def potential():
    return render_template('potential.html')

@app.route('/current')
def current():
    return render_template('current.html')

@app.route('/api/store_data', methods=['POST'])
def store_data():
    data = request.json
    # Process and store data in the database (you can use SQLAlchemy or any other preferred database library)
    # Example: data_processing_function(data)
    return jsonify({'success': True})

if __name__ == '__main__':
    app.run(debug=True)