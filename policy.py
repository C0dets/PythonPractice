import credentials

from interpreter import Interpreter

def initial(status, comm):
    intp = Interpreter(status)

    myTanks = []
    enemyTanks = []

    for player in status['players']:
        if (player['name'] == credentials.username):
            myTanks = player['tanks']
        else:
            enemyTanks += player['tanks']

##    Check if any tank can be attacked
    for myTank in myTanks:
        for enemyTank in enemyTanks:
            if (intp.inRange(myTank['id'], enemyTank['id'])):
                comm.fire(myTank['id'])



##    Check if any tank is in danger, move away  (Do predictive calculations by observing past status and extrapolating?)

##    For each opponenet tank, find own tank that is closest, and assign opponent to own tank and move+rotate agressively





