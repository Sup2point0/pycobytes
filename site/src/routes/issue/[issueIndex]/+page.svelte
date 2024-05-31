<script>

import Header from "$lib/parts/Header.svelte";

export let data;

</script>

<article>
  <Header title={data.title} />

  <svelte:component this={data.content} />
</article>
