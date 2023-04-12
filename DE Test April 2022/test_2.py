# A team of analysts wish to discover how far people are travelling to their nearest
# desired court. We have provided you with a small test dataset so you can find out if
# it is possible to give the analysts the data they need to do this. The data is in
# `people.csv` and contains the following columns:
# - person_name
# - home_postcode
# - looking_for_court_type

# The courts and tribunals finder API returns a list of the 10 nearest courts to a
# given postcode. The output is an array of objects in JSON format. The API is
# accessed by including the postcode of interest in a URL. For example, accessing
# https://courttribunalfinder.service.gov.uk/search/results.json?postcode=E144PU gives
# the 10 nearest courts to the postcode E14 4PU. Visit the link to see an example of
# the output.

# Below is the first element of the JSON array from the above API call. We only want the
# following keys from the json:
# - name
# - dx_number
# - distance
# dx_number is not always returned and the "types" field can be empty.

"""
[
    {
        "name": "Central London Employment Tribunal",
        "lat": 51.5158158439741,
        "lon": -0.118745425821452,
        "number": null,
        "cci_code": null,
        "magistrate_code": null,
        "slug": "central-london-employment-tribunal",
        "types": [
            "Tribunal"
        ],
        "address": {
            "address_lines": [
                "Victory House",
                "30-34 Kingsway"
            ],
            "postcode": "WC2B 6EX",
            "town": "London",
            "type": "Visiting"
        },
        "areas_of_law": [
            {
                "name": "Employment",
                "external_link": "https%3A//www.gov.uk/courts-tribunals/employment-tribunal",
                "display_url": "<bound method AreaOfLaw.display_url of <AreaOfLaw: Employment>>",
                "external_link_desc": "Information about the Employment Tribunal"
            }
        ],
        "displayed": true,
        "hide_aols": false,
        "dx_number": "141420 Bloomsbury 7",
        "distance": 1.29
    },
    etc
]
"""

import pandas as pd
import numpy as np
from pandas import DataFrame
import requests

API_URL = 'https://courttribunalfinder.service.gov.uk/search/results.json'

# Use this API and the data in people.csv to determine how far each person's nearest
# desired court is. Generate an output (of whatever format you feel is appropriate)
# showing, for each person:
# - name
# - type of court desired
# - home postcode
# - nearest court of the right type
# - the dx_number (if available) of the nearest court of the right type
# - the distance to the nearest court of the right type

if __name__ == "__main__":
    # [TODO]: write your answer here
    people_in: DataFrame = pd.read_csv('people.csv')

    person_list = people_in.T.to_dict('list')
    
    
    for person in person_list.keys():
        postcode, court_type = person_list[person][1], person_list[person][2]

        best_court, min_dist = None, np.inf

        possible_courts = requests.get(url=API_URL + f'?postcode={postcode}').json()
        for court in possible_courts:
            if court_type in court['types'] and court['distance'] < min_dist:
                best_court = court
                min_dist = court['distance']
        
        if not best_court is None:
            person_list[person].append(best_court['name'])
            person_list[person].append(best_court['dx_number'])
            person_list[person].append(best_court['distance'])
    
    people = pd.DataFrame(data=person_list).T
    people.columns = ['person_name', 'home_postcode', 'looking_for_court_type', 'court_name', 'court_dx', 'distance']
    people.to_csv('output.csv')
            

