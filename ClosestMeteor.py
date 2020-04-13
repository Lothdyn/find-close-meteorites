
import math
import requests

def calc_dist(lat1, lon1, lat2, lon2):
       lat1 = math.radians(lat1)
       lon1 = math.radians(lon1)
       lat2 = math.radians(lat2)
       lon2 = math.radians(lon2)
       h = math.sin( (lat2 - lat1) / 2) ** 2 + \
            math.cos(lat1) * \
            math.cos(lat2) * \
            math.sin( (lon2 - lon1) / 2) ** 2
       return 6372.8 * 2 * math.asin(math.sqrt(h))

def get_dist(meteor):
  return meteor.get('distance',math.inf)

my_loc = (-37.8136,144.9631) # Melbourne lat and longitude


meteor_resp = requests.get('https://data.nasa.gov/resource/gh4g-9sfh.json')
meteor_data = meteor_resp.json() #This comes back as a lists


for meteor in meteor_data:
  if not ('reclat' in meteor and 'reclong' in meteor): continue # This just allows the loop to continue
  meteor['distance'] = calc_dist(float(meteor['reclat']),float(meteor['reclong']),my_loc[0],my_loc[1])



  # math.inf represents a number that is larger than any other number, so will always sort to the end of our list.

meteor_data.sort(key=get_dist)
  # notice that we're not calling get_dist here. Just passing its name as a parameter
  # you can pass functions to other functions

print(meteor_data[0:10])
