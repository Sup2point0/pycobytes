<script>

import { ISSUES } from "$lib/issues.config.js";

</script>


<svelte:head>
  <title> Issues | pycobytes </title>
</svelte:head>

<ul>
  {#each ISSUES as issue}
    <li>
      <p> {issue.index} </p>
      <a href={`issues/${issue}`}>{issue.title}</a>
    </li>
  {/each}
</ul>


<style>



</style>

