export default function process_animations()
{
  const observer = new IntersectionObserver(entries => {
    for (let entry of entries) {
      if (entry.isIntersecting) {
        entry.target.classList.add("anim-in");
      }
      else if (!entry.isIntersecting) {
        if (!entry.target.classList.contains("init-only")) {
          entry.target.classList.remove("anim-in");
        }
      }
    }
  })

  let animated = document.querySelectorAll(".anim");
  for (let each of animated) {
    observer.observe(each);
  }
}
