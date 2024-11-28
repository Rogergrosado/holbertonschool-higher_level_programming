document.addEventListener('DOMContentLoaded', (event) => {
  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
      .then(response => response.json())
      .then(data => {
          let character = document.querySelector('#character');
          character.textContent = data.name;
      })
      .catch(error => console.error(error));
});
