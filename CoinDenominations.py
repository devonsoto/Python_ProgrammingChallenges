#Devon Soto
#THis scripts uses a greedy algorithm that I coded which gives you the change of n cents


#Where cents is the cents to give change for
#Where coin_values is the list of coin denomiations
def wizardChange(cents,coin_values):
    n = cents
    total_cents = 0
    histogram = coin_values
    values = [0 for i in range(len(coin_values))]   #make list of 0 .. len(coin_values)
    total_coins = 0
    k = 0

    if(cents == 0):
        print("Nothing to make change for.")

    while( cents > 0):  #keep looping until n cents has change
        coin = 0

        while( coin_values[k] <= cents):    #loop throught the coin values
            cents = cents - coin_values[k]  #changing value of cents
            total_cents += coin_values[k]   #keeping change of the total amount of cents
            total_coins+=1                  #Number of coins used
            values[k] = values[k] + 1       #Number of specific coin used


        #check to se if n = 0. There was a solution
        if cents == 0:
            print("A solutioin has been calculated.")
            histogram = list(zip(histogram, values))    #pair specific coins and number of times used
            print("Coin value and number of each coin used: {}".format(histogram))
            print("{} out of {} cents acquired with the coin denomiation given.".format(total_cents,n))
            break

        elif(coin_values[-1] > cents):
            print("No solution has been calculated.")
            histogram = list(zip(histogram, values))
            print("Coin value and number of each coin used: {}".format(histogram))
            print("{} out of {} cents acquired with the coin denomiation given.".format(total_cents,n))
            break

        else:
            k = k + 1

    return "Error in Calculations"




#Test case 1: Number with a solution
n1 = 100
v1 = [70, 28, 8, 2, 1]

#Test case 2: Number with no solution
n2 = 89
v2 = [70, 28, 8, 2]

#Test case 3: No number with solution
n3 = 0
v3 = [100, 28, 8, 1]

#Test case 4: I can't think of another case so yea
n4 = 21
v4 = [100, 28, 8, 1]

#test case 1
print("With {} cents and coin denomiation of {}".format(n1,v1))
wizardChange(n1,v1)
print()

#test case 2
print("With {} cents and coin denomiation of {}".format(n2,v2))
wizardChange(n2,v2)
print()

#test case 3
print("With {} cents and coin denomiation of {}".format(n3,v3))
wizardChange(n3,v3)
print()

#test case 4
print("With {} cents and coin denomiation of {}".format(n4,v4))
wizardChange(n4,v4)
print()
