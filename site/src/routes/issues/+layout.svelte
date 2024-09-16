<script>

import { page } from "$app/stores";

import Header from "#parts/Header.svelte";
import Main from "#parts/Main.svelte";
import IssueNav from "#parts/issue/IssueNav.svelte";
import IssueFooter from "#parts/issue/IssueFooter.svelte";

</script>


<svelte:head>
  <title> {$page.data.title ?? "404 Not Found"} · pycobytes[{$page.data.index ?? "?"}] </title>
</svelte:head>


<Header
  type = "issue"
>
  <IssueNav duality="dark" />
</Header>

<article>
  <Main>
    <slot />
    <IssueFooter />
  </Main>
</article>

<IssueNav />
