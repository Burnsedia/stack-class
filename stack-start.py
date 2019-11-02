

class stack(object):
    def __init__(self):
        self.item = []
        
    
    def push(self, item):
        self.item.append(item)
    

    def pop(self, item):
        return self.item.pop(item)
    
    def get_stack(self):
        return self.item
