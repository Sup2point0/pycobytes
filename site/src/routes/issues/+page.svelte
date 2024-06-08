<script>

import ISSUES from "#src/issues-config.js";

import Header from "#src/parts/Header.svelte";
import Article from "#src/parts/Article.svelte";

</script>


<svelte:head>
  <title> Issues · pycobytes </title>
</svelte:head>

<Header title="Issues" />

<Article>
  <ul>
    {#each ISSUES as issue}
      <li>
        <p>
          <span class="issue-index"> {issue.name} </span>
          <span class="issue-title"> <a href="./issues/{issue.issueIndex}">{issue.title}</a> </span>
          <span class="issue-date"> {issue.date} </span>
        </p>
      </li>
    {/each}
  </ul>
</Article>


<style lang="scss">

h2, h3 {
  color: $col-accent;
}

ul {
  list-style-type: none;
}

span {
  &.issue-index {
    @include font-mono;
    color: $grey-nova;
  }
  &.issue-title {
    @include font-flavour;
    color: $col-flavour;
  }
  &.issue-date {
    color: $grey-nova;
  }
}

</style>
  
