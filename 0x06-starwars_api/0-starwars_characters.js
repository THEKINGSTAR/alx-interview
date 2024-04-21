#!/usr/bin/node
/*
a script that prints all characters of a Star Wars movie:
The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name per line in the same order as the “characters” list in the /films/ endpoint
You must use the Star wars API
You must use the request module
*/
//COMMAND LINE ARGUMENTS
movieId = process.argv[2];
if (!movieId){
	console.error('Please provide a movie ID as the first argument.');
	process.exit(1);
}
//HTTPS URL
const url = 'https://swapi-api.alx-tools.com/api/films/${movieId}';

// const https = require("https");
https.gets(url, resp => {
let data = "";

resp.on("data", chunk => {
	data += chunk;
	});

resp.on("end", () => {
	let url = JSON.parse(data).message;
	console.log(url);
	});
})
.on("error", err => {
		console.log("Error: " + err.message);
});


// handling API response
const films = JSON.parse(data);
const characterUrls = films.characters;


// requests for characters
characterUrls.forEach(characterUrl => {
https.get(characterUrl, characterResp => {
	let characterData = '';

	characterResp.on('data', chunk => {
		characterData += chunk;
	});
	}).on("error", err => {
		console.log("Error: " + err.message);
	});
});
