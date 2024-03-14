import argparse, json, csv, math
from datetime import datetime

parser = argparse.ArgumentParser(description='Convert Google Maps location history to csv file.')
parser.add_argument('-i', '--input', action="store", help='C:\Users\connie\Downloads\takeout-20240312T052014Z-002\Takeout\Location History (Timeline)\Semantic Location History\2024\2024_MARCH .json file.', required=True)
parser.add_argument('-o', '--output', action="store", help='C:\Users\connie\Desktop\Personal Docs\Woody\ .csv file.', required=True)

args = parser.parse_args()
file = open(args.input)
data = json.load(file)
locations = data['locations']
with open(args.output, 'w') as csvfile:
    filewriter = csv.writer(csvfile, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    filewriter.writerow(['timestamp', 'latitude', 'longitude'])
    for l, location in enumerate(locations):
      timestamp = datetime.utcfromtimestamp(int(location['timestampMs']) / 1000)
      filewriter.writerow([timestamp, float(location['latitudeE7'])/math.pow(10, 7), float(location['longitudeE7'])/math.pow(10, 7)])

print('Done! Wrote ' + str(len(locations)) + ' points.')
