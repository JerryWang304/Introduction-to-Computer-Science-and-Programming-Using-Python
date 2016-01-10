# Enter your code for WordTrigger, TitleTrigger,
# SubjectTrigger, SummaryTrigger, PhraseTrigger, and 
# filterStories in this box
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

# Composite Triggers
# Problems 6-8

# TODO: NotTrigger
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

# Phrase Trigger
# Question 9

# TODO: PhraseTrigger
class PhraseTrigger(Trigger):
    def __init__(self,words):
        self.words = words
    def evaluate(self,story):
        if self.words in story.getSubject() or self.words in story.getTitle() or self.words in story.getSummary():
            return True
        return False
def filterStories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    # TODO: Problem 10
    # This is a placeholder (we're just returning all the stories, with no filtering) 
    ret = []
    for story in stories:
        for tri in triggerlist:
            if tri.evaluate(story):
                if story not in ret:
                    ret.append(story)
                break
    return ret
                