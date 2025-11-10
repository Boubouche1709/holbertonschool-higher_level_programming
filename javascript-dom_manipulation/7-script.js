const listMovies = document.querySelector('#list_movies');
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(response => response.json())
  .then(data => {
    const films = data.results;
    films.forEach(film => {
      const li = document.createElement('li');
      li.textContentContent = film.tittle;
      listMovies.appendChild(li);
    });
  });
