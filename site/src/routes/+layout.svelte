<script>

import Nav from "#src/parts/nav/Nav.svelte";
import Footer from "#src/parts/Footer.svelte";

import "#src/styles/essence.scss";
import "#src/styles/prism-night-owl.scss";

import duality from "#src/scripts/duality";

</script>


<svelte:head>
  <script defer src="/src/scripts/prism.js"> </script>
</svelte:head>

<div class="duality-container" style="color-scheme: {$duality}">
  <Nav />
  <slot />
  <Footer />
</div>


<style lang="scss">

.duality-container {
  margin-top: $nav-height;
}

</style>
