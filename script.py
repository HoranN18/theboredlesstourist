#background information
destinations = ["Paris, France", "Shanghai, China", "Los Angeles, USA", "Sao Paulo, Brazil", "Cairo, Egypt"]

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

#getting destination index
def get_destination_index(destination):
  destination_index = destinations.index(destination)
  return destination_index

#get traveler location 
def get_traveler_location(traveler):
#look at string in the 1 postiion of array to get destination name and uses get destination index
  traveler_destination = traveler[1]
  traveler_destination_index = get_destination_index(traveler_destination)
  return traveler_destination_index
test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)