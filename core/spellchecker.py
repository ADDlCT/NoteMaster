from spellchecker import SpellChecker

class SpellCheck:
    """Класс для проверки орфографии."""

    def __init__(self, language='en'):
        """Инициализация проверщика орфографии.

        Args:
            language (str): Язык для проверки (по умолчанию 'en').
        """
        self.spell = SpellChecker(language)

    def check_text(self, text):
        """Проверяет текст на наличие ошибок.

        Args:
            text (str): Текст для проверки.

        Returns:
            dict: Словарь с ошибочными словами и их кандидатами на исправление.
        """
        words = text.split()
        misspelled = self.spell.unknown(words)
        corrections = {word: self.spell.candidates(word) for word in misspelled}
        return corrections

    def correct_text(self, text):
        """Исправляет ошибки в тексте.

        Args:
            text (str): Текст для исправления.

        Returns:
            str: Исправленный текст.
        """
        words = text.split()
        corrected_text = []
        for word in words:
            if word in self.spell:
                corrected_text.append(word)
            else:
                corrected_text.append(self.spell.candidates(word).pop() if self.spell.candidates(word) else word)
        return ' '.join(corrected_text)
