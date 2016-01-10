class WordTrigger(Trigger):
    def __init__(self,word):
        self.word = word.lower()
    def wordList(self,text):
        newText = text
        for char in string.punctuation:
            if char in newText:
                newText = newText.replace(char,' ')
        newText = newText.strip()
        newText = newText.lower()
        return newText.split(' ')
    def isWordIn(self,text):
        words = self.wordList(text)
        if self.word in words:
            return True
        return False
# TODO: TitleTrigger
class TitleTrigger(WordTrigger):
    def evaluate(self, story):
        if self.isWordIn(story.getTitle()):
            return True
        return False
    
# TODO: SubjectTrigger
class SubjectTrigger(WordTrigger):
    def evaluate(self, story):
        if self.isWordIn(story.getSubject()):
            return True
        return False
# TODO: SummaryTrigger
class SummaryTrigger(WordTrigger):
    def evaluate(self, story):
        if self.isWordIn(story.getSummary()):
            return True
        return False