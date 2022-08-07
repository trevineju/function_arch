class FunctionNode:
    filepath = ''
    name = ''
    args = []
    returns = []
    body = ''
    calls = set()
    calledby = set()    

    def __init__(self):
        '''(None) -> None
        '''
 
    def addCall(self, text):
        if text != '': self.calls.add(text)

    def addCalled(self, text):
        self.calledby.add(text)
