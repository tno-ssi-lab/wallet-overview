const columns = {
  logo: '',
  name: '',
  company: '',
  openSource: '',
  eassi: '',
  credentialFormat: '',
  encodingScheme: '',
  signatureAlgorithm: '',
  identifierHolder: '',
  identifierIssuer: '',
  revocationAlgorithm: '',
  peer2peerProtocols: '',
  blockchainUsed: '',
  blockchainType: 'class="td-wrap"',
  blockchainPurpose: 'class="td-wrap"',
  credExchangeProtocol: '',
  connectionTypes: '',
  deepLinking: '',
  offlineFriendly: '',
  selectiveDisclosure: '',
  predicates: '',
  verifierUnlinkability: '',
  cryptoAgility: '',
  postQuantumSecure: '',
}

fetch("wallets.json")
.then(function(response){
	return response.json();
})
.then(function(wallets){
	let placeholder = document.querySelector("#data-output");
	let out = "";
	for(let wallet of wallets){
		out += `<tr><td><img src='${wallet.logo}'></td>`
		for (let param in columns) {
			out += `<td ${columns[param]}>${wallet[param]}</td>`
		}
		out += '</tr>\n';
	}

	placeholder.innerHTML = out;
});
