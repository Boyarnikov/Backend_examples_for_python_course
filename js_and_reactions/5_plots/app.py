from flask import Flask, render_template, jsonify
import plotly
import plotly.graph_objects as go
import json
import random
import threading
import time

app = Flask(__name__)


chart_data = {
    'labels': ['A', 'B', 'C'],
    'values': [20, 14, 23]
}

def update_chart_data():
    while True:
        chart_data['values'] = [item + random.randint(-1, 1) for item in chart_data['values']]
        time.sleep(1)

@app.route('/')
def index():
    fig = go.Figure(data=[go.Pie(labels=chart_data['labels'], values=chart_data['values'])])
    fig.plotly_restyle()
    fig.update_layout(title_text='Dynamic Pie Chart Example')

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('index.html', graphJSON=graphJSON)

@app.route('/update')
def update():
    fig = go.Figure(data=[go.Pie(labels=chart_data['labels'], values=chart_data['values'])])
    fig.update_layout(title_text='Dynamic Pie Chart Example')

    return jsonify(json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder))


threading.Thread(target=update_chart_data, daemon=True).start()