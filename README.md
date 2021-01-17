# pi_estimator
Ce projet consiste à une estimation de pi par une approche de tirage aléatoire.
Deux méthodes sont utilisées à savoir l’utilisation de Spark d’une part et l’utilisation de numpy d’autre part.
# Instructions  
:arrow_forward: Ouvrir l'invité de commande

:arrow_forward: Rentrer l'instruction ci-dessous en se plaçant dans le même repertoire.

     "spark-submit pi_estimator.py"

:arrow_forward: Les resultats attendus apparaîtront directement dans la console.  

Voici un exemple de sortie.  

![](https://github.com/ibsagno95/pi_estimator/blob/master/output/output%20pi.png)

Les résultats des deux opérations sont contenus dans les tableaux ci-dessous :  

**Pour n= 100 000**  
| | Spark | Numpy |
|------------|------:|------:|
|Temps d'éxécution (secondes)| 2.673104| 0.089405|
|Valeur de Pi | 3.138320| 3.136640|
|Écart % Math.pi | 0.003273 |  0.004953| 


**Pour n= 1000 000***  

| | Spark | Numpy |
|------------|------:|------:|
|Temps d'éxécution (secondes)|1.842183| 0.875065|
|Valeur de Pi | 3.141132| 3.144836|
|Écart % Math.pi |0.000461 |  0.003243| 


:heavy_check_mark: On constate que pour n= 100 000, l'éxecution est plus rapide avec numpy qu'avec spark mais l'estimation de spark est plus précise que celle de numpy.  
Pour n= 1000 000, le temps d'éxecution de spark est réduit mais reste inférieure à celle de numpy. Tout porte à croire que le temps d'éxécution de spark sera meilleur pour **n** très grand.
