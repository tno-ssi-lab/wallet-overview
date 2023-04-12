import csv, json
from json2html import *
import collections

keys = ['name', 'company', 'openSource', 'connectionTypes', 'deepLinking', 'selectiveDisclosure', 'predicates', 'offlineFriendly', 'peer2peerProtocols', 'credExchangeProtocol', 'blockchain', 'credentialFormat', 'encodingScheme', 'cryptoAgility', 'signatureAlgorithm', 'verifierUnlinkability', 'hardwareSupport', 'postQuantumSecure', 'revocationAlgorithm', 'observability', 'identifierHolder', 'identifierIssuer', 'keyRotationHolder', 'keyHistoryHolder', 'keyRotationIssuer', 'keyHistoryIssuer', 'logo']

def create_wallet_dict_old_part(cred_profiles:dict) -> dict:
    """
        Creates a dictionary with the relevant characteristics for each wallet, based on the input from the Google Form. From the choices specified in the form, characteristics from the credential comparison matrix are added. 

        param cred_profiles (dict): relevant information from the credential comparison matrix
        returns: the dictionary containing all wallets and their characteristics
    """
    with open('./data/wallet-chars-15.csv', 'r') as csv_file:
        next(csv_file)
        next(csv_file)
        reader = csv.reader(csv_file)
        json_dict = {}
        for row in reader:
            if row[1] == 'PRISM':
                row[1] = 'Atala PRISM'
            if row[1] == 'walt.id Wallet Kit':
                row[1] = 'walt.id'
            if 'IRMA' in row[1]:
                row[1] = 'Yivi'

            json_dict[row[1]] = {}
            json_dict[row[1]].update({'name':row[1]})
            json_dict[row[1]].update({'company':'tbd'})
            json_dict[row[1]].update({'openSource':row[12]})
            json_dict[row[1]].update({'connectionTypes':(', '.join(row[13].split(';')))})
            json_dict[row[1]].update({'peer2peerProtocols':(', '.join(row[14].split(';')))})
            json_dict[row[1]].update({'credExchangeProtocol':(', '.join(row[15].split(';')))})
            if row[16] == "Yes":
                json_dict[row[1]].update({'blockchain':{'used': 'Yes','type': row[17], 'purpose': row[18]}})
            else:
                json_dict[row[1]].update({'blockchain':{'used': 'No','type': 'N/A', 'purpose': 'N/A'}})
            
            # Get characteristics from credential comparison matrix based on credential format
            json_dict[row[1]].update({"credentialFormat":(', '.join(row[4].split(';')))})
            temp = str(row[4]).split(';')
            encodings = []
            for elem in temp:
                if cred_profiles['credentialFormats'].get(elem):
                    encodings += [cred_profiles['credentialFormats'].get(elem).get('encodingScheme')]
                    if cred_profiles['credentialFormats'].get(elem).get('cryptoAgility') == 'yes':
                        json_dict[row[1]].update({"cryptoAgility":'Yes'}) 
                    if 'yes' in cred_profiles['credentialFormats'].get(elem).get('selectiveDisclosure'):
                        json_dict[row[1]].update({"selectiveDisclosure":'Yes'})
                    if 'yes' in cred_profiles['credentialFormats'].get(elem).get('predicates'):
                        json_dict[row[1]].update({"predicates":'Yes'})
            json_dict[row[1]].update({"encodingScheme":', '.join(encodings)})
            if not json_dict[row[1]].get('cryptoAgility'):
                json_dict[row[1]].update({"cryptoAgility":'No'})
            if not json_dict[row[1]].get('selectiveDisclosure'):
                json_dict[row[1]].update({"selectiveDisclosure":'No'})
            if not json_dict[row[1]].get('predicates'):
                json_dict[row[1]].update({"predicates":'No'})

            # Get characteristics from credential comparison matrix based on signature algorithm
            json_dict[row[1]].update({"signatureAlgorithm": (', '.join(row[5].split(';')))})
            temp = str(row[5]).split(';')
            for elem in temp:
                if cred_profiles['signature'].get(elem):
                    if cred_profiles['signature'].get(elem).get('hardwareSupport') == 'yes':
                        json_dict[row[1]].update({"hardwareSupport":'Yes'}) 
                    if 'yes' in cred_profiles['signature'].get(elem).get('verifierUnlinkability'):
                        json_dict[row[1]].update({"verifierUnlinkability":'Yes'})
                    if 'yes' in cred_profiles['signature'].get(elem).get('postQuantumSecure'):
                        json_dict[row[1]].update({"postQuantumSecure":'Yes'})
            if not json_dict[row[1]].get('hardwareSupport'):
                json_dict[row[1]].update({"hardwareSupport":'No'})
            if not json_dict[row[1]].get('verifierUnlinkability'):
                json_dict[row[1]].update({"verifierUnlinkability":'No'})
            if not json_dict[row[1]].get('postQuantumSecure'):
                json_dict[row[1]].update({"postQuantumSecure":'No'})

            # Get characteristics from credential comparison matrix based on revocation algorithm
            json_dict[row[1]].update({"revocationAlgorithm":(', '.join(row[6].split(';')))})
            if row[6] != 'Revocation not supported':
                temp = str(row[6]).split(';')
                for elem in temp:
                    if cred_profiles['revocation'].get(elem):
                        if cred_profiles['revocation'].get(elem).get('observability') == 'yes':
                            json_dict[row[1]].update({"observability":'Yes'}) 
                if not json_dict[row[1]].get('observability'):
                    json_dict[row[1]].update({"observability":'No'})
                # There are more characteristics, such as traceability, but these are all 'tbd', so makes no sense to include at this point.
            
            # Get characteristics from credential comparison matrix based on identifiers
            if row[7] == "DID":
                if "did" not in row[-2].lower():
                    row[-2] = "did:" + row[-2]
                json_dict[row[1]].update({"identifierHolder":row[-2].lower()})
            else:
                json_dict[row[1]].update({"identifierHolder":row[7]})
            if row[8] == "DID":
                if "did" not in row[-1].lower():
                    row[-1] = "did:" + row[-1]
                json_dict[row[1]].update({"identifierIssuer":row[-1].lower()})
            else:
                json_dict[row[1]].update({"identifierIssuer":row[8]})

            temp = json_dict[row[1]]['identifierHolder'].split(';')
            for elem in temp:
                if cred_profiles['identifiers'].get(elem):
                    if cred_profiles['identifiers'].get(elem).get('keyRotation') == 'yes':
                        json_dict[row[1]].update({"keyRotationHolder":'Yes'}) 
                    if 'yes' in cred_profiles['identifiers'].get(elem).get('keyHistory'):
                        json_dict[row[1]].update({"keyHistoryHolder":'Yes'})
            if not json_dict[row[1]].get('keyRotationHolder'):
                json_dict[row[1]].update({"keyRotationHolder":'No'})
            if not json_dict[row[1]].get('keyHistoryHolder'):
                json_dict[row[1]].update({"keyHistoryHolder":'No'})

            temp = str(json_dict[row[1]]['identifierIssuer']).split(';')
            for elem in temp:
                if cred_profiles['identifiers'].get(elem):
                    if cred_profiles['identifiers'].get(elem).get('keyRotation') == 'yes':
                        json_dict[row[1]].update({"keyRotationIssuer":'Yes'}) 
                    if 'yes' in cred_profiles['identifiers'].get(elem).get('keyHistory'):
                        json_dict[row[1]].update({"keyHistoryIssuer":'Yes'})
            if not json_dict[row[1]].get('keyRotationIssuer'):
                json_dict[row[1]].update({"keyRotationIssuer":'No'})
            if not json_dict[row[1]].get('keyHistoryIssuer'):
                json_dict[row[1]].update({"keyHistoryIssuer":'No'})
            json_dict[row[1]].update({'logo':f'static/{row[1].lower().replace(" ", "-").replace(".", "-")}.png'})
        csv_file.close()
    
    return collections.OrderedDict(sorted(json_dict.items()))

def create_wallet_dict_new_part(json_dict: dict, cred_profiles:dict) -> dict:
    """
        Creates a dictionary with the relevant characteristics for each wallet, based on the input from the Google Form. From the choices specified in the form, characteristics from the credential comparison matrix are added. After the first 10 answers we changed the form, hence we have to read it out differently.

        param cred_profiles (dict): relevant information from the credential comparison matrix
        returns: the dictionary containing all wallets and their characteristics
    """
    with open('./data/wallet-chars-15.csv', 'r') as csv_file:
        reader = csv.reader(csv_file)
        # Skip the answers from the 'old' form.
        for i in range(44):
            next(csv_file)
        for row in reader:
            if 'IRMA' in row[1]:
                row[1] = 'Yivi'
            json_dict[row[1]] = {}
            json_dict[row[1]].update({'name':row[1]})
            json_dict[row[1]].update({'company':'tbd'})
            json_dict[row[1]].update({'openSource':row[10]})
            json_dict[row[1]].update({'connectionTypes':(', '.join(row[11].split(';')))})
            json_dict[row[1]].update({'deepLinking':row[12]})
            json_dict[row[1]].update({'selectiveDisclosure':row[13]})
            json_dict[row[1]].update({'predicates':row[14]})
            json_dict[row[1]].update({'offlineFriendly':row[15]})
            json_dict[row[1]].update({'peer2peerProtocols':(', '.join(row[16].split(';')))})
            json_dict[row[1]].update({'credExchangeProtocol':(', '.join(row[17].split(';')))})
            if row[18] == "Yes":
                json_dict[row[1]].update({'blockchain':{'used': 'Yes','type': row[19], 'purpose': row[20]}})
            else:
                json_dict[row[1]].update({'blockchain':{'used': 'No','type': 'N/A', 'purpose': 'N/A'}})
            
            # Get characteristics from credential comparison matrix based on credential format
            json_dict[row[1]].update({"credentialFormat":(', '.join(row[4].split(';')))})
            temp = str(row[4]).split(';')
            encodings = []
            for elem in temp:
                if cred_profiles['credentialFormats'].get(elem):
                    encodings += [cred_profiles['credentialFormats'].get(elem).get('encodingScheme')]
                    if cred_profiles['credentialFormats'].get(elem).get('cryptoAgility') == 'yes':
                        json_dict[row[1]].update({"cryptoAgility":'Yes'}) 
                    if 'yes' in cred_profiles['credentialFormats'].get(elem).get('selectiveDisclosure') and not json_dict[row[1]].get('selectiveDisclosure'):
                        json_dict[row[1]].update({"selectiveDisclosure":'Yes'})
                    if 'yes' in cred_profiles['credentialFormats'].get(elem).get('predicates') and not json_dict[row[1]].get('predicates'):
                        json_dict[row[1]].update({"predicates":'Yes'})
            json_dict[row[1]].update({"encodingScheme":', '.join(encodings)})
            if not json_dict[row[1]].get('cryptoAgility'):
                json_dict[row[1]].update({"cryptoAgility":'No'})
            if not json_dict[row[1]].get('selectiveDisclosure'):
                json_dict[row[1]].update({"selectiveDisclosure":'No'})
            if not json_dict[row[1]].get('predicates'):
                json_dict[row[1]].update({"predicates":'No'})

            # Get characteristics from credential comparison matrix based on signature algorithm
            json_dict[row[1]].update({"signatureAlgorithm": (', '.join(row[5].split(';')))})
            temp = str(row[5]).split(';')
            for elem in temp:
                if cred_profiles['signature'].get(elem):
                    if cred_profiles['signature'].get(elem).get('hardwareSupport') == 'yes':
                        json_dict[row[1]].update({"hardwareSupport":'Yes'}) 
                    if 'yes' in cred_profiles['signature'].get(elem).get('verifierUnlinkability'):
                        json_dict[row[1]].update({"verifierUnlinkability":'Yes'})
                    if 'yes' in cred_profiles['signature'].get(elem).get('postQuantumSecure'):
                        json_dict[row[1]].update({"postQuantumSecure":'Yes'})
            if not json_dict[row[1]].get('hardwareSupport'):
                json_dict[row[1]].update({"hardwareSupport":'No'})
            if not json_dict[row[1]].get('verifierUnlinkability'):
                json_dict[row[1]].update({"verifierUnlinkability":'No'})
            if not json_dict[row[1]].get('postQuantumSecure'):
                json_dict[row[1]].update({"postQuantumSecure":'No'})

            # Get characteristics from credential comparison matrix based on revocation algorithm
            json_dict[row[1]].update({"revocationAlgorithm":(', '.join(row[6].split(';')))})
            if row[6] != 'Revocation not supported':
                temp = str(row[6]).split(';')
                for elem in temp:
                    if cred_profiles['revocation'].get(elem):
                        if cred_profiles['revocation'].get(elem).get('observability') == 'yes':
                            json_dict[row[1]].update({"observability":'Yes'}) 
                if not json_dict[row[1]].get('observability'):
                    json_dict[row[1]].update({"observability":'No'})
                # There are more characteristics, such as traceability, but these are all 'tbd', so makes no sense to include at this point.
            
            # Get characteristics from credential comparison matrix based on identifiers
            json_dict[row[1]].update({"identifierHolder":(', '.join(row[7].split(';')))})
            json_dict[row[1]].update({"identifierIssuer":(', '.join(row[8].split(';')))})
            # for first 10 filled, manually fix the resulting JSON.
            temp = json_dict[row[1]]['identifierHolder'].split(';')
            for elem in temp:
                if cred_profiles['identifiers'].get(elem):
                    if cred_profiles['identifiers'].get(elem).get('keyRotation') == 'yes':
                        json_dict[row[1]].update({"keyRotationHolder":'Yes'}) 
                    if 'yes' in cred_profiles['identifiers'].get(elem).get('keyHistory'):
                        json_dict[row[1]].update({"keyHistoryHolder":'Yes'})
            if not json_dict[row[1]].get('keyRotationHolder'):
                json_dict[row[1]].update({"keyRotationHolder":'No'})
            if not json_dict[row[1]].get('keyHistoryHolder'):
                json_dict[row[1]].update({"keyHistoryHolder":'No'})

            temp = str(json_dict[row[1]]['identifierIssuer']).split(';')
            for elem in temp:
                if cred_profiles['identifiers'].get(elem):
                    if cred_profiles['identifiers'].get(elem).get('keyRotation') == 'yes':
                        json_dict[row[1]].update({"keyRotationIssuer":'Yes'}) 
                    if 'yes' in cred_profiles['identifiers'].get(elem).get('keyHistory'):
                        json_dict[row[1]].update({"keyHistoryIssuer":'Yes'})
            if not json_dict[row[1]].get('keyRotationIssuer'):
                json_dict[row[1]].update({"keyRotationIssuer":'No'})
            if not json_dict[row[1]].get('keyHistoryIssuer'):
                json_dict[row[1]].update({"keyHistoryIssuer":'No'})
            json_dict[row[1]].update({'logo':f'static/{row[1].lower().replace(" ", "-").replace(".", "-")}.png'})
        csv_file.close()
    return collections.OrderedDict(sorted(json_dict.items()))

def extend_wallet_dict(wallets: dict) -> dict:
    """
        Extends the dictionary with the relevant characteristics for each wallet. From the prior knowledge in the original wallet overview, characteristics are added to the wallet dictionary. The answer from the Google Forms weighs more than the information in the old wallet overview, as the Google Form is filled in by the wallet vendor.

        param wallets (dict): the dictionary containing wallets and their characteristics
        returns: the dictionary containing all wallets and their characteristics
    """
    with open('./data/wallet-overview-old.csv', 'r') as csv_file:
        next(csv_file)
        next(csv_file)
        # overlap = []
        for row in csv_file:
            row = str(row).split(';')
            if row[0] == 'myEGO2GO - Unique as you are':
                row[0] = 'CertiShare Wallet'
            if row[0] == 'Spherity':
                row[0] = 'Spherity Wallet'
            if row[0] == 'IRMA':
                row[0] = 'Yivi'
            if row[1] == 'PRISM':
                row[1] = 'Atala PRISM'

            if not wallets.get(row[0]):
                wallets[row[0]] = {}
            wallets[row[0]].update({'company':row[2]})
            wallets[row[0]].update({'name':row[0]})
            if not wallets[row[0]].get('openSource'):
                wallets[row[0]].update({'openSource':row[5]})

            if row[11] == 'Yes' and not wallets[row[0]].get('blockchain'):
                wallets[row[0]].update({'blockchain':{'used': 'Yes','type': row[12], 'purpose': 'tbd'}})
            elif row[11] == 'No' and not wallets[row[0]].get('blockchain'):
                wallets[row[0]].update({'blockchain':{'used': 'No','type': 'N/A', 'purpose': 'N/A'}})
            elif not wallets[row[0]].get('blockchain'):
                wallets[row[0]].update({'blockchain':{'used': 'tbd','type': row[12], 'purpose': 'tbd'}})

            if not wallets[row[0]].get('connectionTypes'):
                wallets[row[0]].update({'connectionTypes':row[24]})

            if not wallets[row[0]].get('deepLinking'):
                wallets[row[0]].update({'deepLinking':row[27]})

            if row[33] != '':
                wallets[row[0]].update({'eassi':row[33]})
            else:
                wallets[row[0]].update({'eassi':'No'})

            if not wallets[row[0]].get('credentialFormat'):
                wallets[row[0]].update({'credentialFormat':'tbd'})
            if not wallets[row[0]].get('encodingScheme'):
                wallets[row[0]].update({'encodingScheme':'tbd'})
            if not wallets[row[0]].get('signatureAlgorithm'):
                wallets[row[0]].update({'signatureAlgorithm':'tbd'})
            if not wallets[row[0]].get('identifierHolder'):
                wallets[row[0]].update({'identifierHolder':'tbd'})
            if not wallets[row[0]].get('identifierIssuer'):
                wallets[row[0]].update({'identifierIssuer':'tbd'})
            if not wallets[row[0]].get('revocationAlgorithm'):
                wallets[row[0]].update({'revocationAlgorithm':'tbd'})
            if not wallets[row[0]].get('peer2peerProtocols'):
                wallets[row[0]].update({'peer2peerProtocols':'tbd'})
            if not wallets[row[0]].get('credExchangeProtocol'):
                wallets[row[0]].update({'credExchangeProtocol':'tbd'})
            if not wallets[row[0]].get('offlineFriendly'):
                wallets[row[0]].update({'offlineFriendly':'tbd'})
            if not wallets[row[0]].get('selectiveDisclosure'):
                wallets[row[0]].update({'selectiveDisclosure':'tbd'})
            if not wallets[row[0]].get('predicates'):
                wallets[row[0]].update({'predicates':'tbd'})
            if not wallets[row[0]].get('verifierUnlinkability'):
                wallets[row[0]].update({'verifierUnlinkability':'tbd'})
            if not wallets[row[0]].get('cryptoAgility'):
                wallets[row[0]].update({'cryptoAgility':'tbd'})
            if not wallets[row[0]].get('logo'): 
                wallets[row[0]].update({'logo':f'static/{row[0].lower().replace(" ", "-").replace(".", "-")}.png'})
            # Order the characteristics for each wallet.
            wallets[row[0]] = collections.OrderedDict(sorted(wallets[row[0]].items()))
    csv_file.close()
    return wallets

# Extracting characteristics of the credential format from the credential profile matrix and putting them in dict
def create_cred_profile_dict() -> dict:
    """
        Creates a dictionary with the relevant characteristics for each technology category.

        returns: the dictionary containing all relevant characteristics
    """
    cred_profiles_chars = {}
    with open('./data/cred-format.csv', 'r') as csv_file:
        next(csv_file)
        next(csv_file)
        reader = csv.reader(csv_file)
        cred_profiles_chars['credentialFormats'] = {}
        for row in reader:
            if row[0] != "":
                cred_profiles_chars['credentialFormats'][row[0]] = {}
                cred_profiles_chars['credentialFormats'][row[0]].update({'encodingScheme':row[6]})
                cred_profiles_chars['credentialFormats'][row[0]].update({'cryptoAgility':row[8]})
                cred_profiles_chars['credentialFormats'][row[0]].update({'selectiveDisclosure':row[9]})
                cred_profiles_chars['credentialFormats'][row[0]].update({'predicates':row[10]})
        csv_file.close()
    with open('./data/identifier.csv', 'r') as csv_file:
        next(csv_file)
        next(csv_file)
        reader = csv.reader(csv_file)
        cred_profiles_chars['identifiers'] = {}
        for row in reader:
            if row[0] != "":
                cred_profiles_chars['identifiers'][row[0]] = {}
                cred_profiles_chars['identifiers'][row[0]].update({'keyRotation':row[5]})
                cred_profiles_chars['identifiers'][row[0]].update({'keyHistory':row[6]})
        csv_file.close()
    with open('./data/revocation.csv', 'r') as csv_file:
        next(csv_file)
        next(csv_file)
        reader = csv.reader(csv_file)
        cred_profiles_chars['revocation'] = {}
        for row in reader:
            if row[0] != "":
                cred_profiles_chars['revocation'][row[0]] = {}
                cred_profiles_chars['revocation'][row[0]].update({'observability':row[9]})
                cred_profiles_chars['revocation'][row[0]].update({'traceability':row[10]})
                cred_profiles_chars['revocation'][row[0]].update({'scalability':row[11]})
                cred_profiles_chars['revocation'][row[0]].update({'offlineFriendliness':row[12]})
        csv_file.close()
    with open('./data/signature.csv', 'r') as csv_file:
        next(csv_file)
        next(csv_file)
        reader = csv.reader(csv_file)
        cred_profiles_chars['signature'] = {}
        for row in reader:
            if row[0] != "":
                cred_profiles_chars['signature'][row[0]] = {}
                cred_profiles_chars['signature'][row[0]].update({'hardwareSupport':row[8]})
                cred_profiles_chars['signature'][row[0]].update({'verifierUnlinkability':row[9]})
                cred_profiles_chars['signature'][row[0]].update({'postQuantumSecure':row[11]})
        csv_file.close()
    return cred_profiles_chars

def check_emptiness(wallets: dict) -> dict:
    """
        param wallets (dict): the dictionary containing wallets and their characteristics
        returns: the same dictionary, where all values are present
    """
    for wallet in wallets:
        for key in keys:
            if not wallets[wallet].get(key):
                wallets[wallet].update({key: "tbd"})
    return wallets
    

def main():
    cred_profiles = create_cred_profile_dict()
    # Write to JSON file
    json_file_cred = open("cred_profile.json", 'w')
    json_file_cred.write(json.dumps(cred_profiles, indent=4))
    json_file_cred.close()

    wallets = create_wallet_dict_old_part(cred_profiles=cred_profiles)

    wallets = create_wallet_dict_new_part(json_dict=wallets, cred_profiles=cred_profiles)

    wallets = extend_wallet_dict(wallets=wallets)

    print(f'{len(wallets.keys())} wallets are written')
    
    wallets = check_emptiness(wallets)

    # Sort on wallet name
    wallets_sorted = collections.OrderedDict(sorted(wallets.items()))
    wallet_list = []
    for wallet in wallets_sorted:
        wallet_list += [wallets_sorted[wallet]]
    # Export to JSON file
    json_file_wallets = open("wallets.json", 'w')
    json_file_wallets.write(json.dumps(wallet_list, indent=4))
    json_file_wallets.close()


if __name__ == "__main__":
    main()