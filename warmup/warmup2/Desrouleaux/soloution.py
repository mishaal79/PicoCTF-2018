import json
from collections import Counter

f = open("incidents.json","r")

tickets = json.load(f)

# print (incidents)

for incident in tickets['tickets']:
    print (incident['src_ip'])

## Get all src ip into a list

srcList = list(tickets['tickets']['src_ip'].values())

print (srcList)
