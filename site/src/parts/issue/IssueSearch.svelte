<script lang="ts">

import { ratio } from "fuzzball";

import { searchData } from "#src/scripts/search";

let value = "";


function searchIssues()
{
  $searchData.filterFunction = (issues) => (
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

  <button on:click={searchIssues}>
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
	@include font-flavour;
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
	background-color: light-dark($col-accent, $col-flavour);

	&:hover {
		background-color: $pink-elec;
	}
}

</style>
