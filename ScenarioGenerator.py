import yaml
import random

class ScenarioGenerator:

    def __init__ (self):
        print("ScenarioSetup object created")
        pass

    def generate_scenario(self, maxX, maxY, numIndustrial, industrialXs, industrialYs, numPOIs):

        industrialPoints = []
        for i in range(numIndustrial):
            searchingForNewIndistrial = True
            while(searchingForNewIndistrial):
                x = random.randint(0, maxX - 20)
                y = random.randint(0, maxY - 20)
                correctPlacement = True
                for points in industrialPoints:
                    if x <= (points[0]["industrialX"] + 10) and x >= (points[0] - 10) and y <= (points[1] + 10) and y >= (points[1] - 10): #this bound is going to be inside of another industrial icon
                        correctPlacement = False
                if(correctPlacement):
                    searchingForNewIndistrial = False
                    newIndustrialPoint = {"ID": i + 1, "industrialX": x, "industrialY": y}
                    industrialPoints.append(newIndustrialPoint)
        print(industrialPoints)

        # industrial_data = [
#         {"ID": i + 1, "industrialX": random.randint(0, maxX), "industrialY": random.randint(0, maxY)}
#         for i in range(numIndustrial)
#     ]

# # Generate points dynamically
#         points = [
#             {"ID": i + 1, "x": random.randint(0, max_x), "y": random.randint(0, max_y), "probability": round(random.uniform(0, 1), 2)}
#             for i in range(num_points)
#         ]
#         data = {
#             "maxX:": maxX,
#             "maxY:": maxY,
#             "numIndustrial:": numIndustrial,
#             "industrialData:": [],
#             "numPOIs:": numPOIs
#         }
      

        #   randPoints = []
        # for i in range(numPOIs):
        #     while(True):
        #         newRandPoint = [random.randint(0, maxX), random.randint(0, maxY), random.uniform(0, 1)]
        #         for randPoint in randPoints:
        #             if(newRandPoint[0] == randPoint[0] and newRandPoint[1] == randPoint[1]):
                        
        #     randPoints.append([random.randint(0, maxX), random.randint(0, maxY), random.uniform(0, 1)])
        
         