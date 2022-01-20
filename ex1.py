#passing parameters cars and k to the function
def carParkingRoof(cars,k):
  
#min1 is declared to store the minimum roof to cover k cars
min1=9999
#sort the cars according to their positions
cars.sort()
#taking all k combinations and checking the minimum value and maximum value
for i in range(len(cars)-(k-1)):
#checking every combination and update the minimum value into the min1
if((cars[i+k-1]-cars[i])<min1):
min1=(cars[i+k-1]-cars[i])
#returning the answer
return min1+1
"""