from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Sample data for searching
data = [
    "Apple",
    "Banana",
    "Cherry",
    "Date",
    "Fig",
    "Grape",
    "Kiwi",
    "Lemon",
    "Mango",
    "Orange",
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('query', '').lower()
    results = [item for item in data if query in item.lower()]
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True)