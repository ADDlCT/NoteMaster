class TextEditor:
    def __init__(self):
        self.content = ""

    def add_text(self, text):
        self.content += text

    def clear_text(self):
        self.content = ""

    def get_text(self):
        return self.content

    def save_to_file(self, filename):
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(self.content)

    def load_from_file(self, filename):
        with open(filename, 'r', encoding='utf-8') as file:
            self.content = file.read()
