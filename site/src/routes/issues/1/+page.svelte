<script>

import ISSUES from "#src/issues-config";
const issue = ISSUES[0];

import Content from "../1/_Content.svx";


import Header from "#src/parts/Header.svelte";
import Main from "#src/parts/Main.svelte";

</script>


<svelte:head>
  <title> {issue.title ?? "404 Not Found"} · pycobytes[{issue.issueIndex ?? "?"}] </title>
</svelte:head>

<article>
  {#if issue.content}
    <Header
      type = "issue"
      issueIndex = {issue.issueIndex}
      title = "{issue.title}"
      caption = {issue.date}
    />

    <Main>
      <Content />
    </Main>

  {:else}
    <Main>
      <h1 align="center"> Oops, something went wrong! </h1>
    </Main>
  
  {/if}
</article>


<style lang="scss">

</style>
