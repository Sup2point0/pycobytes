<script>

import { ISSUES } from "$src/issues-config.js";

import Article from "$src/parts/Article.svelte";

</script>


<svelte:head>
  <title> Issues | pycobytes </title>
</svelte:head>

<Article>
  <ul>
    {#each ISSUES as issue}
      <li>
        <p> {issue} </p>
        <a href={`issues/${issue}`}>{issue.title}</a>
      </li>
    {/each}
  </ul>
</Article>


<style>



</style>

