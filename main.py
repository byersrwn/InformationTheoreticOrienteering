import matplotlib.pyplot as plt
import sys
import Distance_KMeans, DistanceGreedy, Naive_KMeans, NaiveGreedy, ScenarioSetup, ScenarioGenerator, Drone, Algorithm

def main():
    choice = sys.argv[1]
    scenarioFile = sys.argv[2]
    droneBatteryLife = sys.argv[3]
    algorithm = None
    match choice:
        case 'naive_greedy':
            algorithm = NaiveGreedy.NaiveGreedy() # just picks next distance based off of the largest mutual information gain
        case 'greedy_distance':
            algorithm = DistanceGreedy.DistanceGreedy() # uses reward/dist as the decision metric
        case 'naive_kmeans':
            algorithm = Naive_KMeans.NaiveKMeans() # calculates all reward for each cluster, then travels to the next cluster
        case 'distance_kmeans':
            algorithm = Distance_KMeans.DistanceKMeans() # calculates reward/dist for each cluster, then travels to the next cluster

    drone = Drone.Drone(int(droneBatteryLife))  
    scenarioPlt = ScenarioSetup.ScenarioSetup(scenarioFile)
    plt, points = scenarioPlt.read_scenario()
    totalEntropy = algorithm.totalEntropy(points)
    print("Points: ", points)
    print("Total Entropy: ", totalEntropy)
    informationGain = algorithm.planRoute(points, drone) #put the travelList in the drone object
    print("travelList:", drone.travelList)
    print("-----------------STATS-----------------")
    print("Total points to visit: ", len(drone.travelList))
    print("Total Information Gained: ", informationGain)
    print("Total Information Entropy: ", totalEntropy)
    print("Information Gained Ratio: ", (informationGain / totalEntropy)*100)
    print("Total Energy Remaining: ", drone.battery)
    print("% Remaining Battery: ", (drone.battery / drone.totalBattery) * 100)
    plotPath(drone)

def plotPath(drone):
    x_values = [point[0] for point in drone.travelList]
    y_values = [point[1] for point in drone.travelList]
    x_values.insert(0,0)
    y_values.insert(0,0)
    plt.scatter(x_values, y_values, color='black', label='Points', facecolors='none')
    plt.plot(x_values, y_values, color='blue', linestyle='-', marker='', label='Route', linewidth=1)
    pairs = list(zip(x_values, y_values))
    for i, (x, y) in enumerate(pairs):
        plt.text(x + 0.5, y + 0.5, f'{i}', fontsize=12, color='black')
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title('Route Between Points')  
    plt.grid(True)
    plt.show()  

if __name__ == '__main__':
    main()