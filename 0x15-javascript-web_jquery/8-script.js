const url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
$.getJSON(url, function (data) {
	const films = data.results;
	$.each(films, function (i, film) {
		$('UL#list_movies').append(`<li>${film.title}</li>`);
	});
});
