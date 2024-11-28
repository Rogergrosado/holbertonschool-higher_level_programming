document.addEventListener('DOMContentLoaded', (event) => {
  let addItem = document.querySelector('#add_item');
  let myList = document.querySelector('.my_list');

  addItem.addEventListener('click', () => {
      let newLi = document.createElement('li');
      newLi.textContent = 'Item';
      myList.appendChild(newLi);
  });
});
