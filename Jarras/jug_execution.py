import jug as j
import random as r

def execute(bigJugCapacity, shortJugCapacity, initialState = (0,0)):
    states = [initialState]
    jugs = []
    _ = None
    finalState = (2,_)
    jugs.append(j.Jug(bigJugCapacity, initialState[0]))
    jugs.append(j.Jug(shortJugCapacity, initialState[1]))
    
    while states[-1][0] != finalState[0]:
        selectJug = r.randint(0,1)
        if selectJug:
            jugs[1].action(r, jugs[0])
            if (jugs[0].getState(), jugs[1].getState()) not in states:
                states.append((jugs[0].getState(), jugs[1].getState()))
        else:
            jugs[0].action(r, jugs[1])
            if (jugs[0].getState(), jugs[1].getState()) not in states:
                states.append((jugs[0].getState(), jugs[1].getState()))

    # print(f'States: {states}')
    return states
    
def main(args):
    """
    Uso:
    python jug_execution.py simulations bigJugCapacity shortJugCapacity initialState
    Parametros:
    simulations: number of simulations
    bigJugCapacity: galons of capacity (number)
    shortJugCapacity: galons of capacity (number)
    big jug initial state: 0
    short jug initial state: 0
    Ejemplo:
    python jug_execution.py 100 4 3 0 0
    """
    answers = []
    bestAnswer = None
    if len(args) == 5:
        
        simulations = int(args[0])
        bigJugCapacity = int(args[1])
        shortJugCapacity = int(args[2])
        initialState = tuple((int(args[3]), int(args[4])))
        BJlabel = "J" + str(bigJugCapacity)
        SJlabel = "J" + str(shortJugCapacity)
        
        for sims in range(simulations):
            answer = execute(bigJugCapacity, shortJugCapacity, initialState)
            if answer not in answers:
                answers.append(answer)
                
        print(f"Best answer ({BJlabel}, {SJlabel}): {min(answers, key = lambda x: len(x))}")
    else:
        print(main.__doc__)


if __name__ == "__main__":
    import sys
    main(sys.argv[1:])