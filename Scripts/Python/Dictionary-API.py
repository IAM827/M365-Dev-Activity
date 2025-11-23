import random
import requests
from flask import Flask, jsonify

# --- Configuration ---
WORDNIK_API_KEY = "YOUR_WORDNIK_API_KEY"  # <-- REMEMBER TO UPDATE THIS
WORDNIK_API_URL = "http://api.wordnik.com/v4/word.json/{word}/definitions"
WORDLIST_FILENAME = "words_alpha.txt" # The name of the file you downloaded

app = Flask(__name__)

# --- Load the Word List Once at Startup ---
def load_words(filename):
    """Reads the word list from a file and returns it as a list."""
    try:
        print(f"Loading word list from '{filename}'...")
        with open(filename, 'r') as file:
            # Read all lines, strip whitespace (like newlines), and convert to a list
            word_list = [line.strip().lower() for line in file]
        print(f"Successfully loaded {len(word_list)} words.")
        return word_list
    except FileNotFoundError:
        print(f"ERROR: Word list file '{filename}' not found. Using a small fallback list.")
        return ["error", "loading", "file", "please", "check"] # Fallback list

# Global variable to store the loaded word list
# This runs once when the application starts
WORD_LIST = load_words(WORDLIST_FILENAME)

# --- Functions ---

def get_random_word():
    """Selects a random word from the large list."""
    # Filter for words that are not too short or too long for dictionary lookups
    valid_words = [word for word in WORD_LIST if 3 <= len(word) <= 15]
    if valid_words:
        return random.choice(valid_words)
    return random.choice(WORD_LIST) # Fallback

def get_definition(word):
    # (The get_definition function remains the same as before)
    try:
        url = WORDNIK_API_URL.format(word=word)
        params = {
            "limit": 1, 
            "includeRelated": "false", 
            "useCanonical": "false", 
            "includeTags": "false",
            "api_key": WORDNIK_API_KEY
        }
        
        response = requests.get(url, params=params)
        response.raise_for_status()
        
        data = response.json()
        
        if data and 'text' in data[0]:
            return data[0]['text']
        else:
            return "Definition not found for this word."
            
    except requests.exceptions.RequestException as e:
        print(f"API Request Error for '{word}': {e}")
        return "Error fetching definition."
    except Exception as e:
        print(f"An unexpected error occurred for '{word}': {e}")
        return "An unexpected error occurred."


@app.route('/random-word-definition', methods=['GET'])
def random_word_definition():
    """
    API endpoint that generates a random word and returns its definition.
    """
    random_word = get_random_word()
    definition = get_definition(random_word)
    
    response_data = {
        "word": random_word,
        "definition": definition,
        "source": "Wordnik API"
    }
    
    return jsonify(response_data)


if __name__ == '__main__':
    app.run(debug=True)
