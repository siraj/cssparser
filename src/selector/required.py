from selector.readonly import ReadOnly
class Required(ReadOnly):
    def __init__(self,element,r='r'):
        super().__init__(element,r)
        self.attr = 'required'
 
    def match(self,node):
        return super().match(node)
       
