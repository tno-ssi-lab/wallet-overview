
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
				<td>${wallet.name}</td>	
				<td>${wallet.company}</td>
				<td>${wallet.openSource}</td>
				<td>${wallet.credentialFormat}</td>
				<td>${wallet.encodingScheme}</td>
				<td>${wallet.signatureAlgorithm}</td>
				<td>${wallet.identifierHolder}</td>
				<td>${wallet.identifierIssuer}</td>
				<td>${wallet.revocationAlgorithm}</td>
				<td>${wallet.peer2peerProtocols}</td>
				<td>${wallet.blockchain.used}</td>
				<td>tbc</td>
				<td>tbc</td>
				<td>${wallet.credExchangeProtocol}</td>
				<td>${wallet.connectionTypes}</td>
				<td>${wallet.deepLinking}</td>
				<td>${wallet.offlineFriendly}</td>
				<td>${wallet.selectiveDisclosure}</td>
				<td>${wallet.predicates}</td>
				<td>${wallet.verifierUnlinkability}</td>
				<td>${wallet.cryptoAgility}</td>
				<td>${wallet.eassi}</td>
			</tr>
		`;
	}

	placeholder.innerHTML = out;
});
				// <td>${wallet.blockchain.type}</td>
				// <td>${wallet.blockchain.purpose}</td>
				// needs wrapping!
				// <td style="white-space: nowrap; text-overflow:ellipsis; overflow: hidden; max-width:200px;">${wallet.encodingScheme}</td>