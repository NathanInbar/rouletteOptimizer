import random
from matplotlib import pyplot as plt

iterations = 1000 #num rounds of roulette to play
wallet = 10000 #wallet start amount
baseBet = 10 #base amount to return to. (zeroes the bet amount to this)

graphX = []#iterations (time)
graphY = []#wallet balance
# - - -
def roulette():
    r = random.randint(0,1) #red is true, black is false
    if (r):
        return True
    else: return False

def printStats():
    bankruptcy = 0
    print(f"chance of bankruptcy per round:")

def main():
    global iterations, wallet, baseBet, graphX, graphY
    betAmount = baseBet
    betColor = True #start by betting on red
    for x in range(iterations):
        r = roulette()
        if betColor == r:#if we win
            wallet += betAmount
            betAmount = baseBet
            not betColor#bet on opp color
        else: #if we lost
            wallet -= betAmount
            betAmount *= 2

        graphX.append(x)
        graphY.append(wallet)




# - - -
main()
plt.plot(graphX,graphY)
plt.show()
