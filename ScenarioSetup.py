import yaml
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

class ScenarioSetup:

    def __init__(self, scenario_file):
        self.scenario_file = scenario_file

    def read_scenario(self): #return matplot object, points, industrialCenters, 
        industrialImageCoordinates = []
        with open(self.scenario_file, 'r') as stream:
            image = mpimg.imread("Industrial_Icon.png")
            try:
                data = yaml.safe_load(stream)
                numIndustrial = data["numIndustrial"]
                maxX = data["maxX"]
                maxY = data["maxY"]
                plt.xlim(0, maxX)
                plt.ylim(0, maxY)
                industrialCenters = data.get('industrialData', [])
                for center in industrialCenters:
                    x = center.get('industrialX', None)
                    y = center.get('industrialY', None)
                    plt.imshow(image, extent=(x, x+10, y, y+10))
                    industrialImageCoordinates.append([x, y])
                #parse points
                points = data.get('points', [])
                retPoints = []
                for point in points:
                    x = point.get('x', None)
                    y = point.get('y', None)
                    prob = point.get('probability', None)
                    retPoints.append([x, y, prob])
                    plt.plot(x, y, 'ro')
                return plt, retPoints
            except yaml.YAMLError as exc:
                print(exc)
        pass
    
