const clic = document.querySelector('#update_header');
clic.addEventListener('click', function () {
  const header = document.querySelector('header');
  header.textContent = 'New Header!!!';
});
