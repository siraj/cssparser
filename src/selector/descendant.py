
class Descendant:
    """E F	Matches any F element that is a descendant of an E element."""
    def __init__(self,parent,child):
        self.parent = parent
        self.child = child
    def match(self, node):
        self.node = node
        while self.node.parentNode.nodeName!='#document':
              if self.node.parentNode.nodeName == self.parent:
                 return True
              self.node = self.node.parentNode
        return False
        
