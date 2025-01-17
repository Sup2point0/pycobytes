<script>

import Site from "#src/site";

import Meta from "#parts/core/meta.svelte";
import Header from "#parts/core/header.svelte";
import Main from "#parts/core/main.svelte";

import { base } from "$app/paths";

</script>


<Meta title="Issues" />

<Header title="Issues" />

<Main>
  <table><tbody>
    {#each Site.issues ?? [] as issue}
      <tr>
        <td class="index" rowspan="2"> {issue.index} </td>
        <td class="date"> {issue.date_display} </td>
      </tr>
      <tr>
        <td class="title"> <a href="{base}/issues/{issue.index}">{issue.title}</a> </td>
      </tr>
    {/each}
  </tbody></table>
</Main>


<style lang="scss">

@use './src/styles/links' as *;


table {
  width: 100%;
}

td {
  &.index {
    padding: 1rem 2rem 0 0;
    @include font-code;
    font-size: 150%;
    color: $grey-spirit;
    vertical-align: middle;
  }

  &.date {
    padding: 2rem 1rem 0 0;
    @include font-ui;
    font-size: 100%;
    color: $grey-nova;
  }

  &.title {
    padding: 0 10rem 0.5rem 0;
    @include font-ui;
    font-size: 200%;
    color: $col-prot;
    border-bottom: 1px solid $grey-spirit;
  }
}

</style>
  