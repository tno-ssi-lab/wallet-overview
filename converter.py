import csv, json
from lxml import etree, html
from pprint import pprint
from json2html import *

with open('wallet-chars.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    json_dict = {}
    for row in reader:
        json_dict[row[1]] = {}
        json_dict[row[1]].update({'openSource':row[12]})
        json_dict[row[1]].update({'connectionTypes':row[13]})
        json_dict[row[1]].update({'peer2peerProtocols':row[14]})
        json_dict[row[1]].update({'credExchangeProtocol':row[15]})
        if row[16] == "Yes":
            json_dict[row[1]].update({'blockchain':{'type': row[17], 'purpose': row[18]}})
        cred_profile = {}
        cred_profile["credentialFormat"] = row[4]
        cred_profile["signatureAlgorithm"] = row[5]
        cred_profile["revocationAlgorithm"] = row[6]
        if row[8] != "":
            cred_profile["identifierIssuer"] = row[8]
        else:
            cred_profile["identifierIssuer"] = row[7]
        if row[10] != "":
            cred_profile["identifierHolder"] = row[10]
        else:
            cred_profile["identifierHolder"] = row[9]
        extra = {}
        if row[11] != "":
            extra = row[11]
            # parse
        json_dict[row[1]].update({'credProfiles': [cred_profile, extra]})
        print(json_dict[row[1]])
        
    #print(json.dumps(json_dict))
    print(json.dumps(json_dict, indent=4))
    csv_file.close()
html = html.fromstring(json2html.convert(json = json_dict))
print(html)
print(etree.tostring(html, encoding='unicode', pretty_print=True))