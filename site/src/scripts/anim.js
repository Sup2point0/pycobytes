/// Handles processing scroll animations


export default function processAnimations() {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('anim-in');
      } else if (!entry.isIntersecting) {
        if (!entry.target.classList.contains('init-only')) {
          entry.target.classList.remove('anim-in');
        }
      }
    });
  })

  const animElements = document.querySelectorAll('.anim');
  animElements.forEach(each => observer.observe(each))
}
