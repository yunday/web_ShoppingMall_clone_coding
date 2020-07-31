const toggleBtn = document.querySelector('.navbar_toogleBtn');
const menu = document.querySelector('.navbar_menu');
const icons = document.querySelector('.navbar_icons');

toggleBtn.addEventListener('click', ()=>{
    menu.classList.toggle('active'); // active가 있다면 빼고 없으면 넣고
    icons.classList.toggle('active');
});