# Enter your code for WordTrigger, TitleTrigger,
# NotTrigger, AndTrigger, and OrTrigger in this box
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
class NotTrigger(Trigger):
    def __init__(self,x):
        self.tri = x
    def evaluate(self,story):
        return not self.tri.evaluate(story)
        
# TODO: AndTrigger
class AndTrigger(Trigger):
    def __init__(self,x,y):
        self.tri1 = x
        self.tri2 = y
    def evaluate(self,story):
        return self.tri1.evaluate(story) and self.tri2.evaluate(story)
# TODO: OrTrigger
class OrTrigger(Trigger):
    def __init__(self,x,y):
        self.tri1 = x
        self.tri2 = y
    def evaluate(self,story):
        return self.tri1.evaluate(story) or self.tri2.evaluate(story)
