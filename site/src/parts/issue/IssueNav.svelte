<script lang="ts">

import Site from "#src/site";

import type { IssueData } from "#scripts/types";

import { base } from "$app/paths";
import { page } from "$app/stores";

export let duality: string | null = null;


const indexCurrent = Site.issues.findIndex(issue => issue.index == $page.data.index) ?? null;

// issue 0 (#1) has no previous
const issuePrev: IssueData | false | null = (indexCurrent != null) && (
  (indexCurrent > 0) && Site.issues[indexCurrent -1]
);

// latest issue has no next
const issueNext: IssueData | false | null = (indexCurrent != null) && (
  (indexCurrent < Site.issues.length -1) && Site.issues[indexCurrent +1]
);

</script>


<div class="issue-nav" style:color-scheme={duality || "inherit"}>
  {#if issuePrev}
    <a class="no-anim" href="{base}/issues/{issuePrev.index}">
      <button class="prev">
        <span class="material-symbols-outlined"> arrow_back_ios </span>
        <div>
          <p> Previous </p>
          <h4> {issuePrev.title} </h4>
        </div>
      </button>
    </a>
  {/if}

  {#if issueNext}
    <a class="no-anim" href="{base}/issues/{issueNext.index}">
      <button class="next">
        <span class="material-symbols-outlined"> arrow_forward_ios </span>
        <div>
          <p> Next </p>
          <h4> {issueNext.title} </h4>
        </div>
      </button>
    </a>
  {/if}
</div>


<style lang="scss">

.issue-nav {
  padding-top: 1rem;
  display: flex;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
}

a {
  min-width: 5rem;
  color: normal;
  text-decoration: none;
}

button {
  margin: 0 0.5rem;
  padding: 0.5rem;
  display: flex;
  &.prev {
    flex-direction: row;
  }
  &.next {
    flex-direction: row-reverse;
  }
  justify-content: start;
  align-items: center;
  background-color: transparent;
  border: none;
  border-radius: 1rem;
  
  transition: all 0.12s ease-out;
  
  &:hover {
    background-color: light-dark(
      rgba($grey-swallow, 0.42),
      rgb(69 69 69 / 0.42)
    );
  }

  &:focus, &:active {
    background-color: light-dark(
      rgba($grey-spirit, 0.42),
      rgb(69 69 69 / 0.69)
    );
  }
  
  div {
    padding: 0 0.5rem;
    color: grey;
  }

  &.prev { text-align: left; }
  &.next { text-align: right; }
}
 
p {
  @include font-flavour;
  margin: 0;
  color: light-dark($grey-nova, white);
  font-size: 120%;
}

h4 {
  @include font-flavour;
  margin: 0.5rem 0;
  padding: 0;
  color: $pink-elec;
  font-size: 150%;
}

span.material-symbols-outlined {
  color: light-dark($grey-nova, $blue-deep);

  transition: all 0.12s ease-out;
}

button:where(:hover, :focus, :active) {
  h4 {
    color: light-dark($col-accent, $col-flavour);
  }
  
  span.material-symbols-outlined {
    color: light-dark($col-accent, $col-flavour);
  }
}

</style>
