import os
import json

class FileManager:
    """Класс для управления файлами заметок."""

    def __init__(self, storage_dir='notes'):
        """Инициализация менеджера файлов.

        Args:
            storage_dir (str): Директория для хранения заметок (по умолчанию 'notes').
        """
        self.storage_dir = storage_dir
        if not os.path.exists(storage_dir):
            os.makedirs(storage_dir)

    def save_note(self, filename, content):
        """Сохраняет заметку в файл.

        Args:
            filename (str): Имя файла для сохранения заметки.
            content (str): Содержимое заметки для сохранения.
        """
        filepath = os.path.join(self.storage_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as file:
            json.dump(content, file)

    def load_note(self, filename):
        """Загружает заметку из файла.

        Args:
            filename (str): Имя файла для загрузки заметки.

        Returns:
            dict: Содержимое заметки, если файл существует, иначе None.
        """
        filepath = os.path.join(self.storage_dir, filename)
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as file:
                return json.load(file)
        return None

    def list_notes(self):
        """Возвращает список всех заметок в директории.

        Returns:
            list: Список имен файлов заметок.
        """
        return os.listdir(self.storage_dir)
