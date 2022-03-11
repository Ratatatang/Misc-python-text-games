from HungerClasses import *
from math import *

dayCounter = 0
time = 0
started = False
tributes = []
tributeIntroduction = "Tribute {}\n Name: {}\n Personality: {}\n Class: {}"

tributeNumber = input('Enter the number of tributes: ')
tributeNumber = int(tributeNumber)

validPersonalities = ['mad', 'scared', 'friendly']
validClasses = ['brawler', 'scout', 'archer', 'tank']

for i in range(tributeNumber):
    print('')
    tributeName = input('Enter tribute name: ')
    print('')

    print('(Valid Types: Mad, Scared, Friendly)')
    tributePersonality = input('Enter tribute personality: ')
    print('')

    if(tributePersonality.lower() not in validPersonalities):
       print('Invalid Personality')
       tributePersonality = input('Enter tribute personality: ')
       print('')

    print('(Valid Types: Brawler, Scout, Archer, Tank)')
    tributeClass = input('Enter tribute class: ')

    if(tributeClass.lower() not in validClasses):
       print('Invalid Class')
       tributeClass = input('Enter tribute class: ')
       print('')

    if(tributeClass.lower() == 'brawler'):
        tributeRPClass = 4
    elif(tributeClass.lower() == 'scout'):
        tributeRPClass = 2
    elif(tributeClass.lower() == 'archer'):
        tributeRPClass = 1
    elif(tributeClass.lower() == 'tank'):
        tributeRPClass = 3
    tributes.append(Tribute(tributeName, tributePersonality, tributeClass, i, tributeRPClass))
    tributes[i].statIncrease(tributeClass, 4)

print('')

for i in range(tributeNumber):
    print(tributeIntroduction.format(tributes[i].Number, tributes[i].Name, tributes[i].Personality, tributes[i].DisplayClass))
    print('')

while started == False:
    tempInput = input('Press enter to begin, or enter a number to redo a tribute of that number (redo not working yet))')
    print('')
    """
    if(tempInput != ''):
        if(range(tributeNumber) >= tempInput):
            variableRedo = input('Type a variable name to redo (Excluding Number)')
            print('')

            if(variableRedo.lower() == 'name'):
                tributeName = input('Enter tribute name: ')
                print('')

            elif(variableRedo.lower() == 'personality'):
                print('(Valid Types: Mad, Scared, Friendly)')
                tributePersonality = input('Enter tribute personality: ')
                print('')

                if(tributePersonality.lower() not in validPersonalities):
                    print('Invalid Personality')
                    tributePersonality = input('Enter tribute personality: ')
                    print('')

            elif(variableRedo.lower() == 'class'):
                print('(Valid Types: Brawler, Scout, Archer, Tank)')
                tributeClass = input('Enter tribute class: ')

                if(tributeClass.lower() not in validClasses):
                    print('Invalid Class')
                    tributeClass = input('Enter tribute class: ')
                    print('')

        else:
            print('No tribute of that number')
            print('')
            continue
    else:
        started = True

        """

    if(tempInput == 'devMode'):
        for i in range(tributeNumber):
            print(tributes[i].Name)
            print('')
            print('Aim')
            print(tributes[i].Aim)
            print('Attack')
            print(tributes[i].Attack)
            print('Max Health')
            print(tributes[i].MaxHealth)
            print('Perception')
            print(tributes[i].Perception)
            print('Current Health')
            print(tributes[i].CurrentHealth)
    elif(tempInput != ''):
        continue
    else:
        started = True
        break

def doDayCycle():
    dayCounter += 1
    print("Day" + dayCounter)
    activeTributes = tributes