carsList = {
  "car1" : {
    "name" : "Toyota Corolla",
    "year" : 2009,
    "color": "red"
  },
  "car2" : {
    "name" : "Honda Civic",
    "year" : 2007,
    "color": "black"
  },
  "car3" : {
    "name" : "Subaru Forester",
    "year" : 2011,
    "color": "blue"
  }
}

for x in carsList:
    if carsList[x].get("year") == 2009:
        print (carsList[x].get("name"))