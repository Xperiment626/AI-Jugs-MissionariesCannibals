import m_c_b as mcb
import random as r

def execute(mWS = 3, cWS = 3, boatState = 0, mES = 0, cES = 0):
    missionaries = mcb.Missionary(mWS, mES)
    cannibals = mcb.Cannibal(cWS, cES)
    boat = mcb.Boat(boatState)
    
    states = []
    
    initialState = (missionaries.getWestState(), 
                    cannibals.getWestState(), 
                    boat.getLocation(), 
                    missionaries.getEastState(), 
                    cannibals.getEastState())
    
    states.append(initialState)
    
    finalState = (0,0,1,3,3)
    
    while states[-1] != finalState :
        newState = boat.move(r, missionaries, cannibals)
        if newState not in states:
            states.append(newState)
        if len(states) > 13:
            break
    
    return states
    
def main(args):
    """
    Uso:
    python m_c_b_execution.py mWS, cWS, boatLocation, mES, cES
    Parametros:
    mWS: number of missionaries in the west side
    cWS: number of cannibals in the west side
    boatLocation: 0 for west side | 1 for east side
    mES: number of missionaries in the east side
    cES: number of cannibals in the east side
    Ejemplo:
    python m_c_b_execution.py 3 3 0 0 0
    """
    answers = []
    bestAnswer = None
    
    if len(args) == 5:
        
        mWS = int(args[0])
        cWS = int(args[1])
        boatState = int(args[2])
        mES = int(args[3])
        cES = int(args[4])
        
        firstState = (mWS, cWS, boatState, mES, cES)
        
        while True:
            
            answer = execute(mWS, cWS, boatState, mES, cES)
            
            # According to google if you begin with this state (3,3,0,0,0) the best answer for this problem is to have just *13* states taking into account both the first state and the final state.
            # However, I found that it can be only 11 states taking into account both the first state and the final state but to get this answer you have to wait
            # a reasonable amount of time.

            # by default is set to check the best answer in a lenght of 13 states but you can change it to 12 or 11 and also you have to wait the necessary for those answers.

            # If you have a state != to (3,3,0,0,0) the states should be more short.
            
            if len(answer) <= 13:
                answers.append(answer)
            
            if firstState == (3,3,0,0,0):
                if len(answers) == 1:
                    break
            else:
                if len(answers) == 100:
                    break
        
        # Iterating along the list to get the best answer
        bestAnswer = min(answers, key = lambda x: len(x))
        
        print(f"Best answer: {bestAnswer}, tam {len(bestAnswer)}")
        
    else:
        print(main.__doc__)


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])