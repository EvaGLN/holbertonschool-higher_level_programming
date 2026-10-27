const clic = document.querySelector('#add_item');
clic.addEventListener('click', function () {
  const list = document.querySelector('ul.my_list');
  const newelement = document.createElement('li');
  newelement.textContent = 'Item';
  list.appendChild(newelement);
});
