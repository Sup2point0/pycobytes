<script>

let pageSourceLink = "https://github.com/Sup2point0/pycobytes";

</script>


<footer>
  <div class="footer">
    <div class="info left">
      <p> <span class="pyb-flavour left">pyco</span><span class="pyb-flavour centre">:</span><span class="pyb-flavour right">bytes</span>
      <br> exploring the magic of Python, week by week </p>
      <p> by <a href="https://github.com/Sup2point0">Sup#2.0</a> </p>
    </div>
    <div class="info right">
      <p> Created with <a href="https://kit.svelte.dev"><span class="col-flavour svelte">SvelteKit</span></a>
      <br> Hosted on <a href="https://pages.github.com/">GitHub Pages</a> </p>
      <p> View on <a href={pageSourceLink}>GitHub</a> </p>
    </div>
  </div>
</footer>

 
<style lang="scss">

p {
  margin-bottom: 2em;
}

footer {
  width: 100%;
  margin-top: 2rem;
  padding: 2rem 0 3rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: light-dark($grey-swallow, black);
  @include fade-duality;
}

.footer {
  @include font-flavour;
  width: 80%;
  margin: 1rem auto 2rem;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  color: $grey-nova;
}

.left { text-align: left }
.right { text-align: right }

span {
  &.col-flavour {
    &.svelte:not(:hover) { color: #ff3e00; }
  }
}

</style>
