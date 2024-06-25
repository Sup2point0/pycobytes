<script>

import ISSUES from "#src/issues-config";

import Header from "#src/parts/Header.svelte";
import Main from "#src/parts/Main.svelte";
import IssueNav from "#src/parts/IssueNav.svelte";

import Content from "../2/_Content.svx";

const issue = ISSUES[1];

</script>


<svelte:head>
  <title> {issue.titleText ?? "404 Not Found"} · pycobytes[{issue.issueIndex ?? "?"}] </title>
</svelte:head>

{#if Content}
  <Header
    type = "issue"
    issueIndex = {issue.issueIndex}
    title = "{issue.titleText}"
    caption = {issue.releaseDate}
  >
    <IssueNav {issue} />
  </Header>
  

  <article>
    <Main>
      <Content />
    </Main>
  </article>

  <IssueNav {issue} />

{:else}
  <Main>
    <h1 align="center"> Oops, something went wrong! </h1>
  </Main>

{/if}


<style lang="scss">

h2, h3 {
  border-bottom: 1px solid light-dark($grey-nova, $blue-deep);
}

</style>
