<script>

let pageSourceLink = "https://github.com/Sup2point0/pycobytes";

</script>


<footer>
  <div class="footer">
    <div class="info left">
      <p style:font-size="125%"> <span class="pyb-flavour left">pyco</span><span class="pyb-flavour centre">:</span><span class="pyb-flavour right">bytes</span>
      <br> exploring the magic of Python, week by week </p>
      <p> by <a href="https://github.com/Sup2point0">Sup#2.0</a> </p>
    </div>
    <div class="info right">
      <p> Built with <a target="_blank" href="https://svelte.dev"><span class="col-flavour svelte">Svelte</span></a>/<a target="_blank" href="https://svelte.dev/docs/kit/introduction"><span class="col-flavour svelte-kit">Kit</span></a>
      <br> Hosted on <a target="_blank" href="https://pages.github.com/">GitHub Pages</a> </p>
      <p> View on <a target="_blank" href={pageSourceLink}>GitHub</a> </p>
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
    &.svelte-kit:not(:hover) { color: #ff3e00; }
  }
}

</style>
