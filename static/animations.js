const rightAnim = document.querySelectorAll(".right-anim");

const observerRight = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("right-anim-class");
      } else {
        entry.target.classList.remove("right-anim-class");
      }
    });
  },
  {
    threshold: 0,
  }
);

rightAnim.forEach((el) => observerRight.observe(el));

const leftAnim = document.querySelectorAll(".left-anim");

const observerLeft = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("left-anim-class");
      } else {
        entry.target.classList.remove("left-anim-class");
      }
    });
  },
  {
    threshold: 0,
  }
);

leftAnim.forEach((el) => observerLeft.observe(el));

const topAnim = document.querySelectorAll(".top-anim");

const observertop = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("top-anim-class");
      } else {
        entry.target.classList.remove("top-anim-class");
      }
    });
  },
  {
    threshold: 0,
  }
);

topAnim.forEach((el) => observertop.observe(el));

const bottomAnim = document.querySelectorAll(".bottom-anim");

const observer = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("bottom-anim-class");
      } else {
        entry.target.classList.remove("bottom-anim-class");
      }
    });
  },
  {
    threshold: 0,
  }
);

bottomAnim.forEach((el) => observer.observe(el));

const blendInElements = document.querySelectorAll(".blend-in");

const observerBlendIn = new IntersectionObserver(
  (entries) => {
    entries.forEach((entry) => {
      if (entry.isIntersecting) {
        entry.target.classList.add("blend-in-class");
      } else {
        entry.target.classList.remove("blend-in-class");
      }
    });
  },
  {
    threshold: 0,
  }
);

blendInElements.forEach((el) => observerBlendIn.observe(el));
