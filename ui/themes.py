class Theme:
    def __init__(self):
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
        if theme_name in self.themes:
            self.current_theme = theme_name
        else:
            raise ValueError(f"Theme '{theme_name}' not found.")

    def get_current_theme(self):
        return self.themes[self.current_theme]

    def list_themes(self):
        return list(self.themes.keys())
