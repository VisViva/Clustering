from numpy import vstack,savetxt
from numpy.random import rand
from scipy.cluster.vq import kmeans,vq
from scipy.spatial.distance import euclidean
import matplotlib.pyplot as plt
import random
import time
import sys

# Globals
objectiveFunctionResult = 0
calculatedCentroids = []
colors = []
numOfCentroids = input("> Please enter number of centroids: ")
limit = sys.maxsize
limitvalue = raw_input("> Do you want to define a limit? (y/n): ")
if limitvalue == 'y':
	limit = input("> Please enter a limit: ")

# Initialize colors
for x in range(0, numOfCentroids):
	colors.append('#%02X%02X%02X' % (random.randint(0,255),random.randint(0,255),random.randint(0,255)))

# Create data file
generate = raw_input("> Do you want to generate a data file? (y/n): ")
if generate == 'y':
	size = float(raw_input("> Please enter data file size in megabytes: "))
	savetxt('C:\output.txt', vstack((rand(size * 10000,2),rand(size * 10000,2))))

# Calculate centroids
print("> Now calculating centroids")
centroidTimeStart = time.time()
with open("C:\output.txt", "r") as ins:
	data = []
	i = 0
	for line in ins:
		i = i + 1
		items = line.split()
		data.append([float(items[0]), float(items[1])])
		if limit != sys.maxsize:
			if i == limit - len(calculatedCentroids):
				i = 0
				data = vstack(data)
				centroids,_ = kmeans(data,numOfCentroids)
				idx,_ = vq(data,centroids)
				calculatedCentroids = centroids
				data = []
	if limit == sys.maxsize:
		data = vstack(data)
		centroids,_ = kmeans(data,numOfCentroids)
		idx,_ = vq(data,centroids)
		calculatedCentroids = centroids
		data = []
centroidTimeEnd = time.time()

# Log
print(calculatedCentroids)
print("> Time spent calculating centroids: " + str(centroidTimeEnd - centroidTimeStart))

# Plot from file
print("> Now plotting")
plotTimeStart = time.time()
with open("C:\output.txt", "r") as ins:
	for line in ins:
		items = line.split()
		point = [float(items[0]), float(items[1])]
		a = 0
		distances = []
		for centroid in calculatedCentroids:
			distances.append([point, euclidean(point, calculatedCentroids[a]), colors[a]])
			a = a + 1
		minimalDistance = [0,float('inf'),0]
		for distance in distances:
			if distance[1] < minimalDistance[1]:
				minimalDistance = distance
		plt.plot(minimalDistance[0][0], minimalDistance[0][1], marker = 'o', color = minimalDistance[2])
		objectiveFunctionResult += minimalDistance[1] * minimalDistance[1]
for centroid in calculatedCentroids:
	plt.plot(centroid[0], centroid[1], 'ow', ms=15)
	plt.plot(centroid[0], centroid[1], 'ob', ms=10)

# Log
plotTimeEnd = time.time()
print("> Time spent plotting: " + str(plotTimeEnd - plotTimeStart))
print("> Objective function result: " + str(objectiveFunctionResult))
plt.show()
