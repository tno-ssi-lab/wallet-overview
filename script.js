const columns = {
	logo: {header: 'Logo', title: 'The logo of the wallet.', type: 'img', class: ''},
	name: {header: 'Wallet', title: 'The name of the wallet.'},
	company: {header: 'Company', title: 'The developer of the wallet.'},
	scope: {header: 'Scope', title: 'General-purpose or domain-specific (and the domain)', class: 'td-wrap'},
	users: {header: 'Target users', title: 'Targeted at individuals, companies, developers, ...'},
	deployment: {header: 'Deployment', title: 'How is the wallet deployed? E.g. mobile, SaaS, self-hosted, ...'},
	// isHolderWallet: {header: 'Holder Wallet', title: 'Can the wallet hold and present verifiable credentials?'},
	// isIssuerAgent: {header: 'Issuer Agent', title: 'Can the wallet issue verifiable credentials?'},
	// isVerifierAgent: {header: 'Verifier Agent', title: 'Can the wallet verify verifiable credentials?'},
	connectionTypes: {header: 'Connection Types', title: 'Types of connections the wallet can handle, i.e. either direct communication via QR-codes, bluetooth, etc. versus connection-based.'},
	peer2peerProtocols: {header: 'Peer-to-Peer Protocols', title: 'The ToIP level 2 protocol for communication between peers.'},
	credExchangeProtocol: {header: 'Credential Exchange Protocols', title: 'The ToIP level 3 protocol for the exchange of credentials.'},
	selectiveDisclosure: {header: 'Selective Disclosure', title: 'Can holders present only selected attributes from their credentials?'},
	predicates: {header: 'Predicates', title: 'Can holders present predicates, e.g. older than 18?'},
	identifierHolder: {header: 'Holder Identifier', title: 'The type of identifier used to identify the holder.'},
	identifierIssuer: {header: 'Issuer Identifier', title: 'The type of identifier used to identify the issuer.'},
	revocationAlgorithm: {header: 'Revocation Algorithms', title: 'The revocation mechanism use to revoke credentials.'},
	verifierUnlinkability: {header: 'Verifier Unlinkability', title: 'Whether the verifier can link multiple presentation by the same holder.'},
	observability: {header: 'Observability', title: 'Can the verifier observe the revocation status of the credential beyond the presentation?'},
	keyHistoryHolder: {header: 'Key History for Holder', title: 'Is it possible to retain and obtain the history of keys related to a certain identifier?'},
	keyRotationHolder: {header: 'Key Rotation for Holder', title: 'Can the key referred to in a credential can be replaced by a new key?'},
	keyHistoryIssuer: {header: 'Key History for Issuer', title: 'Is it possible to retain and obtain the history of keys related to a certain identifier?'},
	keyRotationIssuer: {header: 'Key Rotation for Issuer', title: 'Can the key referred to in a credential can be replaced by a new key?'},
	transferability: {header: 'Transferability', title: 'Can credentials be exported and imported into another wallet?'},
	credentialFormat: {header: 'Credential Formats', title: 'The credential format used.'},
	encodingScheme: {header: 'Encoding Schemes', title: 'The encoding scheme used.'},
	signatureAlgorithm: {header: 'Signature Algorithms', title: 'The signature algorithms supported by the wallet.'},
	cryptoAgility: {header: 'Crypto Agility', title: 'Is the credential format capable of working with various signature algorithms?'},
	hardwareSupport: {header: 'Hardware Support', title: 'At least one signature algorithm is implemented in a commonly used cryptographic hardware module, such as HSMs, TEEs, etc.'},
	postQuantumSecure: {header: 'Post-Quantum Secure', title: 'Signatures cannot be cracked using quantum computers?'},
	blockchainUsed: {header: 'Blockchain Used', title: 'Uses blockchain (always, optionally, never)?'},
	blockchainType: {header: 'Blockchain Type', title: 'What kind of blockchain can be used?', class: 'td-wrap'},
	blockchainPurpose: {header: 'Blockchain Purpose', title: 'The purpose of the use of the blockchain.', class: 'td-wrap'},
	deepLinking: {header: 'Deep Linking', title: 'The user can be sent to the wallet app instead of to a website, such that the user can have a mobile-only workflow. For web-based wallets, ability to link directly to a specific task like credential offer.'},
	offlineFriendly: {header: 'Offline Friendliness', title: 'Can be used without Internet access?'},
	support: {header: 'Support', title: 'What kind of support is available (commercial, community, developer)'},
	license: {header: 'License', title: 'Type of licensing (pricing model and price, open-source license)'},
	openSource: {header: 'Open Source', title: 'Source code is available?'},
	sourceCode: {header: 'Source code', title: 'Location of the source code', type: 'link'},
	api: {header: 'API/SDK', title: 'Functionality can be enhanced using an API or an SDK'},
	eassi: {header: 'Connected to TNO EASSI', title: 'Is the wallet connected to the TNO EASSI gateway (https://eassi.ssi-lab.nl/)?'},
	ebsi: {header: 'EBSI conformant', title: 'Has passed EBSI conformance testing (https://ec.europa.eu/digital-building-blocks/wikis/display/EBSI/Conformant+wallets)'},
	website: {header: 'Website', title: 'Site for information about the wallet', type: 'link'},
	appstore: {header: 'App Store', title: 'Download link in Apple\'s App Store', type: 'link'},
	googlePlay: {header: 'Google Play', title: 'Download link in Google Play store', type: 'link'},
	webApp: {header: 'Web app', title: 'Launch URL for the web app', type: 'link'},
	email: {header: 'Contact e-mail', title: 'Address for general and commercial enquiries', type: 'mail'},
	supportEmail: {header: 'Support e-mail', title: 'Address for support requests', type: 'mail'},
}
/* the rows below display a JSON template with the keys in alphabetical order – e.g., for updating README.md */
// const template = {}
// Object.keys(columns).map(key => {template[key] = ''})
// console.log(JSON.stringify(template, null, 4))

// let headerPlaceholder = document.querySelector("#table-headers")
// let ths = `<tr onclick="this.classList.toggle('verbose')"><th>#</th>`
// let count = 1
// for (let col in columns) {
// 	ths += `<th title="${columns[col].title}">${columns[col].header}`
// 	if (columns[col].type != 'img') {
// 		ths += ` <button class="btn" onclick="arguments[0]?.stopPropagation(); sortTable(${count})"><i class="fa-solid fa-sort"></i></button>`
// 	}
// 	ths += `</th>`
// 	count++
// }
// ths += '</tr>\n'
// headerPlaceholder.innerHTML = ths

// fetch("wallets.json")
// .then(function(response){
// 	return response.json()
// })
// .then(function(wallets){
// let placeholder = document.querySelector("#data-output")
// let out = ""
// let rowCount = 0
// for(let wallet of wallets){
// 	out += `<tr><td>${++rowCount}</td>`
// 	for (let param in columns) {
// 		if (wallet[param] === undefined || wallet[param] === '' || wallet[param] === '-') {
// 			out += '<td>-</td>'
// 			continue
// 		}
// 		switch (columns[param].type) {
// 			case 'img':
// 				out += `<td><img src='${wallet[param]}'></td>`
// 				break
// 			case 'link':
// 			out += `<td><a href="${wallet[param]}">${wallet[param]}</a></td>`
// 				break;
// 			case 'mail':
// 				out += `<td><a href="mailto:${wallet[param]}">${wallet[param]}</a></td>`
// 				break;
// 			default:
// 			out += `<td class="${columns[param].class}">${wallet[param]}</td>`
// 		}
// 	}
// 	out += '</tr>\n'
// }

// placeholder.innerHTML = out
// })

fetch("wallets.json")
.then(function(response){
	return response.json();
})
.then(function(wallets){
	let placeholder = document.querySelector("#data-output");
	let out = "";
	for(let wallet of wallets){
		out += `
			<tr>
				<td><img src='${wallet.logo}'></td>
				<td><a href="${wallet.website}">${wallet.name}</a></td>	
				<td>${wallet.company}</td>
				<td>${wallet.scope}</td>
				<td>${wallet.deployment}</td>
				<td>${wallet.organizationalWallet}</td>
				<td>${wallet.openSource}</td>
				<td>${wallet.download}</td>
				<td>${wallet.support}</td>

				<td>${wallet.credentialFormat}</td>
				<td>${wallet.encodingScheme}</td>
				<td>${wallet.signatureAlgorithm}</td>
				<td>${wallet.identifierHolder}</td>
				<td>${wallet.identifierIssuer}</td>
				<td>${wallet.revocationAlgorithm}</td>
				<td>${wallet.peer2peerProtocols}</td>
				<td>${wallet.credExchangeProtocol}</td>
				<td>${wallet.blockchain.used}</td>
				<td class="td-wrap">${wallet.blockchain.type}</td>
				<td class="td-wrap">${wallet.blockchain.purpose}</td>
				
				<td>${wallet.connectionTypes}</td>
				<td>${wallet.deepLinking}</td>
				<td>${wallet.offlineFriendly}</td>
				<td>${wallet.keyHistoryHolder}</td>
				<td>${wallet.keyHistoryIssuer}</td>
				<td>${wallet.portability}</td>

				<td>${wallet.selectiveDisclosure}</td>
				<td>${wallet.predicates}</td>
				<td>${wallet.verifierUnlinkability}</td>
				<td>${wallet.observability}</td>

				<td>${wallet.cryptoAgility}</td>
				<td>${wallet.postQuantumSecure}</td>
				<td>${wallet.keyRotationHolder}</td>
				<td>${wallet.keyRotationIssuer}</td>

				<td>${wallet.eassi}</td>
				<td>${wallet.ebsi}</td>
				<td>${wallet.aip}</td>
				<td>${wallet.ddip}</td>
				<td>${wallet.iso18013}</td>
				
			</tr>
		`;
	}

	placeholder.innerHTML = out;
});

// <td><a href="${wallet.website}"><i class="fas fa-code";></i></a></td>