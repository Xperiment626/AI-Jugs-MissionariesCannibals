class Jug:
    def __init__(self, capacity, state = 0):
        self.capacity = capacity
        self.state = state
        
    def setState(self, state):
        self.state = state
    
    def getCapacity(self):
        return self.capacity
    
    def getState(self):
        return self.state
    
    def empty(self):
        self.state = 0  
      
    def pour(self, jug):
        if jug.getState() == 0:
            if self.getState() <= jug.getCapacity():
                jug.fill(self.getState())
                self.empty()
            else:
                jug.fill(jug.getCapacity())
                self.fill(self.getState() - jug.getCapacity())
        else:
            if jug.getState() < jug.getCapacity():
                if (self.getState() + jug.getState()) <= jug.getCapacity():
                    jug.fill(self.getState() + jug.getState())
                    self.empty()
                else:
                    permitted = (jug.getCapacity() - jug.getState())
                    leftOver = abs(self.getState() - permitted)
                    jug.fill(jug.getState() + permitted)
                    self.setState(leftOver)
    
    def fill(self, content = None):
        if content is not None:
            self.setState(content)
        else:
            self.setState(self.getCapacity())
            
    def action(self, r, jug):
        action = r.randint(0, 2)
        if action == 1:
            if self.getState() == self.getCapacity():
                self.empty()
        elif action == 0:
            self.pour(jug)
        elif action == 2:
            if self.getState() < self.getCapacity():
                self.fill()