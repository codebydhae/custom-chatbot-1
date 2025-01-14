#match best response to inputs given to chatbot
import json
from difflib import get_close_matches

#load kb to program
def load_knowledge_base(file_path: str) -> dict:
    with open(file_path, 'r') as file:
        data: dict = json.load(file)
        print(data)
    return data

load_knowledge_base('knowledge_base.json')