#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
    console.log('Usage: ./script.js <movie_id>');
    process.exit(1);
}

const filmID = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmID}`;

function makeURLReq(url) {
    return new Promise((resolve, reject) => {
        request(url, (error, response, body) => {
            if (error) {
                reject(error);
            } else {
                try {
                    const charactJSON = JSON.parse(body);
                    resolve(charactJSON.name);
                } catch (e) {
                    reject(e);
                }
            }
        });
    });
}

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error('Error fetching film data:', error);
        return;
    }

    try {
        const json = JSON.parse(body);
        const characters = json.characters;

        // Map characters to promises of fetching their names
        const characterPromises = characters.map(character => makeURLReq(character));

        // Resolve all promises concurrently
        Promise.all(characterPromises)
            .then(characterNames => {
                characterNames.forEach(name => console.log(name));
            })
            .catch(err => {
                console.error('Error fetching character data:', err);
            });

    } catch (e) {
        console.error('Error parsing film data:', e);
    }
});
