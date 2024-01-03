#!/usr/bin/node

const request = require('request');
const filmId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

request(url, (error, response, body) => {
  if (!error) {
    const characters = JSON.parse(body).characters;
      for (const charUrl of characters) {
        request(charUrl, (error, response, body) => {
          if (!error) {
            console.log(JSON.parse(body).name);
	  }
        });
      }
  }
});
