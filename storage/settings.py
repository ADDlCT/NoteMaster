import json
import os

class Settings:
    def __init__(self, settings_file='settings.json'):
        self.settings_file = settings_file
        self.settings = {}
        self.load_settings()

    def load_settings(self):
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r', encoding='utf-8') as file:
                self.settings = json.load(file)

    def save_settings(self):
        with open(self.settings_file, 'w', encoding='utf-8') as file:
            json.dump(self.settings, file)

    def get_setting(self, key, default=None):
        return self.settings.get(key, default)

    def set_setting(self, key, value):
        self.settings[key] = value
        self.save_settings()
