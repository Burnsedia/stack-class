

class stack(object):
    def __init__(self):
        self.item = []
        
    
    def push(self, item):
        self.item.append(item)
    

    def pop(self, item):
        self.item.pop(item)