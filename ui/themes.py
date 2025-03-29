class Theme:
    def __init__(self):
        self.themes = {
            'light': {
                'background': '#ffffff',
                'text_color': '#000000'
            },
            'dark': {
                'background': '#333333',
                'text_color': '#ffffff'
            },
            'blue': {
                'background': '#007BFF',
                'text_color': '#ffffff'
            }
        }
        self.current_theme = 'light'

    def set_theme(self, theme_name):
        if theme_name in self.themes:
            self.current_theme = theme_name
        else:
            raise ValueError(f"Theme '{theme_name}' not found.")

    def get_current_theme(self):
        return self.themes[self.current_theme]
