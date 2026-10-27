fetch('https://swapi-api.hbtn.io/api/films/?format=json')
  .then(function (response) {
    return response.json();
  })
  .then(function (datas) {
    const list = document.querySelector('#list_movies');
    datas.results.forEach(function (movie) {
      const item = document.createElement('li');
      item.textContent = movie.title;
      list.appendChild(item);
    });
  });
