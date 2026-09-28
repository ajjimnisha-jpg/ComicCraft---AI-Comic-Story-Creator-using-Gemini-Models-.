# ComicCraft – AI Comic Story Creator using Gemini Models

## Project Description
ComicCraft is a Python-based AI application that converts a user's story idea into a structured comic story using a Gemini model.

## Features
- User story prompt
- AI-generated title
- Character descriptions
- Multiple comic panels
- Scene descriptions
- Dialogue
- Narration
- Tkinter GUI
- Save generated comic as a text file
- Console version

## Requirements
- Python 3.10 or later
- Gemini API key
- Internet connection

## Installation

```bash
pip install -r requirements.txt
```

## API Key
Open `src/comiccraft_gui.py` or `src/comiccraft_console.py` and replace:

```python
API_KEY = "YOUR_GEMINI_API_KEY"
```

with your own key.

For a real deployment, use an environment variable instead of putting the key directly in source code.

## Run GUI

```bash
python src/comiccraft_gui.py
```

## Run Console Version

```bash
python src/comiccraft_console.py
```
