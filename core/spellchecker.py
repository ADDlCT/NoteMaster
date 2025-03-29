from spellchecker import SpellChecker

class SpellCheck:
    def __init__(self, language='en'):
        self.spell = SpellChecker(language)

    def check_text(self, text):
        words = text.split()
        misspelled = self.spell.unknown(words)
        corrections = {word: self.spell.candidates(word) for word in misspelled}
        return corrections

    def correct_text(self, text):
        words = text.split()
        corrected_text = []
        for word in words:
            if word in self.spell:
                corrected_text.append(word)
            else:
                corrected_text.append(self.spell.candidates(word).pop() if self.spell.candidates(word) else word)
        return ' '.join(corrected_text)
