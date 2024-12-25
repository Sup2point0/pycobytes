<!-- @component Main

The main content of a page, which resizes responsively.
-->

<script lang="ts">

let { children } = $props();

</script>

<main>
  <div class="content">
    {#if children}
      {@render children()}
    {:else}
      <p class="error"> Uh, something went wrong! </p>
    {/if}
  </div>
</main>


<style>

main {
  margin: 0;
  padding: 1rem;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.content {
  max-width: min(100%, 60rem);
}

</style>
