from flask import Flask, render_template, jsonify
import os

app = Flask(__name__)

# Configuration
app.config['DEBUG'] = True

@app.route('/')
def home():
    """Home page with overview of available topics."""
    return render_template('index.html')

@app.route('/api/topics')
def get_topics():
    """API endpoint to fetch available topics."""
    # TODO: Load topics from data sources dynamically
    topics = {
        'genghis_khan': {
            'title': 'Genghis Khan',
            'description': 'The rise and influence of Genghis Khan'
        }
    }
    return jsonify(topics)

@app.route('/topic/<topic_id>')
def topic_page(topic_id):
    """Display a specific topic."""
    return render_template('topic.html', topic_id=topic_id)

@app.route('/api/topic/<topic_id>')
def get_topic_data(topic_id):
    """API endpoint to fetch data for a specific topic."""
    # TODO: Load data from data sources based on topic_id
    return jsonify({'topic_id': topic_id, 'data': {}})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
