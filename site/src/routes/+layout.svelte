<script>

import Nav from "$src/parts/Nav.svelte";
import Footer from "$src/parts/Footer.svelte";

import '$src/styles/essence.scss';
import '$src/styles/prism-night-owl.css';

import duality from "$src/scripts/duality";

</script>


<div class="duality-container" style="color-scheme: {$duality}">
  <Nav />
  <slot />
  <Footer />
</div>


<style lang="scss">

</style>
