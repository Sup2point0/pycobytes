<script>

  import { ISSUES } from "$src/issues-config.js";
  
  import Header from "$src/parts/Header.svelte";
  import Article from "$src/parts/Article.svelte";
  
  </script>
  
  
  <svelte:head>
    <title> Issues • pycobytes </title>
  </svelte:head>
  
  <Header title="Issues" />
  
  <Article>
    <ul>
      {#each ISSUES as issue}
        <li>
          <p> {issue.index} </p>
          <a href={`issues/${issue.index}`}>{issue.title}</a>
        </li>
      {/each}
    </ul>
  </Article>
  
  
  <style>
  
  
  
  </style>
  
  