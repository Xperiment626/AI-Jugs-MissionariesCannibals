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
    
    # print(F"INITIAL STATE: {initialState}")
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
    python m_c_b_execution.py simulations mWS, mES, cWS, cES, boatState
    Parametros:
    simulations: number of simulations
    bigJugCapacity: galons of capacity (number)
    shortJugCapacity: galons of capacity (number)
    big jug initial state: 0
    short jug initial state: 0
    Ejemplo:
    python m_c_b_execution.py 10000 3 3 0 0 0
    """
    answers = []
    bestAnswer = None
    if len(args) == 6:
        simulations = int(args[0])
        mWS = int(args[1])
        cWS = int(args[2])
        boatState = int(args[3])
        mES = int(args[4])
        cES = int(args[5])
        
        # for i in range(simulations):
        while True:
            answer = execute(mWS, cWS, boatState, mES, cES)
            if len(answer) <= 11:
                answers.append(answer)
                break
        
        bestAnswer = min(answers, key = lambda x: len(x))
        
        print(f"Best answer: {bestAnswer}, tam {len(bestAnswer)}")
        
    else:
        print(main.__doc__)


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])