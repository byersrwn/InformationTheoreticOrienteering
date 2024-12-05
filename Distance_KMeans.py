from Algorithm import Algorithm
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


class DistanceKMeans(Algorithm):

    def __init__(self):
        super().__init__()
        pass

    def __init__(self):
        super().__init__()
        pass

    def planRoute(self, points, drone): #maximize information gain by choosing the next k cluster with the highest reward to distance ratio
        newPoints = np.array([[point[0], point[1]] for point in points])
        k = 5

        kmeans = KMeans(n_clusters=k, random_state=126)
        kmeans.fit(newPoints)

        labels = kmeans.labels_
        centroids = kmeans.cluster_centers_ #centroids are in order of cluster number

        for i, point in enumerate(points):
            point.append(labels[i])

        plt.figure(figsize=(8, 6))
        for i in range(k):
            cluster_points = [point for point in points if point[3] == i]
            plt.scatter([point[0] for point in cluster_points],
                        [point[1] for point in cluster_points],
                        label=f'Cluster {i + 1}')
        plt.scatter(centroids[:, 0], centroids[:, 1], s=100, c='black', marker='X', label='Centroids', edgecolors='none', facecolors='black')
        plt.xlabel('X Coordinate')
        plt.ylabel('Y Coordinate')
        image = mpimg.imread("Industrial_Icon.png")
        plt.imshow(image, extent=(30, 40, 30, 40))
        plt.imshow(image, extent=(50, 60, 30, 40))
        plt.imshow(image, extent=(30, 40, 50, 60))
        plt.imshow(image, extent=(50, 60, 50, 60))
        plt.legend()
        plt.grid(True)

        #now get the total amount of reward for each cluster
        cluster_rewards = [] #[reward for cluster, cluster number, reward/dist ratio]

        points.sort(key=lambda x: x[3]) #sort the points by the cluster number
        for point in points:
            print(f"Point({point[0]}, {point[1]}, {point[2]}) - Cluster: {point[3]}") #[x,y,prob,cluster]
        for i in range(k):
            cluster_points = [point for point in points if point[3] == i] #get the points in this cluster
            totalClusterInformation = 0
            for point in cluster_points:
                totalClusterInformation += self.entropy(point[2])
            cluster_rewards.append([totalClusterInformation, i + 1, 0]) #0 is the placeholder for reward/dist ratio
        print("Cluster Rewards: ", cluster_rewards)
        print("Centroids: ", centroids)

        #now pick the next highest cluster based on distance to reward ratio, travel to the centroid, and traverse as many points in order as you can.
        informationGain = 0
        while(len(cluster_rewards) > 0):
            for i in range(len(cluster_rewards)):
                dist = drone.distanceTo(centroids[cluster_rewards[i][1] - 1]) #get distance to centroid of ith cluster
                cluster_rewards[i][2] = (cluster_rewards[i][0] / dist) #place in the last spot of each inner list. inner list now: [reward, cluster number, reward/dist]
            print("Cluster Rewards with Ratios: ", cluster_rewards)
            cluster_rewards.sort(key=lambda x: x[2], reverse=True) #sort by reward/dist ratio
            nextCluster = cluster_rewards[0] # [reward, cluster number] list. Get the best ratio cluster
            nextClusterID = nextCluster[1]
            nextClusterReward = nextCluster[0]
            print("Next Cluster to travel to: ", nextClusterID, " with information reward: ", nextClusterReward)
            clusterCentroid = centroids[nextClusterID - 1] #get the centroid of the next cluster. Should be [x,y]
            print("Next Cluster Centroid: ", clusterCentroid)
            #now travel to the centroid if possible
            dist = drone.distanceTo(clusterCentroid)
            if(drone.travelPossible(dist)): #can get to centroid from curr position
                drone.travelTo(clusterCentroid, dist)
                cluster_points = [point for point in points if point[3] == nextClusterID - 1] #get the points in this cluster
                print("Cluster Points: ", cluster_points)
                while(len(cluster_points) > 0):
                    dist = drone.distanceTo(cluster_points[0])
                    if(drone.travelPossible(dist)):
                        informationGain += self.entropy(cluster_points[0][2])
                        drone.travelTo(cluster_points[0], dist)
                        cluster_points.remove(cluster_points[0])
                    else:
                        return informationGain # out of energy for drone
            cluster_rewards.remove(nextCluster) #this cluster has been fully traversed
        return informationGain #everything has been traversed






    
