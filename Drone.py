import math

class Drone():

    def __init__(self, totalBattery):
        self.totalBattery = totalBattery
        self.battery = totalBattery
        self.currX = 0
        self.currY = 0
        self.travelList = []

    def getBattery(self):
        return self.battery

    def travelPossible(self, distance):
        if(distance > self.battery):
            return False
        return True
    
    def travelTo(self, point, distance):
        self.currX = point[0]
        self.currY = point[1]
        self.battery -= distance
        self.travelList.append(point)

    def distanceTo(self, pointTo):
        if(pointTo[0] == self.currX and pointTo[1] == self.currY):
            return 0
        return math.sqrt((pointTo[0] - self.currX)**2 + (pointTo[1] - self.currY)**2)