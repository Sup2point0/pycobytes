<script>

import { page } from "$app/stores";

import Nav from "#parts/nav/Nav.svelte";

</script>


<Nav />

<main>
  <div>
    <p class="error"> Something went wrong! </p>
  </div>
</main>


<style lang="scss">

div {
  width: 100%;
  text-align: center;
}

p {
  @include font-flavour;
}

</style>
