#!/usr/bin/node
/* eslint-disable semi */
const request = require('request');

// Function to fetch character names from the Star Wars API
function getCharacterNames (movieId) {
  return new Promise((resolve, reject) => {
    const url = `https://swapi.dev/api/films/${movieId}/`;

    request.get(url, (error, response, body) => {
      if (error) {
        reject(new Error('Failed to fetch movie details.'));
        return;
      }

      if (response.statusCode !== 200) {
        reject(new Error('Failed to fetch movie details. Invalid response.'));
        return;
      }

      try {
        const data = JSON.parse(body);
        const characterUrls = data.characters;

        // Function to fetch character name from character URL
        const fetchCharacterName = (characterUrl) => {
          return new Promise((resolve, reject) => {
            request.get(characterUrl, (error, response, body) => {
              if (error) {
                reject(new Error('Failed to fetch character details.'));
                return;
              }

              if (response.statusCode !== 200) {
                reject(new Error('Failed to fetch character details. Invalid response.'));
                return;
              }

              const characterData = JSON.parse(body);
              resolve(characterData.name);
            });
          });
        };

        // Fetch character names asynchronously
        const fetchPromises = characterUrls.map((characterUrl) => fetchCharacterName(characterUrl));

        Promise.all(fetchPromises)
          .then((names) => {
            resolve(names);
          })
          .catch((error) => {
            reject(new Error('Failed to fetch character names.'));
          });
      } catch (error) {
        reject(new Error('Failed to parse response data.'));
      }
    });
  });
}

// Main function
function main () {
  const movieId = process.argv[2];
  if (!movieId) {
    console.error('Usage: node ./0-starwars_characters.js <movieId>');
    process.exit(1);
  }

  getCharacterNames(movieId)
    .then((characterNames) => {
      characterNames.forEach((name) => {
        console.log(name);
      });
    })
    .catch((error) => {
      console.error(error.message);
      process.exit(1);
    });
}

main();
