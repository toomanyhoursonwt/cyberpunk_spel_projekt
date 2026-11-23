import random as rand
def skada(kraft, hälsa):
    kraft = kraft * 1.5
    kraft = kraft + rand.randint(-5, 5)
    hälsa = hälsa - kraft
    return int(hälsa)

def parera(försvar):
    försvar = försvar/25
    if försvar > rand.uniform(0.0, 1.0):
        return True
    else:
        return False
    
def steg():
    stegalternativ = rand.randint (1, 3)
    if stegalternativ == 1:
        trap = skada(rand.randint(10, 15))
        return trap
    if stegalternativ == 2:
        fiende = 


def start_attack(medvetenhet):
    medvetenhet = medvetenhet/30
    if medvetenhet > rand.uniform(0.0, 1.0):
        return True
    else:
        return False