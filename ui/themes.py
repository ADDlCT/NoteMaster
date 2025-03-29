class Theme:
    """Класс для управления темами оформления приложения."""

    def __init__(self):
        """Инициализация доступных тем."""
        self.themes = {
            'light': {
                'background': '#ffffff',
                'text_color': '#000000',
                'highlight_color': '#f0f0f0'
            },
            'dark': {
                'background': '#333333',
                'text_color': '#ffffff',
                'highlight_color': '#444444'
            },
            'blue': {
                'background': '#007BFF',
                'text_color': '#ffffff',
                'highlight_color': '#0056b3'
            }
        }
        self.current_theme = 'light'  # Установка темы по умолчанию

    def set_theme(self, theme_name):
        """Устанавливает текущую тему.

        Args:
            theme_name (str): Имя темы для установки.

        Raises:
            ValueError: Если тема не найдена.
        """
        if theme_name in self.themes:
            self.current_theme = theme_name
        else:
            raise ValueError(f"Theme '{theme_name}' not found.")

    def get_current_theme(self):
        """Возвращает параметры текущей темы.

        Returns:
            dict: Параметры текущей темы (цвета фона, текста и выделения).
        """
        return self.themes[self.current_theme]

    def list_themes(self):
        """Возвращает список доступных тем.

        Returns:
            list: Список имен доступных тем.
        """
        return list(self.themes.keys())
