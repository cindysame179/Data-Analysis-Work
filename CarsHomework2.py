import pandas as pd
#(1)Takes the raw data set from github and labels the corresponding headers
df = pd.read_csv('https://raw.githubusercontent.com/cindysame179/Data-Analytics-Work/main/cars-sample35.csv', names = ['price','Maintenance cost','Number of doors','Number of passengers','Luggage capacity', 'safety rating', 'Classification of vehicle'])
df.head()

#(2)
#list of prices
priceL = df.iloc[:,0].copy()

#list of Maintenance Cost
MCL = df.iloc[:,1].copy()

#list of Number of Doors
doorsL = df.iloc[:,2].copy()

#list of Number of Passengers
passengerL = df.iloc[:,3].copy()

#list of Luggage Capacity
luggageL = df.iloc[:,4].copy()

#list of Safety Rating
SRL = df.iloc[:,5].copy()

#list of Classification of vehicle
classificationL = df.iloc[:,6].copy()

priceL.head()

#(3)
PriceMedL = []
for i in range(len(priceL)):
  if priceL[i] == 'med':
    PriceMedL.append(i)
print(PriceMedL)

#(4)
PassengerMedL = []
for i in PriceMedL:
  PassengerMedL.append(passengerL[i])
print(PassengerMedL)

#(5)
carsub = df.iloc[:,[0,1]].copy()
HighNotLow = []
for i in range(len(carsub)):
  if (carsub['price'][i] == 'high') & (carsub['Maintenance cost'][i] != 'low'):
    HighNotLow.append(i)
print(HighNotLow)

#(6)
PriceMedLC = [i for i in range(len(priceL)) if priceL[i]=='med']
print(PriceMedLC)

#(7)
PassengerMedLC = [passengerL[i] for i in PriceMedL]
print(PassengerMedLC)

#(8)
carsub = df.iloc[:,[0,1]].copy()
HighNotLowLC = [i for i in range(len(carsub)) if (carsub['price'][i] == 'high') & (carsub['Maintenance cost'][i] != 'low')]
print(HighNotLowLC)

#Nested List Comprehension
nlist = [ [1, 2, 3], ['A', 'B', 'C'], [4, 5], ['D', 'E'] ]
list2 = [j for i in nlist for j in i]
print(list2)