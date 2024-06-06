<script>

import Header from "$src/parts/Header.svelte";
import Article from "$src/parts/Article.svelte";

import ISSUES from "$src/issues-config";

export let data;

</script>


<svelte:head>
  <title> {data.title ?? "404 Not Found"} · pycobytes[{data.issueIndex ?? "?"}] </title>
</svelte:head>

<article>
  {#if data.content}
    <Header
      type = "issue"
      issueIndex = {data.issueIndex}
      title = "{data.title}"
      date = {data.date}
    />

    <Article>
      <svelte:component this={data.content} />
    </Article>

  {:else}
    <Article>
      <h1 align="center"> Oops, something went wrong! </h1>
    </Article>
  
  {/if}
</article>


<style lang="scss">

</style>
