from random import seed
from random import randint

NUMBER_OF_PEOPLE = 10
NUMBER_TO_COUNT_TO = NUMBER_OF_PEOPLE
NUMBER_OF_SIMULATIONS = 10

class Person:
    count = 0
    isCounting = False
    def __init__(self, isCounting):
        self.isCounting = isCounting
    
    def enterRoom(self):
        if self.isCounting:
            self.count = self.count + 1

class Room:
    lightIsOn = False
    def switchLight(self):
        if self.lightIsOn:
            self.lightIsOn = False
        else:
            self.lightIsOn = True

room = Room()

results = {"lived" : 0,
           "died" : 0}

for i in range(NUMBER_OF_SIMULATIONS):
    listOfPeople = []
    listOfPeople.append(Person(True))
    for i in range(NUMBER_OF_PEOPLE - 1):
        listOfPeople.append(Person(False))
    peopleWhoEntered = {}
    while True:
        chosenPerson = randint(0,NUMBER_OF_PEOPLE - 1)
        if chosenPerson in peopleWhoEntered:
            peopleWhoEntered[chosenPerson] = peopleWhoEntered[chosenPerson] + 1
        else:
            peopleWhoEntered[chosenPerson] = 1
        listOfPeople[chosenPerson].enterRoom()
        if listOfPeople[chosenPerson].count >= NUMBER_TO_COUNT_TO:
            break
    if len(peopleWhoEntered) != NUMBER_OF_PEOPLE:
        results["died"] = results["died"] + 1
    else:
        results["lived"] = results["lived"] + 1

print(results)

