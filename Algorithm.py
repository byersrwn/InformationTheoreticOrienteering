import math
class Algorithm:

    def __init__(self):
        pass

    def entropy(self, probability):
        return self.shanonEntropyTwoOutcome(probability)

    def shanonEntropyTwoOutcome(self, probability):
        return -1*((probability * math.log2(probability) + (1 - probability) * math.log2(1 - probability)))
    
    def totalEntropy(self, points):
        sumOfEntropy = 0
        for point in points:
            if point[2] != 0:
                sumOfEntropy += self.shanonEntropyTwoOutcome(point[2])

        return sumOfEntropy 
