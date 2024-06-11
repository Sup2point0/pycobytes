<script>

import Header from "#src/parts/Header.svelte";
import Main from "#src/parts/Main.svelte";

import ISSUES from "#src/issues-config";

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
      caption = {data.date}
    />

    <Main>
      <svelte:component this={data.content} />
    </Main>

  {:else}
    <Main>
      <h1 align="center"> Oops, something went wrong! </h1>
    </Main>
  
  {/if}
</article>


<style lang="scss">

</style>
