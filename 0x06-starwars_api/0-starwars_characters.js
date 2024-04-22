#!/usr/bin/node
/*
a script that prints all characters of a Star Wars movie:
The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name per line in the same order as the “characters” list in the /films/ endpoint
You must use the Star wars API
You must use the request module
*/
const request = require('request');

// COMMAND LINE ARGUMENTS
const movieId = process.argv[2];
if (!movieId) {
    console.error('Please provide a movie ID as the first argument.');
    process.exit(1);
}

// API URL
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch character data
const fetchCharacterData = characterUrl => {
    return new Promise((resolve, reject) => {
        request.get(characterUrl, (error, response, body) => {
            if (error) {
                reject(error);
            } else {
                const character = JSON.parse(body);
                resolve(character.name);
            }
        });
    });
};

// Main function to fetch movie data and character names
const fetchMovieData = () => {
    request.get(url, (error, response, body) => {
        if (error) {
            console.error('Error fetching movie data:', error);
            return;
        }
        
        const film = JSON.parse(body);
        // console.log("Characters in the movie:");
        
        // Iterate over character URLs
        film.characters.forEach(async characterUrl => {
            try {
                const characterName = await fetchCharacterData(characterUrl);
                console.log(characterName);
            } catch (error) {
                console.error('Error fetching character data:', error);
            }
        });
    });
};

// Call the main function
fetchMovieData();