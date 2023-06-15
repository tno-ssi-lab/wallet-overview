# Overview of SSI Wallets and their Characteristics

This is the repository for TNO's overview of SSI wallets. The actual overview can be found [here](https://tno-ssi-lab.github.io/wallet-overview/).

## Sources
The information is aggregated from input from wallet vendors (via a [form](https://docs.google.com/forms/d/e/1FAIpQLSdM1h1n-LtbaB5ug8YEnT7pfa__2Y4ehhNobdsPdNMA63c4YQ/viewform?usp=sf_link?hl=en)), TNO internal overviews and our [IIW/RWOT work on credential profiles](https://github.com/vcstuff/credential-profile-comparison).

## Goal 
The overview serves the following purposes:
- Issuers, verifiers and holders can use it to make a choice in wallet, based on their preferred characteristics.
- It offers insight in which wallets are interoperable with each other.
- It allows us to prioritise for which wallet a connector to our [TNO EASSI gateway](https://eassi.ssi-lab.nl/) should be developed.

See [below](#characteristics) for a description of the characteristics included.

## How to contribute
You can contribute to the overview by:
- Filling in the [form](https://docs.google.com/forms/d/e/1FAIpQLSdM1h1n-LtbaB5ug8YEnT7pfa__2Y4ehhNobdsPdNMA63c4YQ/viewform?usp=sf_link?hl=en) if you are a wallet vendor.
- Sharing this repository in your network.
- Directly contributing to the overview through forking. See [below](#modifying-json) on how to do this concretely.

<h3 id="modifying-json">Modifying <code>wallets.json</code></h3>

To update the overview, you just have to update [wallets.json](wallets.json). Search for your wallet and update the characteristic(s) you want to change. If you want to add a new wallet, add and fill in the [format](#format) to `wallets.json`.

Note that you can't add new types of characteristics. If you feel that a new characteristic should be added, create an [issue](https://github.com/tno-ssi-lab/wallet-overview/issues/new).

After your merge request has been accepted, you will see the updated version of the overview on the [overview page](https://tno-ssi-lab.github.io/wallet-overview/). If you want to see locally what the modified HTML looks like, open a terminal in your local copy of the repository and type `python -m http.server 8080`, then you should see the modified overview [here](http://localhost:8080/).

<h3 id="format">Format</h3>

If you want to add/change the logo, add the logo to [static/](static/) and change `"logo": "static/<your-wallet>.png"`.

Descriptions of fields can be seen on the [overview page](https://tno-ssi-lab.github.io/wallet-overview/) or in [script.js](script.js).

```json
{
    "logo": "",
    "name": "",
    "company": "",
    "scope": "",
    "users": "",
    "deployment": "",
    "isHolderWallet": "",
    "isIssuerAgent": "",
    "isVerifierAgent": "",
    "connectionTypes": "",
    "peer2peerProtocols": "",
    "credExchangeProtocol": "",
    "selectiveDisclosure": "",
    "predicates": "",
    "identifierHolder": "",
    "identifierIssuer": "",
    "revocationAlgorithm": "",
    "verifierUnlinkability": "",
    "observability": "",
    "keyHistoryHolder": "",
    "keyRotationHolder": "",
    "keyHistoryIssuer": "",
    "keyRotationIssuer": "",
    "transferability": "",
    "credentialFormat": "",
    "encodingScheme": "",
    "signatureAlgorithm": "",
    "cryptoAgility": "",
    "hardwareSupport": "",
    "postQuantumSecure": "",
    "blockchainUsed": "",
    "blockchainType": "",
    "blockchainPurpose": "",
    "deepLinking": "",
    "offlineFriendly": "",
    "support": "",
    "license": "",
    "openSource": "",
    "sourceCode": "",
    "api": "",
    "eassi": "",
    "ebsi": "",
    "website": "",
    "appstore": "",
    "googlePlay": "",
    "webApp": "",
    "email": "",
    "supportEmail": ""
}```

<h3 id="characteristics">Characteristics</h3>

The characteristics included are listed [above](#format). Here we will give a short description of characteristics that are not obvious from their name.

**connectionTypes** list the types of connections the wallet can handle, i.e. either direct communication via QR-codes, bluetooth, etc. versus connection-based. The latter uses a persistent connection with another party, that is reused for new interactions.

**cryptoAgility** is whether the credential format is capable of working with various signature algorithms.

**deepLinking** allows for sending the user to the wallet app instead of to a website, such that the user can have a mobile-only workflow.

**eassi** is whether the wallet connected to our [TNO EASSI gateway](https://eassi.ssi-lab.nl/).

**hardwareSupport** is about whether the signature algorithm(s) is implemented in a commonly used cryptographic hardware modules, such as HSMs, TEEs, etc.

**keyHistory** is supported if it is possible to retain and obtain the history of keys related to a certain identifier.

**keyRotation** is supported if the key referred to in a credential can be replaced by a new key.

**observability** is about whether the verifier can observe the revocation status of the credential beyond the presentation.

**offlineFriendly** is about whether the revocation algorithm allows for offline checking the status of the credential.

**postQuantumSecure** depends on the signature algorithm and indicates whether the signature algorithm could resist attacks by a quantum computer.

**predicates** are attestations about the information without revealing the actual information. This characteristic indicates whether the credential format can produce general-purpose predicates.

**selectiveDisclosure** is about whether the credential format can present a subset of the claims in the credentials.

**verifierUnlinkability** is when the verifier cannot correlate multiple presentation exchanges with the same holder, i.e. the verifier does not know they are communicating with the same holder again. This depends on the signature algorithm and the holder's identifier.

