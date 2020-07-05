import random
from matplotlib import pyplot as plt

iterations = 1000 #num rounds of roulette to play
wallet = 1000 #wallet start amount
baseBet = 10 #base amount to return to. (zeroes the bet amount to this)

graphX = []#iterations (time)
graphY = []#wallet balance

bkSequence = [baseBet]#first term is baseBet
# - - -
def roulette():
    r = random.randint(0,1) #red is true, black is false
    if (r):
        return True
    else: return False

def printStats():
    global iterations, baseBet, bkSequence
    seqSum = 0
    def nthTerm(n):#compute nth term of the geometric sequence
        return bkSequence[0] * (2**(n-1))#ratio = 2
    def sumSequence():
        return bkSequence[0] * ((1-(2**(len(bkSequence)-1)))/(1-2))

    while seqSum < wallet:
        bkSequence.append(nthTerm(len(bkSequence)+1))#compute next term
        seqSum = sumSequence()#compute new sum
    bkSequence.pop()
    bkChance = (1 / 2**len(bkSequence))
    print(f"there is a {bkChance}% probability of going bankrupt per turn")
    print(f"given {iterations} iterations, there is a {bkChance*iterations}% chance of going bankrupt")
    print(f"(you would have to lose {len(bkSequence)} times in a row before not being able to double your bet again)")

def main():
    global iterations, wallet, baseBet, graphX, graphY
    printStats()
    # - - -
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
