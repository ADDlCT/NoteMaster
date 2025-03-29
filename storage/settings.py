import json
import os

class Settings:
    """Класс для управления пользовательскими настройками."""

    def __init__(self, settings_file='settings.json'):
        """Инициализация менеджера настроек.

        Args:
            settings_file (str): Имя файла для хранения настроек (по умолчанию 'settings.json').
        """
        self.settings_file = settings_file
        self.settings = {}
        self.load_settings()

    def load_settings(self):
        """Загружает настройки из файла."""
        if os.path.exists(self.settings_file):
            with open(self.settings_file, 'r', encoding='utf-8') as file:
                self.settings = json.load(file)

    def save_settings(self):
        """Сохраняет текущие настройки в файл."""
        with open(self.settings_file, 'w', encoding='utf-8') as file:
            json.dump(self.settings, file)

    def get_setting(self, key, default=None):
        """Получает значение настройки по ключу.

        Args:
            key (str): Ключ настройки.
            default: Значение по умолчанию, если настройка не найдена.

        Returns:
            Значение настройки или значение по умолчанию.
        """
        return self.settings.get(key, default)

    def set_setting(self, key, value):
        """Устанавливает значение настройки по ключу.

        Args:
            key (str): Ключ настройки.
            value: Значение для установки.
        """
        self.settings[key] = value
        self.save_settings()
