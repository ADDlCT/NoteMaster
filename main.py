from ui.window import MainWindow
from core.editor import TextEditor
from core.spellchecker import SpellCheck
from storage.file_manager import FileManager
from storage.settings import Settings


def main():
    # Инициализация компонентов
    editor = TextEditor()
    spell_checker = SpellCheck(language='en')  # Можно изменить на 'ru' для русского
    file_manager = FileManager()
    settings = Settings()

    # Создание главного окна приложения
    main_window = MainWindow(title="NoteMaster")

    # Запуск пользовательского интерфейса
    main_window.run()


if __name__ == "__main__":
    main()
