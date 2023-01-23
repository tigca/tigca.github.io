const page = document.querySelector('.page')
const themeButton = document.querySelector('.btn-theme')
const bodyTheme = document.querySelector('.dark-theme')
// бургер меню
const burgerMenu = document.querySelector('.header-menu-icon')
const headerLink = document.querySelectorAll('.header__item')
const headerMenu = document.querySelector('.header__nav')

const slider = document.getElementById("carouselExampleDark")
themeButton.onclick = function() {
    page.classList.toggle('light-theme')
    page.classList.toggle('dark-theme')

    if (bodyTheme.classList.contains('light-theme')) document.querySelector(".git").src="assets/img/GH.png"
    else document.querySelector(".git").src="assets/img/GitHub-Mark-Light-120px-plus.png"
};
if(burgerMenu){
    burgerMenu.addEventListener('click',  () => {
        burgerMenu.classList.toggle('active')
        headerMenu.classList.toggle('active')
        page.classList.toggle('lock')
        if(!page.classList.contains("lock")) slider.style.display = "block"
        else slider.style.display = "none"

    });
}

for (let i = 0; i < headerLink.length; i++){
    headerLink[i].addEventListener('click', () => {
        console.log('123')
        burgerMenu.classList.remove('active')
        headerMenu.classList.remove('active')
        page.classList.remove('lock')
        slider.style.display = "block"
    });
}
let popoverTriggerList = [].slice.call(document.querySelectorAll('[data-toggle="popover"]'))
popoverTriggerList.map(function (popoverTiger){
   return new bootstrap.Popover(popoverTiger)
});
// translate
let rus = {
    title: 'Будущий Веб-разработчик',
    theme: 'Тема',
    advantages: 'Достижения',
    skills: 'Умения',
    about: 'Обо мне',
    member: 'Участник',
    сontributer: 'Контрибьютер',
    hit:'написать мне',
    help:'- я помогу Вам',
    bugs:'Если Вы нашли какие-то баги, то Вы можете',
    studying: '<span class="red">Инструменты</span> & <span class="red">Языки</span>, которые я учу',
    web: 'Веб-разработка',
    programming: 'Языки программирования',
    tools: 'Инструменты',
    future: 'В ближайшем будущем я планирую изучить <span class="red">инструменты</span> / <span class="red">языки</span> такие как',
    frameworks: 'Фреймворки',
    libraries: 'Библиотеки',
    aboutInf: 'Здесь некоторая информация <span class="red">обо мне</span> <br> <span class="red">Например,</span> мои сертификаты',
    notFound: 'Страница не найдена',
    goBack: 'Вернуться',
    lang: 'Язык'
};

let eng = {
    title: 'I\'m Web dev in the future',
    theme: 'Theme',
    advantages: 'Advantages',
    skills: 'Skills',
    about: 'About me',
    member: 'Member of',
    сontributer: 'Contributer',
    hit:'hit me up',
    help:'- I\'ll help you',
    bugs:'If you found some bugs you can',
    studying: '<span class="red">Tools</span> & <span class="red">Languages</span> I\'ve been studying',
    web: 'Web-Stack',
    programming: 'Programming languages',
    tools: 'Tools',
    future: 'In the near future I plan to learn <span class="red">tools</span> / <span class="red">languages</span> such as',
    frameworks: 'Web-Frameworks',
    libraries: 'Libraries',
    aboutInf: 'Here is some information <span class="red">about me</span> <br> <span class="red">For example</span> my certificates',
    notFound: 'Page not found',
    goBack: 'Go back',
    lang: 'Lang'
};


document.querySelector('.btn-language').onclick = () => changeLanguage()
function changeLanguage(){
    const language = page.classList.toggle('eng') ? eng : rus;
    document.querySelectorAll('[text]').forEach(el => {
        el.innerHTML = language[el.getAttribute('text')]
    })
}
