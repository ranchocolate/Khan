# Data Sources

This directory contains data sources for different topics.

## Structure

Each topic should have its own JSON file:
- `genghis_khan.json` - Data about Genghis Khan and the Mongol Empire

## Format

Data files should be structured in JSON format for easy loading and processing by the Flask application.

Example structure:
```json
{
  "id": "genghis_khan",
  "title": "Genghis Khan",
  "timeline": [...],
  "sections": [...],
  "sources": [...]
}
```

You can expand this as needed for your content.
