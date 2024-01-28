people = [1,49,50,51,56,199,200,201,202,203,204,205,206]
buses = 0
taxi = 0
taxiPeople = 0
counter = 0
for i in people:
  taxiPeople = i%50
  if(taxiPeople%5 != 0):
    taxiPeople = (taxiPeople  - (taxiPeople%5)) + 5
  if(i < 50):
    taxi = i//5+1
  elif(i == 50):
    buses = 1
    taxi = 0
  elif (i > 50):
      buses = i//50
      taxi = taxiPeople//5
  print(i, 'people will need', buses, 'buses and', taxi, 'taxis')
  end = ''