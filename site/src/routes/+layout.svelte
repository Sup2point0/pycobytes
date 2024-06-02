<script>

import Nav from "$lib/parts/Nav.svelte";
import Footer from "$lib/parts/Footer.svelte";

import '$lib/styles/essence.scss';

</script>


<Nav />

<div class="content">
  <slot />
</div>

<Footer />


<style lang="scss">

.content {
  display: flex;
  flex-direction: column;
  align-items: center;
}

</style>
