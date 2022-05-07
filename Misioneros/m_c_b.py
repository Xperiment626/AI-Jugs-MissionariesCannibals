class Missionary:
    def __init__(self, westState = 3, eastState = 0):
        self.westState = westState # west side of the river state for missionaries
        self.eastState = eastState # east side of the river state for missionaries
        
    # Gets & Sets
    def getWestState(self):
        return self.westState
    
    def getEastState(self):
        return self.eastState
    
    def setWestState(self, newState):
        self.westState = newState
        
    def setEastState(self, newState):
        self.eastState = newState
        
    # Returns a random integer between the parameters. This int means the number of missionaries that are going to be upload to the boat
    def getOn(self, r, loc):
        if loc:
            if self.getEastState() > 0:
                return r.randint(0, self.getEastState())
        else:
            if self.getWestState() > 0:
                return r.randint(0, self.getWestState())
        return 0
        
    # Returns a random integer between the parameters. This int means the number of missionaries that are going to be download to the boat.
    def getOff(self, r, bcs):
        return r.randint(r.randint(0,1), bcs) if bcs > 0 else 0 
class Cannibal:
    def __init__(self, westState = 3, eastState = 0):
        self.westState = westState # west side of the river state for missionaries
        self.eastState = eastState # east side of the river state for missionaries
        
    # Gets & Sets
    def getWestState(self):
        return self.westState
    
    def getEastState(self):
        return self.eastState
    
    def setWestState(self, newState):
        self.westState = newState
        
    def setEastState(self, newState):
        self.eastState = newState
        
    # Returns a random integer between the parameters. This int means the number of cannibals that are going to be upload to the boat
    def getOn(self, r, loc):
        if loc:
            if self.getEastState() > 0:
                return r.randint(0, self.getEastState())
        else:
            if self.getWestState() > 0:
                return r.randint(0, self.getWestState())
        return 0
        
    # Returns a random integer between the parameters. This int means the number of cannibals that are going to be download to the boat.
    def getOff(self, r, bcs):
        return r.randint(0, bcs) if bcs > 0 else 0
    
class Boat:
    def __init__(self, location = 0):
        self.location = location # 1 for east side, 0 for west side.
        self.load = 0 # Total load, is the sum of mload and cload
        self.mLoad = 0 # number of missionaries loaded
        self.cLoad = 0 # number of cannibals loaded
        
    def getLoad(self):
        return self.load
    
    def getLocation(self):
        return self.location
    
    def setLocation(self, location):
        self.location = location
    
    # This method transport people in the boat to the other side of the river but first check that the correct conditions are set and they are fulfilled.
    def uploadPeople(self, r, m, c):
        # Check if there is space for more load
        if self.getLoad() < 2:
            
            ml = m.getOn(r, self.getLocation())
            cl = c.getOn(r, self.getLocation())
            
            if self.getLocation():
                mges = m.getEastState()
                cges = c.getEastState()

                # Calcs to check if the next state of the boat and the states from cannibals and missionaries in this side of the river is correct.
                auxmes = mges - ml
                auxces = cges - cl
                validSum = (ml + self.mLoad) + (cl + self.cLoad)
                
                # If true we modify current state
                if ((validSum > 0 and validSum <= 2) and (ml > 0 or cl > 0) and
                    ((auxmes >= auxces or (auxmes == 0 and auxces >= 0)) or
                    (auxmes >= auxces and auxmes >= 0 and auxces >= 0))):
                    self.mLoad += ml
                    self.cLoad += cl
                    self.load = self.mLoad + self.cLoad
                    m.setEastState(auxmes)
                    c.setEastState(auxces)

                # If the current load is greater that 0 then the boat can move.
                if self.getLoad() > 0:
                    self.setLocation(0)
            else:
                
                mgws = m.getWestState()
                cgws = c.getWestState()

                # Calcs to check if the next state of the boat and the states from cannibals and missionaries in this side of the river is correct.
                auxmws = mgws - ml
                auxcws = cgws - cl
                validSum = (ml + self.mLoad) + (cl + self.cLoad)

                # If true we modify current state
                if ((validSum > 0 and validSum <= 2) and (ml > 0 or cl > 0) and
                    ((auxmws >= auxcws or (auxmws == 0 and auxcws >= 0)) or
                    (auxmws >= auxcws and auxmws >= 0 and auxcws >= 0))):
                    self.mLoad += ml
                    self.cLoad += cl
                    self.load = self.mLoad + self.cLoad
                    m.setWestState(auxmws)
                    c.setWestState(auxcws)
                
                # If the current load is greater that 0 then the boat can move.
                if self.getLoad() > 0:
                    self.setLocation(1)
                    
    def downloadPeople(self, r, m, c):
        # Check if there is almost 1 person loaded to the boat in oder to perform a download action.
        if self.getLoad() > 0:
            
            md = m.getOff(r, self.mLoad)
            cd = c.getOff(r, self.cLoad)
            
            if self.getLocation():
                
                mges = m.getEastState()
                cges = c.getEastState()

                # Calcs to check if the next state of the boat and the states from cannibals and missionaries in this side of the river is correct.
                auxmes = mges + md
                auxces = cges + cd
                validSum = (self.mLoad - md) + (self.cLoad - cd)
                
                # If true we modify current state
                if ((validSum >= 0 and validSum <= 2) and (md > 0 or cd > 0) and
                    (auxmes >= auxces or (auxmes == 0 and cd > 0))):
                    self.mLoad -= md
                    self.cLoad -= cd
                    self.load = self.mLoad + self.cLoad
                    m.setEastState(auxmes)
                    c.setEastState(auxces)

                # If the current load is greater that 0 then the boat can move.
                if self.getLoad() > 0:
                    self.setLocation(0)
            else:
                
                mgws = m.getWestState()
                cgws = c.getWestState()

                # Calcs to check if the next state of the boat and the states from cannibals and missionaries in this side of the river is correct.
                auxmws = mgws + md
                auxcws = cgws + cd
                validSum = (self.mLoad - md) + (self.cLoad - cd)
                
                # If true we modify current state
                if ((validSum >= 0 and validSum <= 2) and (md > 0 or cd > 0) and
                    (auxmws >= auxcws or (auxmws == 0 and cd > 0))):
                    self.mLoad -= md
                    self.cLoad -= cd
                    self.load = self.mLoad + self.cLoad
                    m.setWestState(auxmws)
                    c.setWestState(auxcws)
                
                # If the current load is greater that 0 then the boat can move.
                if self.getLoad() > 0:
                    self.setLocation(1)
            
    def move(self, r, m, c):
        action = r.randint(0,1)

        if action:
            self.uploadPeople(r, m, c)
        else:
            self.downloadPeople(r, m, c)

        # Returning the current state of everything after modified it 
        return (m.getWestState(),
                c.getWestState(),
                self.getLocation(),
                m.getEastState(),
                c.getEastState())