<script>

import Nav from "#src/parts/Nav.svelte";
import Footer from "#src/parts/Footer.svelte";

import '#src/styles/essence.scss';
import '#src/styles/prism-night-owl.css';

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

</style>
