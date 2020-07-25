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

#list of attractions
attractions = [[] for destination in destinations]

def add_attraction(destination, attraction):
 try:
  destination_index = get_destination_index(destination)
  attractions_for_destination = attractions[destination_index]
  attractions_for_destination.append(attraction)
  return attractions_for_destination
 except ValueError:
   return
#adding attractions to the search engine
add_attraction("Los Angeles, USA", ['Venice Beach', ['beach']])
add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", ["historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", ["garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", ["skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("Sao Paulo, Brazil", ["Sao Paulo Zoo", ["zoo"]])
add_attraction("Sao Paulo, Brazil", ["Patio do Colegio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", ["monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])

def find_attractions(destination, interests):
  destination_index = get_destination_index(destination)
  attractions_in_city =attractions[destination_index]
  attractions_with_interest = []
  for attraction in attractions_in_city:
    possible_attraction = [attraction[0]]
    attraction_tags = attraction[1]
    for interest in interests:
      if interest in attraction_tags:
        append = possible_attraction[0]
        attractions_with_interest.append(append)
  return attractions_with_interest

la_arts = find_attractions("Los Angeles, USA", ["art"])

print(la_arts)







