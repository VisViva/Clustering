# Clustering example in python

K-Means clustering example written in python using Scipy and Numpy.
Limit can be defined to invoke RAM - friendly calculations.

Output:

![Output](https://github.com/VisViva/Clustering/blob/master/images/cluster.jpg)

Objective function:

![Output](https://github.com/VisViva/Clustering/blob/master/images/objective_function.png)

![Output](https://github.com/VisViva/Clustering/blob/master/images/x.png) - data point in the cluster j

![Output](https://github.com/VisViva/Clustering/blob/master/images/c.png) - centroid in the cluster j

```
python cluster.py
> Please enter number of centroids: 25
> Do you want to define a limit? (y/n): n
> Do you want to generate a data file? (y/n): y
> Please enter data file size in megabytes: 2
> Now calculating centroids
[[ 0.29593915  0.87711703]
 [ 0.91356424  0.32456301]
 [ 0.10472423  0.71197471]
 [ 0.28040085  0.45247715]
 [ 0.49112003  0.91361268]
 [ 0.49576576  0.50424544]
 [ 0.8992449   0.09889416]
 [ 0.34554032  0.2782289 ]
 [ 0.90668573  0.53675608]
 [ 0.68096499  0.08694059]
 [ 0.0942271   0.09982239]
 [ 0.89046297  0.7327958 ]
 [ 0.6853976   0.88301196]
 [ 0.48151309  0.09816654]
 [ 0.08924305  0.51120193]
 [ 0.7150915   0.4555357 ]
 [ 0.74746303  0.26060756]
 [ 0.30561794  0.64802739]
 [ 0.10028467  0.90947882]
 [ 0.5534239   0.30031605]
 [ 0.69612629  0.65573274]
 [ 0.28079449  0.09722093]
 [ 0.89528204  0.91471021]
 [ 0.49967817  0.71693477]
 [ 0.11103228  0.29887778]]
> Time spent calculating centroids: 9.14600014687
> Now plotting
> Time spent plotting: 148.612999916
> Objective function result: 264.987686639
```

Some results with different settings:

```
> Number of centroids: 10
> Data file size in megabytes: 100 (2000000 two dimensional points)

> Limit: No

> Time spent calculating centroids: 255.254999876 seconds (4 minutes 15 seconds)
> Time spent plotting: 1098.23200011 seconds (18 minutes 18 seconds)
> Objective function result: 33996.1672088
> RAM usage: peak at ~400 mb

> Limit: 50 points

> Time spent calculating centroids: 779.876999855 seconds (13 minutes)
> Time spent plotting: 989.68599987 seconds (16 minutes 30 seconds)
> Objective function result: 40939.884787
> RAM usage: peak at ~30 mb
```
