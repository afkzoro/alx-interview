#!/usr/bin/node
const axios = require('axios');

// Function to fetch character names from the Star Wars API
async function getCharacterNames (movieId) {
  try {
    const response = await axios.get(`https://swapi.dev/api/films/${movieId}/`);
    const { characters } = response.data;

    const characterNames = await Promise.all(characters.map(async (characterUrl) => {
      const characterResponse = await axios.get(characterUrl);
      return characterResponse.data.name;
    }));

    return characterNames;
  } catch (error) {
    throw new Error('Failed to fetch character names.');
  }
}

// Main function
async function main () {
  try {
    const movieId = process.argv[2];
    if (!movieId) {
      console.error('Usage: node star_wars_characters.js <movieId>');
      process.exit(1);
    }

    const characterNames = await getCharacterNames(movieId);

    characterNames.forEach((name) => {
      console.log(name);
    });
  } catch (error) {
    console.error(error.message);
    process.exit(1);
  }
}

main();
