from Algorithm import Algorithm
from Drone import Drone
import copy

class NaiveGreedy(Algorithm):

    def __init__(self):
        super().__init__()
        pass

    def planRoute(self, points, drone): #maximize information gain
        informationGain = 0
        copiedPoints = copy.deepcopy(points)
        for i in range(len(copiedPoints)):
            copiedPoints[i][2] = self.entropy(copiedPoints[i][2]) #replace with bits of entropy gain
        copiedPoints.sort(key=lambda x: x[2], reverse=True)
        dist = drone.distanceTo(copiedPoints[0])
        while(drone.travelPossible(dist)):
            drone.travelTo(copiedPoints[0], dist)
            informationGain += copiedPoints[0][2]
            copiedPoints.remove(copiedPoints[0])
            if len(copiedPoints) == 0:
                break
            dist = drone.distanceTo(copiedPoints[0])
        return informationGain

        
    