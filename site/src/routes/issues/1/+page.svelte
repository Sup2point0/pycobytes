<script>

import { page } from "$app/stores";
import { Issues } from "#src/site";

import Header from "#src/parts/Header.svelte";
import Main from "#src/parts/Main.svelte";
import IssueNav from "#src/parts/IssueNav.svelte";
import IssueFooter from "#src/parts/IssueFooter.svelte";

import Content from "./~content.svx";


const issue = Issues[$page.data.index];

</script>


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
