<script>

import Header from "$src/parts/Header.svelte";
import Article from "$src/parts/Article.svelte";

export let data;

</script>


<svelte:head>
  <title> {data.title ?? "404"} · pycobytes[{data.index ?? "?"}] </title>
</svelte:head>

<article>
  <Header
    issueIndex={data.index}
    title="{data.title}"
    date={data.date}
  />

  <Article>
    {#if data.content}
      <svelte:component this={data.content} />
    {:else}
      <h1 align="center"> Oops, something went wrong! </h1>
    {/if}
  </Article>
</article>


<style lang="scss">

</style>
