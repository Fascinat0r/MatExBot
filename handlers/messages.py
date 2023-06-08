import json

# Load the messages from the JSON file
with open('../configs/language.json', 'r', encoding='utf-8') as f:
    messages = json.load(f)


# Get a message by key and language
def get(key, language):
    if language not in messages[key]:
        language = 'en'
    return messages[key][language]
