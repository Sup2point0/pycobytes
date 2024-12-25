<footer>
  <div class="info left">
    <p style:font-size="125%"> <span class="pyco-flavour left">pyco</span><span class="pyco-flavour centre">:</span><span class="pyco-flavour right">bytes</span>
    <br> exploring the magic of Python, week by week </p>
    <p> by <a href="https://github.com/Sup2point0">Sup#2.0</a> </p>
  </div>

  <small>
    built with <a target="_blank" href="https://svelte.dev/">Svelte 5</a> + <a target="_blank" href="https://svelte.dev/docs/kit/introduction">SvelteKit</a> &ensp; · &ensp; hosted on <a target="_blank" href="https://pages.github.com/">GitHub Pages</a>
  </small>
</footer>

 
<style lang="scss">

@use './src/styles/links' as *;

p {
  margin-bottom: 2em;
}

footer {
  width: 100%;
  margin-top: 2rem;
  padding: 2rem 10% 3rem;
  display: flex;
  flex-direction: column;
  align-items: start;

  @include font-ui;
  color: $col-text-deut;
  background-color: $col-hover;
  transition: #{fade-duality()};
}

small {
  width: 100%;
  text-align: center;
}

</style>
