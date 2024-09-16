<script>

import ISSUES from "#src/issues-config";

import Header from "#parts/Header.svelte";
import Main from "#parts/Main.svelte";


const issues = [...ISSUES];
issues.reverse();

</script>


<svelte:head>
  <title> Issues · pycobytes </title>
</svelte:head>

<Header title="Issues" />

<Main>
  <table>
    {#each issues as issue}
      <tr>
        <td class="issue-index" rowspan="2"> {issue.displayIndex} </td>
        <td class="issue-date"> {issue.releaseDate} </td>
      </tr>
      <tr>
        <td class="issue-title"> <a href="./issues/{issue.issueIndex}">{issue.titleText}</a> </td>
      </tr>
    {/each}
    </table>
</Main>


<style lang="scss">

table {
  width: 100%;
}

td {
  &.issue-index {
    padding: 1rem 2rem 0 0;
    @include font-mono;
    font-size: 150%;
    color: $grey-spirit;
    vertical-align: middle;
  }

  &.issue-date {
    padding: 2rem 1rem 0 0;
    @include font-flavour;
    font-size: 100%;
    color: $grey-nova;
  }

  &.issue-title {
    padding: 0 10rem 0.5rem 0;
    @include font-flavour;
    font-size: 200%;
    color: $col-flavour;
    border-bottom: 1px solid $grey-spirit;
  }
}

</style>
  
