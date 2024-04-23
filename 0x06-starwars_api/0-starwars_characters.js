#!/usr/bin/node
/*
a script that prints all characters of a Star Wars movie:
The first positional argument passed is the Movie ID - example: 3 = “Return of the Jedi”
Display one character name per line in the same order as the “characters” list in the /films/ endpoint
You must use the Star wars API
You must use the request module
*/
const https = require('https');

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
    https.get(characterUrl, (response) => {
      let data = '';

      // A chunk of data has been received.
      response.on('data', (chunk) => {
        data += chunk;
      });

      // The whole response has been received.
      response.on('end', () => {
        const character = JSON.parse(data);
        resolve(character.name);
      });
    }).on('error', (error) => {
      reject(error);
    });
  });
};

// Main function to fetch movie data and character names
const fetchMovieData = () => {
  https.get(url, (response) => {
    let data = '';

    // A chunk of data has been received.
    response.on('data', (chunk) => {
      data += chunk;
    });

    // The whole response has been received.
    response.on('end', () => {
      const film = JSON.parse(data);

      // Array to store promises for character data
      const characterPromises = film.characters.map(characterUrl => fetchCharacterData(characterUrl));

      // Wait for all character data promises to resolve
      Promise.all(characterPromises)
        .then(characterNames => {
          // Print character names in correct order
          characterNames.forEach(name => console.log(name));
        })
        .catch(error => {
          console.error('Error fetching character data:', error);
        });
    });
  }).on('error', (error) => {
    console.error('Error fetching movie data:', error);
  });
};

// Call the main function
fetchMovieData();
