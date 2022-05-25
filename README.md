# Script Python - API


L'objectif : Réaliser un script Python, à partir de l'API de la Flotte Océanographique Française, qui permet d'identifier :
- le navire ayant été le plus au nord en 2021
- le navire dont la moyenne des relevés de température d'eau est la plus élevée en 2021

Les données fournie part l'API sont disponible sur le site [Position des navires de la Flotte Océanographique Française](https://www.data.gouv.fr/fr/datasets/position-des-navires-de-la-flotte-oceanographique-francaise/)


### Description du script

Le script Python se décompose en 3 étapes principale : La **Initialisation**, le **Traitement de données** et le **programme Main** :

1. La **Initialisation** : 
  * Il s'agit simplement de récupérer les données avec une **requête** à l'aide de l'**API** du site [Position des navires de la Flotte Océanographique Française](https://www.data.gouv.fr/fr/datasets/position-des-navires-de-la-flotte-oceanographique-francaise/), puis on affecte le JSON du résultat de la requête à une variable.
    ```python
    url = "https://localisation.flotteoceanographique.fr/api/v2/vessels"
    response = requests.get(url)
    listOfShip = response.json()
    ```
  * finalement, on déclare les variables `startDate` et `endDate`, on récupère les arguments (si ils existent), et on affecte des valeurs en fonction d'un argument aux deux variables
    ```python
    # Declaration of variables of Dates
    global startDate, endDate

    # Check arguments
    args = sys.argv
    if(len(args) > 2):
        startDate = ""+args[2]+"-01-01T00:00:00.000Z"
        endDate = ""+args[2]+"-12-31T23:59:59.000Z"
    else :
        startDate = "2021-01-01T00:00:00.000Z"
        endDate = "2021-12-31T23:59:59.000Z"
    ```

2. Le **Traitement de données** : est simplement la partie avec les fonctions. Ces dernières vont manipuler le JSON (qui est sous forme de tableau). Chaque fonction a sa propre utilité, certaines vont faire aussi une requête pour récuperer des données supplémentaires sur un des objets du tableau (de JSON) (comme `getShipPosition(shipList, i,  startDate, endDate)`, d'autres vont parcourir des tableaux pour retourner la valeur maximal d'une clé ou d'un attribut (tel que `maxAverage(listShipA)`).

3. L'étape **programme Main** est le programme principale, une suite d'instruction dans un ordre précis, permettant une solution au problème donnée. C'est de la manipulation de liste (ou de tableaux) pour récupérer les données recherchés et on les affectes à la variable `resultShipData` contenant les données ciblées de la liste de navires :
    ```python
    resultShipData = []

    for i in range(0, len(listOfShip)):
        shipPositions = getShipPosition(listOfShip, i, startDate,e endDate)
        a = {'id': listOfShip[i]['id'], 'name': listOfShip[i]['name'], 'average' : tempAverage(shipPositions)}
        a['dataNorth'] = northernmostPoint(shipPositions)
        resultShipData.append(a)
    ```
    Finalement, on récupere les données sur le navire ayant été le plus au nord et sur le navire dont la moyenne des relevés de température d'eau est la plus élevée en 2021 dans deux variables séparés
    ```python
    shipMaxAverage = maxAverage(resultShipData)
    shipNortherPoint = maxNorthPoint(resultShipData)
    ```
    
    *(Note : vous avez la possibilité d'entrer l'année en argument lors de l'exécution du programme)*
    


