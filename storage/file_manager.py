import os
import json

class FileManager:
    def __init__(self, storage_dir='notes'):
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)

    def save_note(self, filename, content):
        filepath = os.path.join(self.storage_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(content, file)

    def load_note(self, filename):
        filepath = os.path.join(self.storage_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as file:
                return json.load(file)
        return None

    def list_notes(self):
        return os.listdir(self.storage_dir)
