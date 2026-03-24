# Khan

An interactive educational web application about Genghis Khan's history and influence in the modern world.

Built with Flask for flexibility to support multiple data sources and topics.

## Setup

### 1. Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Run the application
```bash
python app.py
```

The app will be available at `http://localhost:5000`

## Project Structure

```
Khan/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── data/                  # Data sources (JSON, CSV, etc.)
├── templates/             # HTML templates
├── static/                # CSS, JavaScript, images
└── README.md
```

## Development

- Add new data sources in the `data/` directory
- Create routes in `app.py` for different topics/pages
- Use templates for reusable UI components
