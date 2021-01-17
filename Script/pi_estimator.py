#On importe SparkConf et SparkContext dans l'environnement 
from pyspark import SparkConf,SparkContext
import numpy as np
import pandas as pd
import random
import time
import math

#Instantiation du client Spark sous Python
if __name__ == "__main__":
    conf = SparkConf().setAppName('pi_estimator').setMaster("local")
    sc = SparkContext(conf=conf)
    sc.setLogLevel("ERROR")

#Fonction de simulation de point
def is_point_inside_unit_circle(p):
    x, y = random.random(), random.random()   # simuler deux point  x et y
    return 1 if x*x + y*y < 1 else 0 #vérifier si ces deux point sont dans le cercle

#test de la fonction
print(is_point_inside_unit_circle(3))

#Fonction pi_estimator_spark(n)
def pi_estimator_spark(n):
    count=sc.parallelize(range(0,n))
    k=count.map(is_point_inside_unit_circle)
    interieur= k.filter(lambda x: x==1).count()
    pi_estimator= 4 * interieur/n
    return  pi_estimator

tps1 = time.time()
pi_spark=pi_estimator_spark(100000)
tps2 = time.time()
Temps_spark=tps2-tps1

#En utilisant numpy 
def pi_estimator_numpy(n):
    count=np.array(range(0,n))
    cercle=np.array([is_point_inside_unit_circle(i) for i in count])
    #interieur= len([x for x in cercle if x==1])
    interieur= len(cercle[cercle==1])
    pi_estimator_numpy= 4*interieur/n
    return pi_estimator_numpy

tps_1= time.time()
pi_numpy=pi_estimator_numpy(100000)
tps_2=time.time()
Temps_numpy= tps_2-tps_1

print("################ Pour n=100 000 ######################")
arr= np.array([[Temps_spark,Temps_numpy],[pi_spark,pi_numpy],[math.pi-pi_spark,math.pi-pi_numpy]])
tableau=pd.DataFrame(arr,index=["temps d execution","valeur de pi","ecart"],columns=["spark","numpy"])
print(tableau)

#Pour n=1000000
tps_1= time.time()
pi_numpy=pi_estimator_numpy(1000000)
tps_2=time.time()
Temps_numpy= tps_2-tps_1

tps1 = time.time()
pi_spark=pi_estimator_spark(1000000)
tps2 = time.time()
Temps_spark=tps2-tps1
print("################ Pour n=1 000 000 ######################")
arr= np.array([[Temps_spark,Temps_numpy],[pi_spark,pi_numpy],[math.pi-pi_spark,math.pi-pi_numpy]])
tableau2=pd.DataFrame(arr,index=["temps d execution","valeur de pi","ecart"],columns=["spark","numpy"])
print(tableau2)

#on ferme 
sc.stop()