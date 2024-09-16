<script>

import { page } from "$app/stores";
import { Issues } from "#src/site";

import Header from "#parts/Header.svelte";
import Main from "#parts/Main.svelte";
import IssueNav from "#parts/issue/IssueNav.svelte";
import IssueFooter from "#parts/issue/IssueFooter.svelte";

import Content from "./%{file}.svx";


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
