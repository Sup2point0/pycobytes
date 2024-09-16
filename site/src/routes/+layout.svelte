<script>

import "#styles/essence.scss";
import "#styles/prism-night-owl.scss";

import duality from "#scripts/duality";

import Nav from "#parts/nav/Nav.svelte";
import Footer from "#parts/Footer.svelte";

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
