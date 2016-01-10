#class Frob(object):
#    def __init__(self, name):
#        self.name = name
#        self.before = None
#        self.after = None
#    def setBefore(self, before):
#        # example: a.setBefore(b) sets b before a
#        self.before = before
#    def setAfter(self, after):
#        # example: a.setAfter(b) sets b after a
#        self.after = after
#    def getBefore(self):
#        return self.before
#    def getAfter(self):
#        return self.after
#    def myName(self):
#        return self.name
#def insert(atMe,newFrob):
#    if newFrob.myName() < atMe.myName():
#        if atMe.getBefore() == None:
#            atMe.setBefore(newFrob)
#            newFrob.setAfter(atMe)
#        else:
#            if atMe.getBefore().myName() < newFrob.myName():
#                newFrob.setBefore(atMe.getBefore())
#                newFrob.setAfter(atMe)
#                atMe.getBefore().setAfter(newFrob)
#                atMe.setBefore(newFrob)
#            else:
#                insert(atMe.getBefore(),newFrob)
#    elif newFrob.myName() >= atMe.myName():
#        if atMe.getAfter() == None:
#            atMe.setAfter(newFrob)
#            newFrob.setBefore(atMe)
#        else:
#            if atMe.getAfter().myName() > newFrob.myName():
#                newFrob.setAfter(atMe.getAfter())
#                newFrob.setBefore(atMe)
#                atMe.getAfter().setBefore(newFrob)
#                atMe.setAfter(newFrob)
#            else:
#                insert(atMe.getAfter(),newFrob)

def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list 
    """
    # Your Code Here
    #print start.myName()
    if start.getBefore() == None:
        return start
    else:
        return findFront(start.getBefore())
#eric = Frob('eric')
#andrew = Frob('andrew')
#ruth = Frob('ruth')
#fred = Frob('fred')
#martha = Frob('martha')
#
#insert(eric, andrew)
#insert(eric, ruth)
#insert(eric, fred)
#insert(ruth, martha)
#print findFront(ruth).myName()