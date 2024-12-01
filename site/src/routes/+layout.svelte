<script>

import "#styles/essence.scss";
import "#styles/prism-night-owl.scss";

import { duality, setFromLocalDuality } from "#scripts/stores";

import Nav from "#parts/nav/Nav.svelte";
import Footer from "#parts/layout/Footer.svelte";

import { browser } from "$app/environment";


$: currentDuality = (
  $duality ? ($duality == "dark" ? "dark" : "light")
  : browser ? setFromLocalDuality(window) : "light"
);

</script>


<!-- <svelte:head>
  <script defer src="/src/scripts/prism.js"> </script>
</svelte:head> -->

<div class="duality-container" style="color-scheme: {currentDuality}">
  <Nav />
  <slot />
  <Footer />
</div>


<style lang="scss">

.duality-container {
  margin-top: $nav-height;
}

</style>
