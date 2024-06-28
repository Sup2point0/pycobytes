<script>

import ISSUES from "#src/issues-config";

import Header from "#src/parts/Header.svelte";
import Main from "#src/parts/Main.svelte";
import IssueNav from "#src/parts/IssueNav.svelte";
import IssueFooter from "#src/parts/IssueFooter.svelte";

import "#src/routes/issues/_issue.scss";

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
    tags = {issue.topicTags}
  >
    <IssueNav {issue} duality="dark" />
  </Header>
  

  <article>
    <Main>
      <Content />
      <IssueFooter />
    </Main>
  </article>

  <IssueNav {issue} />

{:else}
  <Main>
    <h1 align="center"> Oops, something went wrong! </h1>
  </Main>

{/if}
