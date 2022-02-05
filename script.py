
import requests
import math

url = "https://localisation.flotteoceanographique.fr/"

urlListNavire = "https://localisation.flotteoceanographique.fr/api/v2/vessels"

response = requests.get(urlListNavire)

print(response.status_code)

# print(response[0])

print('-------------------------------------------')

dataNavire = response.json()

# The Year2021
startDate = "2021-01-01T00:00:00.000Z"
endDate = "2021-12-31T23:59:59.000Z"

# Coordinate of the North
global latNorth, lonNorth
latNorth = 90.000000
lonNorth = -135.000000

def getShipPosition(i, startDate, endDate):
    ps = requests.get(url+ "/api/v2/vessels/"+dataNavire[i]['id']+"/positions?startDate="+startDate+"&endDate="+endDate)
    positionsInArray = ps.json()
    return positionsInArray


def averageTemp(shipData):
    tempAverage = 0
    for i in range(0,len(shipData)-1):
        if('seatemp' in shipData[i]['data']):
            tempAverage = tempAverage + shipData[i]['data']['seatemp']
            # print(shipData[i]['data']['seatemp'])

        # print(tempAverage)
    
    tempAverage = tempAverage / len(shipData)
    return tempAverage

def maxLattitude(shipData):
    max = shipData[0]
    for i in range(0,len(shipData)-1):
        if(shipData[i]['lat'] > max['lat']):
            max = shipData[i]
    
    return max


reponse = requests.get(url+"/api/v2/vessels/"+dataNavire[0]['id']+"/positions")
ship0Postions = getShipPosition(0, startDate, endDate);

averageTempShip0 = averageTemp(ship0Postions)

maxLatShip0 = maxLattitude(ship0Postions)

print(type(ship0Postions))

print(len(ship0Postions))

print("average temp : ",averageTempShip0)
print(maxLatShip0)






