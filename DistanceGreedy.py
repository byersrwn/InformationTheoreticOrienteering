from Algorithm import Algorithm

class DistanceGreedy(Algorithm):

    def __init__(self):
        super().__init__()
        pass


    def planRoute(self, points, drone): #maximize information gain vs distance [x,y,prob,entropy,entropyDistRatio]
        for point in points:
            point.append(0) #add another slot for each point to store the ratio of entropy to distance
            point.append(0) #add another slot for each point to store the distance entropy ratio
            point[3] = self.entropy(point[2]) #replace with bits of entropy gain
        informationGain = 0
        while(True):
            for point in points:
                dist = drone.distanceTo(point)
                if(dist == 0):
                    continue
                entropyDistRatio = point[3] / dist #replace last value with bits of entropy gain
                point[4] = entropyDistRatio
            points.sort(key=lambda x: x[4], reverse=True)
            dist = drone.distanceTo(points[0])
            if(drone.travelPossible(dist)):
                drone.travelTo(points[0], dist)
                informationGain += points[0][3]
                points.remove(points[0])
                if len(points) == 0:
                    break
            else:#drone out of energy
                break
        return informationGain
