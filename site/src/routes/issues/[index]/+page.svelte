<script>

import Header from "$src/parts/Header.svelte";
import Article from "$src/parts/Article.svelte";

export let data;

</script>


<svelte:head>
  <title> {data.title ?? "404"} • pycobytes[{data.index ?? "?"}] </title>
</svelte:head>

<Article>
  <article>
    <Header title="{data.title}" date={data.date} />

    {#if data.content}
      <svelte:component this={data.content} />
    {:else}
      <h1> ERROR </h1>
    {/if}
  </article>
</Article>
