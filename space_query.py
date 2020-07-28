import argparse
import urllib.request
import json
import datetime

CURRENT_LOC_URL = 'http://api.open-notify.org/iss-now.json'
PASSING_LOC_URL = 'http://api.open-notify.org/iss-pass.json?lat={}&lon={}'
PEOPLE_INFO_URL = 'http://api.open-notify.org/astros.json'

CURRENT_LOC_MSG = "The ISS current location at {} is ({}, {})."
PASSING_LOC_MSG = "The ISS will be overhead ({}, {}) at {} for {} seconds."
PEOPLE_INFO_MSG = "Craft Name: {}\nNum People: {}"

ERROR_MSG = "Sorry, but we're having trouble retrieving that information. Please try again."
SEPERATOR = "-----------------------"

def format_timestamp(timestamp):
    utc_datetime = str(datetime.datetime.utcfromtimestamp(timestamp)) + " (UTC)"
    return utc_datetime

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-l", "--loc", dest="current_loc", action="store_true", help="Print the current location of the ISS.")
    parser.add_argument("-p", "--pass", dest="passing_loc", help="Print the passing details of the ISS for a given location. Takes argument of the form (latitude, longitude).")
    parser.add_argument("-pp", "--people", dest="people_info", action="store_true", help="Print the details of those people that are currently in space." )
    args = parser.parse_args()
    return args

def parse_loc(passing_loc):
    unwanted_chars = '() '
    formatted_loc = passing_loc
    for char in unwanted_chars:
        formatted_loc = formatted_loc.replace(char, '')
    lat, lon = formatted_loc.split(',')
    return lat, lon

def print_current_location():
    try:
        with urllib.request.urlopen(CURRENT_LOC_URL) as response:
            obj = json.loads(response.read())
            lat = obj['iss_position']['latitude']
            lon = obj['iss_position']['longitude']
            date_time_str = format_timestamp(obj['timestamp'])
            print(SEPERATOR)
            print(CURRENT_LOC_MSG.format(date_time_str, lat, lon))
    except:
        print(ERROR_MSG)

def print_passing_loc(passing_loc):
    lat, lon = parse_loc(passing_loc)
    try:
        with urllib.request.urlopen(PASSING_LOC_URL.format(lat, lon)) as response:
            obj = json.loads(response.read())
            for passing_details in obj['response']:
                date_time_str = format_timestamp(passing_details['risetime'])
                print(SEPERATOR)
                print(PASSING_LOC_MSG.format(lat, lon, date_time_str, passing_details['duration']))
    except:
        print(ERROR_MSG)

def print_people_details():
    try:
        with urllib.request.urlopen(PEOPLE_INFO_URL) as response:
            craft_details = {}
            obj = json.loads(response.read())
            for person in obj['people']:
                person_name = person['name']
                craft_name = person['craft']
                if craft_name in craft_details.keys():
                    craft_details[craft_name].append(person_name)
                else:
                    craft_details[craft_name] = [person_name]
            
            print(SEPERATOR)
            print("Listed below are the personnel details for each space craft: ")
            for craft_name, people in craft_details.items():
                print(SEPERATOR)
                print(PEOPLE_INFO_MSG.format(craft_name, len(people)))
                for person in people:
                    print("\t{}".format(person))
                print(SEPERATOR)
    except:
        print(ERROR_MSG)

def main(args):
    if args.current_loc:
        print_current_location() 

    if args.passing_loc:
        print_passing_loc(args.passing_loc)

    if args.people_info:
        print_people_details()

if __name__ == '__main__':
    args = parse_args()
    main(args)