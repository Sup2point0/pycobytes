<script>

let pageSourceLink = "https://github.com/Sup2point0/pycobytes";

</script>

<div class="footer">
  <div class="footer-info">
    <p> <span class="pyb-flavour left">pyco</span><span class="pyb-flavour centre">:</span><span class="pyb-flavour right">bytes</span>
    <br> exploring the magic of Python, week by week </p>
    <p> by Sup#2.0 </p>
  </div>
  <div class="footer-note">
    <p> View on <a href={pageSourceLink}>GitHub</a> </p>
  </div>
</div>
 
<style lang="scss">

.footer {
  width: 100%;
  color: $grey-nova;
  background-color: $grey-swallow;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.footer-info {
  width: 100%;
}

.footer-note {
  width: 100%;
  text-align: center;
}

span.pyb-flavour {
  &.left { color: $light-accent-prot; }
  &.centre { color: $grey-nova; }
  &.right { color: $light-accent-deut; }
}

</style>
