<script>

import { page } from "$app/stores";

import Header from "#parts/core/header.svelte";
import Main from "#parts/core/main.svelte";
import IssueNav from "#parts/issue/nav.issue.svelte";
import IssueFooter from "#parts/issue/footer.issue.svelte";


let { children } = $props();

</script>


<svelte:head>
  <title> {$page.data.title ?? "404 Not Found"} · pycobytes[{$page.data.index ?? "?"}] </title>
</svelte:head>


<Header ctx="issue">
  <IssueNav duality="dark" />
</Header>

<article>
  <Main>
    {#if children}
      {@render children()}
    {:else}
      <p class="error"> Uh, something went wrong! </p>
    {/if}
    
    <IssueFooter />
  </Main>
</article>

<IssueNav />
