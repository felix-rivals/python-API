# Script Python - API


L'objectif : Réaliser un script Python qui, à partir de l'API de la Flotte Océanographique Française, permet d'identifier :
- le navire ayant été le plus au nord en 2021
- le navire dont la moyenne des relevés de température d'eau est la plus élevée en 2021

Les données fournie part l'API sont disponible sur le site [Position des navires de la Flotte Océanographique Française](https://www.data.gouv.fr/fr/datasets/position-des-navires-de-la-flotte-oceanographique-francaise/)


### Description du script

Le script Python se décompose en 3 étapes principale : La **Initialisation**, le **Traitement de données** et le **programme Main** :

1. La **Initialisation** : 
  * Il s'agit simplement de récupérer les données avec une **requête** à l'aide de l'**API** du site [Position des navires de la Flotte Océanographique Française](https://www.data.gouv.fr/fr/datasets/position-des-navires-de-la-flotte-oceanographique-francaise/), 
  * puis on affecte le JSON du résultat de la requête à une variable.
    ```python
    url = "https://localisation.flotteoceanographique.fr/api/v2/vessels"
    
    response = requests.get(url)

    listOfShip = response.json()
    ```
  * finalement, on déclare les variables `startDate` et `endDate`, on récupère les arguments (si ils existent), et on affecte des valeurs en fonction d'un argument aux deux variables

2. Le **Traitement de données** : est simplement la partie avec les fonctions. Ces dernières vont manipuler le JSON (qui est sous forme de tableau). Chaque fonction a sa propre utilité, certaines vont faire aussi une requête pour récuperer des données supplémentaires sur un des objets du tableau (de JSON) (comme `getShipPosition(shipList, i,  startDate, endDate)`, d'autres vont parcourir des tableaux pour retourner la valeur maximal d'une clé ou d'un attribut (tel que `maxAverage((listShipA)`.

3. Le **programme Main** est le programme principale, une suite d'instruction dans un ordre précis, permettant une solution au problème donnée. C'est juste un parcours du tableau `
