import language_tool_python

class GrammarChecker:
    def __init__(self):
        self.tool = language_tool_python.LanguageTool('en-US')

    def correct_sentence(self, sentence):
        matches = self.tool.check(sentence)
        return language_tool_python.utils.correct(sentence, matches)

if __name__ == "__main__":
    checker = GrammarChecker()
    print(checker.correct_sentence("She go to scholl yesturday."))
