from random import randint
from Lane import Lane


class Junction:
    def __init__(self, jtype, jname):
        self._name = jname
        self._type = jtype
        self._numberOfLanes = randint(3, 4)
        self._lanesList = []
        self._lanesList.append("A")
        print("Junction " + jname + " (" + jtype + ") " + "has created, Number of lanes:" + str(self._numberOfLanes))


