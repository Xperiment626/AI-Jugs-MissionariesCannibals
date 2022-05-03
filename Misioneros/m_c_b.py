class Missionary:
    def __init__(self, westState = 3, eastState = 0):
        self.westState = westState
        self.eastState = eastState
        
    def getWestState(self):
        return self.westState
    
    def getEastState(self):
        return self.eastState
    
    def setWestState(self, newState):
        self.westState = newState
        
    def setEastState(self, newState):
        self.eastState = newState
        
    def getOn(self, r, loc):
        if loc:
            if self.getEastState() > 0:
                return r.randint(0, self.getEastState())
        else:
            if self.getWestState() > 0:
                return r.randint(0, self.getWestState())
        return 0
        
    def getOff(self, r, bcs):
        return r.randint(0, bcs) if bcs > 0 else 0
        
class Cannibal:
    def __init__(self, westState = 3, eastState = 0):
        self.westState = westState
        self.eastState = eastState
        
    def getWestState(self):
        return self.westState
    
    def getEastState(self):
        return self.eastState
    
    def setWestState(self, newState):
        self.westState = newState
        
    def setEastState(self, newState):
        self.eastState = newState
        
    def getOn(self, r, loc):
        if loc:
            if self.getEastState() > 0:
                return r.randint(0, self.getEastState())
        else:
            if self.getWestState() > 0:
                return r.randint(0, self.getWestState())
        return 0
        
    def getOff(self, r, bcs):
        return r.randint(0, bcs) if bcs > 0 else 0
    
class Boat:
    def __init__(self, location = 0):
        self.location = location
        self.load = 0
        self.mLoad = 0
        self.cLoad = 0
        
    def getLoad(self):
        return self.load
    
    def getLocation(self):
        return self.location
    
    def setLocation(self, location):
        self.location = location
    
    def uploadPeople(self, r, m, c):
        if self.getLoad() < 2:
            ml = m.getOn(r, self.getLocation())
            cl = c.getOn(r, self.getLocation())
            if self.getLocation():
                mges = m.getEastState()
                cges = c.getEastState()
                auxmes = mges - ml
                auxces = cges - cl
                validSum = (ml + self.mLoad) + (cl + self.cLoad)
                
                if ((validSum > 0 and validSum <= 2) and
                    (((auxmes >= auxces or auxmes == 0) and (auxces >= 0 or auxmes >= 0)) or
                    (auxmes >= auxces and auxmes >= 0 and auxces >= 0))):
                    # print("UPLOAD")
                    self.mLoad += ml
                    self.cLoad += cl
                    self.load = self.mLoad + self.cLoad
                    m.setEastState(auxmes)
                    c.setEastState(auxces)
            else:
                mgws = m.getWestState()
                cgws = c.getWestState()
                auxmws = mgws - ml
                auxcws = cgws - cl
                validSum = (ml + self.mLoad) + (cl + self.cLoad)
                if ((validSum > 0 and validSum <= 2) and
                    (((auxmws >= auxcws or auxmws == 0) and (auxcws >= 0 or auxmws >= 0)) or
                    (auxmws >= auxcws and auxmws >= 0 and auxcws >= 0))):
                    # print("UPLOAD")
                    self.mLoad += ml
                    self.cLoad += cl
                    self.load = self.mLoad + self.cLoad
                    m.setWestState(auxmws)
                    c.setWestState(auxcws)
                    
    def downloadPeople(self, r, m, c):
        if self.getLoad() > 0:
            md = m.getOff(r, self.mLoad)
            cd = c.getOff(r, self.cLoad)
            if self.getLocation():
                mges = m.getEastState()
                cges = c.getEastState()
                auxmes = mges + md
                auxces = cges + cd
                validSum = (self.mLoad - md) + (self.cLoad - cd)
                
                if ((validSum >= 0 and validSum <= 2) and (md > 0 or cd > 0) and
                    ((auxmes >= auxces or auxmes == 0) or
                    (auxmes >= auxces))):
                    # print("DOWNLOAD")
                    # print(md, cd)
                    self.mLoad -= md
                    self.cLoad -= cd
                    self.load = self.mLoad + self.cLoad
                    m.setEastState(auxmes)
                    c.setEastState(auxces)
            else:
                mgws = m.getWestState()
                cgws = c.getWestState()
                auxmws = mgws + md
                auxcws = cgws + cd
                validSum = (self.mLoad - md) + (self.cLoad - cd)
                
                if ((validSum >= 0 and validSum <= 2) and (md > 0 or cd > 0) and
                    ((auxmws >= auxcws or auxmws == 0) or
                    (auxmws >= auxcws))):
                    # print("DOWNLOAD")
                    # print(md, cd)
                    self.mLoad -= md
                    self.cLoad -= cd
                    self.load = self.mLoad + self.cLoad
                    m.setWestState(auxmws)
                    c.setWestState(auxcws)
            
    def move(self, r, m, c):
        # self.uploadPeople(r, m, c)
        action = r.randint(0,1)
        # print(action, self.mLoad, self.cLoad, self.load)
        
        if action:
            self.uploadPeople(r, m, c)
        else:
            self.downloadPeople(r, m, c)
            
        if self.getLoad() > 0:
            if self.getLocation():
                self.setLocation(0)
            else:
                self.setLocation(1)
        
        return (m.getWestState(),
                c.getWestState(),
                self.getLocation(),
                m.getEastState(),
                c.getEastState())