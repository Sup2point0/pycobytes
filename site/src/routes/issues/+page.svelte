<script>

import { ISSUES } from "$lib/issues.config.js";

import Article from "$lib/parts/Article.svelte";

</script>


<svelte:head>
  <title> Issues | pycobytes </title>
</svelte:head>

<Article>
  <ul>
    {#each ISSUES as issue}
      <li>
        <p> {issue.index} </p>
        <a href={`issues/${issue}`}>{issue.title}</a>
      </li>
    {/each}
  </ul>
</Article>


<style>



</style>

