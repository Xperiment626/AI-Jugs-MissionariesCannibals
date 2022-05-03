# self.uploadPeople(r, m, c)
        action = r.randint(0,1)
        print(action, self.mLoad, self.cLoad, self.load)
        
        if action:
            self.uploadPeople(r, m, c)
            
            if self.getLoad() > 0:
                if self.getLocation():
                    self.setLocation(0)
                else:
                    self.setLocation(1)
                    
            newState = (m.getWestState(),
                        c.getWestState(),
                        self.getLocation(),
                        m.getEastState(),
                        c.getEastState())

            if newState not in states:
                states.append(newState)
        else:
            self.downloadPeople(r, m, c)
            
            if self.getLoad() > 0:
                if self.getLocation():
                    self.setLocation(0)
                else:
                    self.setLocation(1)
                    
            newState = (m.getWestState(),
                        c.getWestState(),
                        self.getLocation(),
                        m.getEastState(),
                        c.getEastState())

            if newState not in states:
                states.append(newState)
        
        print(states)







-------------------------------------------------------------------------------

def uploadPeople(self, people):
        if self.getLocation():
            if people.getEastState() > 0:
                if type(people) == Missionary:
                    people.changeEastState(abs(people.getEastState() - people.getLoadEast()))
                    self.state[0] += people.getLoadEast()
                else:
                    people.changeEastState(abs(people.getEastState() - people.getLoadEast()))
                    self.state[1] += people.getLoadEast() + self.getState()[1]
        else:
            if people.getWestState() > 0:
                if type(people) == Missionary:
                    people.changeWestState(abs(people.getWestState() - people.getLoadWest()))
                    self.state[0] += people.getLoadWest()
                else:
                    people.changeWestState(abs(people.getWestState() - people.getLoadWest()))
                    self.state[1] += people.getLoadWest()
        
    def downloadPeople(self, people):
        if self.getLocation():
            if type(people) == Missionary:
                if people.getDownloadEast() > 0 and people.getLoadWest() > 0:
                    people.changeEastState(people.getEastState() + people.getDownloadEast())
                    people.setLoadEast(abs(people.getLoadWest() - people.getDownloadEast()))
                    people.setDownloadEast(0)
                    self.state[0] = people.getLoadEast()
            else:
                if people.getDownloadEast() > 0 and people.getLoadWest() > 0:
                    people.changeEastState(people.getEastState() + people.getDownloadEast())
                    people.setLoadEast(abs(people.getLoadWest() - people.getDownloadEast()))
                    people.setDownloadEast(0)
                    self.state[1] = people.getLoadEast()
        else:
            if type(people) == Missionary:
                if people.getDownloadWest() > 0 and people.getLoadEast() > 0:
                    people.changeWestState(people.getWestState() + people.getDownloadWest())
                    people.setLoadWest(abs(people.getLoadEast() - people.getDownloadWest()))
                    people.setDownloadWest(0)
                    self.state[0] = people.getLoadWest()
            else:
                if people.getDownloadWest() > 0 and people.getLoadEast() > 0:
                    people.changeWestState(people.getWestState() + people.getDownloadWest())
                    people.setLoadWest(abs(people.getLoadEast() - people.getDownloadWest()))
                    people.setDownloadWest(0)
                    self.state[1] = people.getLoadWest()
        
    def validateUploadMove(self, r, missionaries, cannibals):
        if self.getLocation():
            mES = missionaries.getEastState()
            cES = cannibals.getEastState()
            mLoad = r.randint(0, mES)
            cLoad = r.randint(0, cES)
            
            auxmload = abs(mES - mLoad)
            auxcload = abs(cES - cLoad)
            
            if ((mES > 0 or cES > 0) 
                # and (auxmload >= 0 or auxcload >= 0) 
                and (auxmload >= auxcload or (auxmload == 0 and auxcload > 0)) 
                and (((mLoad + self.getState()[0]) + (cLoad + self.getState()[1])) <= 2 
                and (mLoad + cLoad) > 0) 
                and (self.getState()[0] + self.getState()[1]) < 2):
                
                missionaries.setLoadEast(mLoad)
                cannibals.setLoadEast(cLoad)
                print(f"CARGA {self.state}")
                missionaries.getOn(self)
                cannibals.getOn(self)
                self.setLocation(0)
                print(f"CARGA {self.state}")
        else:
            mWS = missionaries.getWestState()
            cWS = cannibals.getWestState()
            mLoad = r.randint(0, mWS)
            cLoad = r.randint(0, cWS)
            
            auxmload = abs(mWS - mLoad)
            auxcload = abs(cWS - cLoad)
            
            if ((mWS > 0 or cWS > 0)
                and (auxmload > 0 or auxcload > 0) 
                and (auxmload >= auxcload or (auxmload == 0 and auxcload > 0)) 
                and (((mLoad + self.getState()[0]) + (cLoad + self.getState()[1])) <= 2 
                and (mLoad + cLoad) > 0) 
                and (self.getState()[0] + self.getState()[1]) < 2):
                
                missionaries.setLoadWest(mLoad)
                cannibals.setLoadWest(cLoad)
                print(f"CARGA {self.state}")
                missionaries.getOn(self)
                cannibals.getOn(self)
                self.setLocation(1)
                print(f"CARGA {self.state}")
    
    def validateDownloadMove(self, r, missionaries, cannibals):
        if self.getState()[0] > 0 or self.getState()[1] > 0:
            if self.getLocation():
                print("DOWNLOAD EAST")
                mES = missionaries.getEastState()
                cES = cannibals.getEastState()
                mDownload = r.randint(0, self.getState()[0])
                cDownload = r.randint(0, self.getState()[1])
                
                auxmdownload = abs(mES + mDownload)
                auxcdownload = abs(cES + cDownload)
                
                if (auxmdownload == 0 and auxcdownload > 0) or auxmdownload >= auxcdownload:
                    missionaries.setDownloadEast(mDownload)
                    cannibals.setDownloadEast(cDownload)
                    print(f"DESCARGA {self.state}")
                    missionaries.getOff(self)
                    cannibals.getOff(self)
                    print(f"DESCARGA {self.state}")
            else:
                print("DOWNLOAD WEST")
                mWS = missionaries.getWestState()
                cWS = cannibals.getWestState()
                mDownload = r.randint(0, self.getState()[0])
                cDownload = r.randint(0, self.getState()[1])
                    
                auxmdownload = abs(mWS + mDownload)
                auxcdownload = abs(cWS + cDownload)
                            
                if (auxmdownload == 0 and auxcdownload > 0) or auxmdownload >= auxcdownload:
                    missionaries.setDownloadWest(mDownload)
                    cannibals.setDownloadWest(cDownload)
                    print(f"DESCARGA {self.state}")
                    missionaries.getOff(self)
                    cannibals.getOff(self)
                    print(f"DESCARGA {self.state}")
    
    def move(self, r, missionaries, cannibals, states):
        action = r.randint(0,1)
        if self.getLocation():
            if action:   
                self.validateUploadMove(r, missionaries, cannibals)
                newState = (missionaries.getWestState(),
                            cannibals.getWestState(),
                            self.getLocation(),
                            missionaries.getEastState(),
                            cannibals.getEastState())
                
                if newState not in states:
                    states.append(newState)
                    print(states)
            else:
                self.validateDownloadMove(r, missionaries, cannibals)
                newState = (missionaries.getWestState(),
                            cannibals.getWestState(),
                            self.getLocation(),
                            missionaries.getEastState(),
                            cannibals.getEastState())
                
                if newState not in states:
                    states.append(newState)
                    print(states)
        else:
            if action:
                self.validateUploadMove(r, missionaries, cannibals)
                newState = (missionaries.getWestState(),
                            cannibals.getWestState(),
                            self.getLocation(),
                            missionaries.getEastState(),
                            cannibals.getEastState())
                
                if newState not in states:
                    states.append(newState)
                    print(states)
            else:
                self.validateDownloadMove(r, missionaries, cannibals)
                newState = (missionaries.getWestState(),
                            cannibals.getWestState(),
                            self.getLocation(),
                            missionaries.getEastState(),
                            cannibals.getEastState())
                
                if newState not in states:
                    states.append(newState)
                    print(states)
                    
                    
----------------------------------------------------------------------------------------------          
                    
                    
if self.validMove(m, c, mEastLoad, cEastLoad):
                print("UPLOAD")
                print(mEastLoad, cEastLoad, validmLoad, validcLoad, self.loadlist)
                m.setEastState(abs(m.getEastState() - mEastLoad))
                c.setEastState(abs(c.getEastState() - cEastLoad))
                self.state += validSum
                if self.loadlist[0] > 0:
                    self.loadlist[0] += mEastLoad
                else:
                    self.loadlist[0] = mEastLoad
                
                if self.loadlist[1] > 0:
                    self.loadlist[1] += cEastLoad
                else:
                    self.loadlist[1] = cEastLoad
                # self.setLocation(1)
        else:
            mWestLoad = r.randint(0, m.getWestState())
            cWestLoad = r.randint(0, c.getWestState())
            
            validmLoad = m.getWestState() - mWestLoad
            validcLoad = c.getWestState() - cWestLoad
            
            validSum = mWestLoad + cWestLoad + self.state
            
            if ((validmLoad >= validcLoad or validmLoad == 0) 
                and (m.getWestState() > 0 or c.getWestState() > 0)):
                if validSum > 0 and validSum <= 2:
                    print("UPLOAD")
                    print(mWestLoad, cWestLoad, validmLoad, validcLoad, self.loadlist)
                    m.setWestState(abs(m.getWestState() - mWestLoad))
                    c.setWestState(abs(c.getWestState() - cWestLoad))
                    self.state += validSum
                    if self.loadlist[0] > 0:
                        self.loadlist[0] += mWestLoad
                    else:
                        self.loadlist[0] = mWestLoad
                    
                    if self.loadlist[1] > 0:
                        self.loadlist[1] += cWestLoad
                    else:
                        self.loadlist[1] = cWestLoad
                    # self.setLocation(1)