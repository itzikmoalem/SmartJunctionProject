
class RoadUser:
    def __init__(self, p, n):
        self._SocialPriority = p
        self._Name = n
        self._Moves = 0

    def setSocialPriority(self, p):
        self._SocialPriority = p

    def setSocialPriority(self):
        return self._SocialPriority

    def move(self):
        self._Moves += 1
        


