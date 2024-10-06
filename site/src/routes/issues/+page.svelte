<script>

import Site from "#src/site";

import Header from "#parts/Header.svelte";
import Main from "#parts/Main.svelte";

import { base } from "$app/paths";

</script>


<svelte:head>
  <title> Issues · pycobytes </title>
</svelte:head>

<Header title="Issues" />

<Main>
  <table>
    {#each Site.issues ?? [] as issue}
      <tr>
        <td class="issue-index" rowspan="2"> {issue.index} </td>
        <td class="issue-date"> {issue.date_display} </td>
      </tr>
      <tr>
        <td class="issue-title"> <a href="{base}/issues/{issue.dest}">{issue.title}</a> </td>
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
  
