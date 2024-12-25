<script lang="ts">

import { ratio } from "fuzzball";

import { searchData } from "#scripts/stores/search";

let value = $state("");


function searchIssues()
{
  $searchData.filterFunction = (issue) => (
    issues.toSorted((prot, deut) =>
      ratio(deut.titleText, value) - ratio(prot.titleText, value)
    )
  );
}

</script>


<search>
  <input
    type="search"
    placeholder="Search issues..."
    maxlength="200"
    bind:value
  />

  <button onclick={searchIssues}>
    <span class="material-symbols-outlined">
      search
    </span>
  </button>
</search>


<style lang="scss">

search {
  width: 100%;
  padding: 1rem 0;
  display: flex;
  flex-direction: row;
}

input {
  @include font-ui;
  padding: 1em;
  flex-grow: 1;
  border-radius: 0.5em;

  &:focus {
    outline: none;
  }
}

button {
  font-size: 100%;
  color: white;
  background-color: light-dark($col-prot, $col-deut);

  &:hover {
    background-color: $pink-elec;
  }
}

</style>
