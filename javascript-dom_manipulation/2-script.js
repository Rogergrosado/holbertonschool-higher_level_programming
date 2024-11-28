document.addEventListener('DOMContentLoaded', (event) => {
  let redHeader = document.querySelector('#red_header');
  let header = document.querySelector('header');

  redHeader.addEventListener('click', () => {
      header.classList.add('red');
  });
});
