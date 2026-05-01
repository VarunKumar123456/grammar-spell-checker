from spellchecker import SpellChecker

class SpellCorrector:
    def __init__(self):
        self.spell = SpellChecker()

    def correct_sentence(self, sentence):
        words = sentence.split()
        corrected_words = [self.spell.correction(word) or word for word in words]
        return " ".join(corrected_words)

if __name__ == "__main__":
    checker = SpellCorrector()
    print(checker.correct_sentence("Ths is a smple txt with erors."))
