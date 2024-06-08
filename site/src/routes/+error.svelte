<script>

import Nav from "#src/parts/Nav.svelte";

</script>


<Nav />

<main>
  <div>
    <p> Something went wrong! </p>
  </div>
</main>


<style lang="scss">

div {
  width: 100%;
  text-align: center;
}

p {
  @include font-body;
  color: $grey-nova;
}

</style>
