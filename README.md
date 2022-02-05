# Script Python - API


L'objectif : Réaliser un script Python qui, à partir de l'API de la Flotte Océanographique Française, permet d'identifier :
- le navire ayant été le plus au nord en 2021
- le navire dont la moyenne des relevés de température d'eau est la plus élevée en 2021

Les données fournie part l'API sont disponible sur https://www.data.gouv.fr/fr/datasets/position-des-navires-de-la-flotte-oceanographique-francaise/


### Description du script

Le script Python se décompose en 3 étapes principale : La **Initialisation**, le **Traitement de données** et le **programme Main** :

1. La **Initialisation** :
  * Il s'agit simplement de récupérer les données avec une **requête** à l'aide de l'**API** du site https://www.data.gouv.fr/fr/datasets/position-des-navires-de-la-flotte-oceanographique-francaise/
  * puis on affecte le JSON du résultat de la requête à une variable

1. Le **Traitement de données** : est simplement la partie avec les fonctions. Ces dernières vont manipuler le JSON (qui est sous forme de tableau). Chaque fonction a sa propre utilité, certaines vont faire aussi une requête pour récuperer des données supplémentaires sur un des objets du tableau (de JSON), d'autres vont parcourir des tableaux pour retourner la valeur maximal d'une clé ou d'un attribut



