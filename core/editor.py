class TextEditor:
    """Класс для текстового редактора с базовыми функциями."""

    def __init__(self):
        """Инициализация текстового редактора."""
        self.content = ""

    def add_text(self, text):
        """Добавляет текст в редактор.

        Args:
            text (str): Текст для добавления.
        """
        self.content += text

    def clear_text(self):
        """Очищает текст в редакторе."""
        self.content = ""

    def get_text(self):
        """Возвращает текущий текст редактора.

        Returns:
            str: Текущий текст.
        """
        return self.content

    def save_to_file(self, filename):
        """Сохраняет текущий текст в файл.

        Args:
            filename (str): Имя файла для сохранения.
        """
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.content)

    def load_from_file(self, filename):
        """Загружает текст из файла.

        Args:
            filename (str): Имя файла для загрузки.
        """
        with open(filename, 'r', encoding='utf-8') as file:
            self.content = file.read()
