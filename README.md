# Overview of SSI Wallets and their Characteristics

This is the repository for TNO's overview of SSI wallets. The actual overview can be found [here](https://tno-ssi-lab.github.io/wallet-overview/).

## Sources
The information is aggregated from input from wallet vendors (via a [form](https://docs.google.com/forms/d/e/1FAIpQLSdM1h1n-LtbaB5ug8YEnT7pfa__2Y4ehhNobdsPdNMA63c4YQ/viewform?usp=sf_link?hl=en)), TNO internal overviews and our [IIW/RWOT work on credential profiles](https://github.com/vcstuff/credential-profile-comparison).

## Goal 
The overview serves the following purposes:
- Issuers, verifiers and holders can use it to make a choice in wallet, based on their preferred characteristics.
- It offers insight in which wallets are interoperable with each other.
- It allows us to prioritise for which wallet a connector to our [TNO EASSI gateway](https://eassi.ssi-lab.nl/) should be developed.

## How to contribute
You can contribute to the overview by:
- Filling in the [form](https://docs.google.com/forms/d/e/1FAIpQLSdM1h1n-LtbaB5ug8YEnT7pfa__2Y4ehhNobdsPdNMA63c4YQ/viewform?usp=sf_link?hl=en) if you are a wallet vendor.
- Sharing this repository in your network.
- Directly contributing to the overview through forking. See [below](#modifying-json) on how to do this concretely.

<h3 id="modifying-json">Modifying <code>wallets.json </code></h3>

To update the overview, you just have to update `wallets.json`. Search for your wallet and update the characteristic(s) you want to change. If you want to add a new wallet, add and fill in the [format](#format) to `wallets.json`.

Note that you can't add new types of characteristics. If you feel that a new characteristic should be added, create an [issue](https://github.com/tno-ssi-lab/wallet-overview/issues/new).

After your merge request has been accepted, you will see the updated version of the overview on the [overview page](https://tno-ssi-lab.github.io/wallet-overview/). If you want to see locally what the modified HTML looks like, open a terminal in your local copy of the repository and type `python -m http.server 8080`, then you should see the modified overview [here](http://localhost:8080/).

<h3 id="format">Format</h3>
If you want to add/change the logo, add the logo to `wallet-overview/static/` and change `"logo": "static/<your-wallet>.png"`.

    {
        "blockchain": {
            "used": "",
            "type": "",
            "purpose": ""
        },
        "company": "",
        "connectionTypes": "",
        "credExchangeProtocol": "",
        "credentialFormat": "",
        "cryptoAgility": "",
        "deepLinking": "",
        "eassi": "",
        "encodingScheme": "",
        "hardwareSupport": "",
        "identifierHolder": "",
        "identifierIssuer": "",
        "keyHistoryHolder": "",
        "keyHistoryIssuer": "",
        "keyRotationHolder": "",
        "keyRotationIssuer": "",
        "logo": "",
        "name": "",
        "observability": "",
        "offlineFriendly": "",
        "openSource": "",
        "peer2peerProtocols": "",
        "postQuantumSecure": "",
        "predicates": "",
        "revocationAlgorithm": "",
        "selectiveDisclosure": "",
        "signatureAlgorithm": "",
        "verifierUnlinkability": ""
    },
