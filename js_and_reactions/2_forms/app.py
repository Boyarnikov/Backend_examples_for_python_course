from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# In-memory storage for contact submissions
contacts = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    print(request.headers)
    contacts.append(data)  # Store the contact data in memory
    return jsonify({"message": "Contact submitted successfully!"}), 200

@app.route('/data')
def data():
    return jsonify(contacts)

if __name__ == '__main__':
    app.run(debug=True)
