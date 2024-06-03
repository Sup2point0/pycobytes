<script>

let pageSourceLink = "https://github.com/Sup2point0/pycobytes";

</script>

<div class="footer-container">
  <div class="footer">
    <div class="info left">
      <p> <span class="pyb-flavour left">pyco</span><span class="pyb-flavour centre">:</span><span class="pyb-flavour right">bytes</span>
      <br> exploring the magic of Python, week by week </p>
      <p> by <a href="https://github.com/Sup2point0">Sup#2.0</a> </p>
    </div>
    <div class="info right">
      <p> Created with SvelteKit
      <br> Hosted on GitHub Pages </p>
      <p> View on <a href={pageSourceLink}>GitHub</a> </p>
    </div>
  </div>
</div>
 
<style lang="scss">

.footer-container {
  width: 100%;
  padding: 1rem auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: $grey-swallow;
}

.footer {
  width: 80%;
  display: flex;
  flex-direction: row;
  justify-items: space-between;
  color: $grey-nova;
}

.left { text-align: left }
.right { text-align: right }

info {
  // min-width: 30vw;
}

span.pyb-flavour {
  &.left { color: $light-accent-prot; }
  &.centre { color: $grey-nova; }
  &.right { color: $light-accent-deut; }
}

</style>
