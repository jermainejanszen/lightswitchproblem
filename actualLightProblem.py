from random import seed
from random import randint

NUMBER_OF_PEOPLE = 10
NUMBER_OF_SIMULATIONS = 100000

class RegularPerson:
    isCounting = False
    hasEnteredRoom = False
    def enterRoom(self, room):
        if self.hasEnteredRoom:
            return
        else:
            if room.lightIsOn:
                return
            else:
                self.hasEnteredRoom = True
                room.switchLight()
                return

class CountingPerson:
    count = 0
    isCounting = True
    def enterRoom(self, room):
        if room.lightIsOn:
            self.count = self.count + 1
            room.switchLight()
            return
        else:
            return

class Room:
    lightIsOn = False
    def switchLight(self):
        if self.lightIsOn:
            self.lightIsOn = False
            return
        else:
            self.lightIsOn = True
            return

results = {"lived" : 0,
           "died" : 0}

for i in range(NUMBER_OF_SIMULATIONS):
    room = Room()
    listOfPeople = []
    listOfPeople.append(CountingPerson())
    for i in range(NUMBER_OF_PEOPLE - 1):
        listOfPeople.append(RegularPerson())
    peopleWhoEntered = {}
    while True:
        chosenPerson = randint(0,NUMBER_OF_PEOPLE - 1)
        if chosenPerson in peopleWhoEntered:
            peopleWhoEntered[chosenPerson] = peopleWhoEntered[chosenPerson] + 1
        else:
            peopleWhoEntered[chosenPerson] = 1
        listOfPeople[chosenPerson].enterRoom(room)
        if listOfPeople[chosenPerson].isCounting:
            if listOfPeople[chosenPerson].count >= NUMBER_OF_PEOPLE - 1:
                break
    if len(peopleWhoEntered) != NUMBER_OF_PEOPLE:
        results["died"] = results["died"] + 1
    else:
        results["lived"] = results["lived"] + 1

print(results)

