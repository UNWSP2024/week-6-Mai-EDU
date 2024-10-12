#Programmer: Mai Lillie
#Date: 10/11/24
# Program #1: Random Dice
import random

#Creating the function
def randDice():
    #Create two random numbers and add
    d1 = random.randint(1,6)
    d2 = random.randint(1,6)
    d_sum = d1 + d2
    #return sum
    return d_sum

#Main function to make it run
def main():
    total = 0
    # Creating the loop
    for x in range(0,100):
        d_sum = randDice()
        total += d_sum
    average = total / 100
    print(f"The average of these dice rolls is {average:.2f}.")

#Runs the code
main()
