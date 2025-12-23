//function toggleMenu() {
//let menuClose = document.querySelector(".menu-close");
//let menuOpen = document.querySelector(".menu-open");
//let linkContainer = document.querySelector(".link-container");

//menuOpen.classList.toggle("hide-menu");
//menuClose.classList.toggle("show-x");
//linkContainer.classList.toggle("show-links");
//}

function sleep(ms) {
  return new Promise((resolve) => setTimeout(resolve, ms));
}

let index = 0;

const bibleVerses = [
  `<p style=''><mark>Ze względu na Syjon nie będę milczał</mark></p> <p style=''> i ze względu na Jerozolimę nie spocznę</p>`,
  `<p style='font-size: 3vw;'>Nie możemy milczeć wobec antyseminyzmu</p> <p><mark>Stańmy po stronie prawdy</mark></p>`,
  `<p><mark>Wy, którzy wspominacie PANA, nie milczcie;</mark> I nie dajcie mu odpoczynku, dopóki nie utwierdzi i dopóki nie uczyni Jerozolimy chwałą na ziemi.</p>`,
  `<p>I tak cały Izrael będzie zbawiony, jak jest napisane: Przyjdzie z Syjonu wybawiciel i odwróci bezbożność od Jakuba.</p>`,
];

let bibleVerseContainer = document.querySelector(".bible-verse");

showVerse();

function changeBibleVerseForward() {
  index++;
  if (index > 3) {
    index = 0;
  }
  showVerse();
}

function changeBibleVerseBackward() {
  index -= 1;
  if (index < 0) {
    index = 3;
  }
  showVerse();
}

async function showVerse() {
  const imgSource = document.querySelector(".slide-img");

  imgSource.classList.add("blend-out-class");
  bibleVerseContainer.classList.add("blend-out-class");
  await sleep(150);

  bibleVerseContainer.innerHTML = `${bibleVerses[index]}`;
  imgSource.src = `${slideShowImgs[index]}`;

  imgSource.classList.remove("blend-out-class");
  bibleVerseContainer.classList.remove("blend-out-class");
  imgSource.classList.add("blend-half-in-class");
  bibleVerseContainer.classList.add("blend-half-in-class");
  await sleep(150);
  imgSource.classList.remove("blend-half-in-class");
  bibleVerseContainer.classList.remove("blend-half-in-class");
}
