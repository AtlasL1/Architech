// Light switcher
const lightSwitches = document.querySelectorAll('.light-switch');
if (lightSwitches.length > 0) {
  lightSwitches.forEach((lightSwitch, i) => {
    if (localStorage.getItem('dark-mode') === 'true') {
      // eslint-disable-next-line no-param-reassign
      lightSwitch.checked = true;
    }
    lightSwitch.addEventListener('change', () => {
      const { checked } = lightSwitch;
      lightSwitches.forEach((el, n) => {
        if (n !== i) {
          // eslint-disable-next-line no-param-reassign
          el.checked = checked;
        }
      });
      if (lightSwitch.checked) {
        document.documentElement.classList.add('dark');
        localStorage.setItem('dark-mode', true);
      } else {
        document.documentElement.classList.remove('dark');
        localStorage.setItem('dark-mode', false);
      }
    });
  });
}

// Scrollspy
document.addEventListener('DOMContentLoaded', function () {
  const targets = document.querySelectorAll('[data-scrollspy-target]');
  const links = document.querySelectorAll('[data-scrollspy-link]');
  if (links.length < 1) return;
  const addActive = (i) => {
    const link = links[i] ? links[i] : links[0];
    link.classList.add('scrollspy-active');
  }
  const removeActive = (i) => {
    links[i].classList.remove('scrollspy-active');
  }
  const removeAllActive = () => [...Array(targets.length).keys()].forEach((link) => removeActive(link));
  const targetMargin = 100;
  let currentActive = 0;
  addActive(0);
  // listen for scroll events
  window.addEventListener('scroll', () => {
    const current = targets.length - [...targets].reverse().findIndex((target) => window.scrollY >= target.offsetTop - targetMargin) - 1;
    if (current !== currentActive) {
      removeAllActive();
      currentActive = current;
      addActive(current);
    }
  });
}, false);

(function switchColor() {
	if (localStorage.getItem('dark-mode') === 'true') {
		let elements = document.querySelectorAll('.cm8ed , .c9lju , .chsoc , .cresr , .ct45g, .c88rp, .cgs8z , .cmjxz, .crlg4, .cc9ex, .czg3k, .c22mi, .cdujf, .cr4sc, .cns0p, .crjda, .ciyk3');
		elements.forEach(function (element) {
			element.style.backgroundColor = 'black';
		});
	};
	if (localStorage.getItem('dark-mode') === 'false') {
		let elements = document.querySelectorAll('.cm8ed , .c9lju , .chsoc , .cresr , .ct45g, .c88rp, .cgs8z , .cmjxz, .crlg4, .cc9ex, .czg3k, .c22mi, .cdujf, .cr4sc, .cns0p, .crjda, .ciyk3');
		elements.forEach(function (element) {
			element.style.backgroundColor = 'white';
		});
	};
	requestAnimationFrame(switchColor);
})();
