const clic = document.querySelector('#red_header');
clic.addEventListener('click', function () {
  const header = document.querySelector('header');
  header.classList.add('red');
});
