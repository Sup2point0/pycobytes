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

main {
  width: 80%;
}

span.pyb-flavour {
  &.left { color: $light-accent-prot; }
  &.centre { color: $grey-nova; }
  &.right { color: $light-accent-deut; }
}

</style>
