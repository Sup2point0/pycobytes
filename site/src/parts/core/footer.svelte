<script>

import Pycobytes from "#parts/misc/pyco.svelte";

</script>


<footer>
  <div class="dark-overlay">
    <div class="info">
      <Pycobytes size="500%" />
      <p id="footer-pyco-desc"> exploring the magic of Python, week by week </p>
      <div class="line"></div>

      <p id="footer-sup"> by <a href="https://github.com/Sup2point0">Sup#2.0</a> </p>
    </div>

    <div class="credits">
      built with <a target="_blank" href="https://svelte.dev/">Svelte 5</a> + <a target="_blank" href="https://svelte.dev/docs/kit/introduction">SvelteKit</a> &thinsp; · &thinsp; hosted on <a target="_blank" href="https://pages.github.com/">GitHub Pages</a>
    </div>
  </div>
</footer>

 
<style lang="scss">

@use './src/styles/links' as *;

footer {
  color-scheme: dark;
  margin-top: 2rem;

  @include font-ui;
  color: white;
  background-color: $blue-night;
  background-image: url("/pycobytes-back-2.png");
  background-size: 100%;
  background-repeat: no-repeat;
}

.dark-overlay {
  width: 100%;
  height: 100%;
  padding: 4rem 10% 8rem;
  display: flex;
  flex-direction: column;
  align-items: end;
  text-align: right;
  background: linear-gradient(to right in srgb,
    rgb(black, 20%),
    black 75%,
  );
  backdrop-filter: blur(1px);
}

.info {
  margin-bottom: 5em;
  
  #footer-pyco-desc {
    padding: 0.75em 0 1.5em;
    font-size: 150%;
  }

  .line {
    width: 50%;
    padding-top: 0.75em;
    margin-left: auto;
    border-bottom: 1px solid $col-prot;
  }

  #footer-sup {
    padding-top: 1em;
  }
}

.credits {
  padding-top: 1em;
}

</style>
