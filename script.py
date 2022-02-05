
from ast import arg
import requests
import math
import sys


# Get Data from API with url

url = "https://localisation.flotteoceanographique.fr/"

urlShipList = "https://localisation.flotteoceanographique.fr/api/v2/vessels"

response = requests.get(urlShipList)

print(response.status_code)

listOfShip = response.json()

# Declaration of variables of Dates
global startDate, endDate
startDate = "2021-01-01T00:00:00.000Z"
endDate = "2021-12-31T23:59:59.000Z"

# Check arguments
args = sys.argv
if(len(args) > 2):
    startDate = ""+args[2]+"-01-01T00:00:00.000Z"
    endDate = ""+args[2]+"-12-31T23:59:59.000Z"


# returns a list with the entire position with datas of one ship during a whole year
def getShipPosition(shipList, i,  startDate, endDate):
    ps = requests.get(url+"/api/v2/vessels/"+shipList[i]['id']+"/positions?startDate="+startDate+"&endDate="+endDate)
    positionsInArray = ps.json()
    return positionsInArray

# returns the average of sea-temperature of one ship
def tempAverage(shipPos):
    tempAverage = 0
    for i in range(0,len(shipPos)-1):
        if('seatemp' in shipPos[i]['data']):
            tempAverage = tempAverage + shipPos[i]['data']['seatemp']
            # print(shipPos[i]['data']['seatemp'])

        # print(tempAverage)
    
    tempAverage = tempAverage / len(shipPos)
    return tempAverage

# retuns the element i of the array named 'shipPos' with the highest value for the key 'lat', it returns a dictionnary
def northernmostPoint(shipPos):
    max = shipPos[0]
    for i in range(0,len(shipPos)-1):
        if(shipPos[i]['lat'] > max['lat']):
            max = shipPos[i]
    
    return max


def maxAverage(listShipA):
    maxA = listShipA[0]
    for i in range(0, len(listShipA)):
        if(listShipA[i]['average'] > maxA['average']):
            maxA = listShipA[i]

    return maxA

def maxNorthPoint(listShipNP):
    maxNP = listShipNP[0]
    for i in range(0, len(listShipNP)):
        if(listShipNP[i]['dataNorth']['lat'] > maxNP['dataNorth']['lat']):
            maxNP = listShipNP[i]

    return maxNP


resultShipData = []

for i in range(0, len(listOfShip)):
    shipPositions = getShipPosition(listOfShip, i, startDate, endDate)
    a = {'id': listOfShip[i]['id'], 'name': listOfShip[i]['name'], 'average' : tempAverage(shipPositions)}
    a['dataNorth'] = northernmostPoint(shipPositions)
    resultShipData.append(a)



shipMaxAverage = maxAverage(resultShipData)
shipNortherPoint = maxNorthPoint(resultShipData)


print('------------------------------------------------')
print(' The northermost Ship is ',shipMaxAverage['name'],', with a sea-temperature average of ',shipMaxAverage['average'])
print(' The ship with the highest Seatemp Average is ',shipNortherPoint['name'],', with a lattitude : ',shipNortherPoint['dataNorth']['lat'])






