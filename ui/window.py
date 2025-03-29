import tkinter as tk
from tkinter import scrolledtext, messagebox, Menu
from .themes import Theme

class MainWindow:
    """Класс для создания главного окна приложения."""

    def __init__(self, title="NoteMaster"):
        """Инициализация главного окна.

        Args:
            title (str): Заголовок окна (по умолчанию "NoteMaster").
        """
        self.root = tk.Tk()
        self.root.title(title)
        self.theme = Theme()
        self.setup_ui()

    def setup_ui(self):
        """Настраивает пользовательский интерфейс."""
        # Создание текстовой области
        self.text_area = scrolledtext.ScrolledText(self.root, wrap=tk.WORD, font=("Arial", 12))
        self.text_area.pack(expand=True, fill='both')

        # Создание меню
        self.create_menu()

        # Применение текущей темы
        self.apply_theme()

        # Обработка закрытия окна
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def create_menu(self):
        """Создает меню приложения."""
        menu_bar = Menu(self.root)

        # Файл
        file_menu = Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Сохранить", command=self.save_note)
        file_menu.add_command(label="Загрузить", command=self.load_note)
        file_menu.add_separator()
        file_menu.add_command(label="Выход", command=self.on_closing)
        menu_bar.add_cascade(label="Файл", menu=file_menu)

        # Настройки
        settings_menu = Menu(menu_bar, tearoff=0)
        settings_menu.add_command(label="Сменить тему", command=self.change_theme)
        menu_bar.add_cascade(label="Настройки", menu=settings_menu)

        self.root.config(menu=menu_bar)

    def apply_theme(self):
        """Применяет текущую тему к интерфейсу."""
        current_theme = self.theme.get_current_theme()
        self.root.configure(bg=current_theme['background'])
        self.text_area.configure(bg=current_theme['background'], fg=current_theme['text_color'])

    def change_theme(self):
        """Сменяет тему на следующую в списке доступных тем."""
        available_themes = self.theme.list_themes()
        current_index = available_themes.index(self.theme.current_theme)
        new_index = (current_index + 1) % len(available_themes)
        new_theme = available_themes[new_index]
        self.theme.set_theme(new_theme)
        self.apply_theme()

    def save_note(self):
        """Сохраняет текущую заметку в файл."""
        filename = "note.txt"  # Замените на диалог выбора файла
        content = self.text_area.get("1.0", tk.END)
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(content)
        messagebox.showinfo("Сохранение", f"Заметка сохранена в {filename}")

    def load_note(self):
        """Загружает заметку из файла."""
        filename = "note.txt
