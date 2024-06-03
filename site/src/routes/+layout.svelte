<script>

import Nav from "$src/parts/Nav.svelte";
import Footer from "$src/parts/Footer.svelte";

import '$src/styles/essence.scss';
import '$src/styles/prism-night-owl.css'

</script>


<Nav />

<div style="margin-top: 4rem">
  <slot />
</div>

<Footer />


<style lang="scss">

</style>
