<script lang="ts">

import Site from "#src/site";
import type { Duality } from "#scripts/types";

import { page } from "$app/stores";
import { base } from "$app/paths";

interface Props {
  duality?: Duality;
}

let { duality }: Props = $props();


let index_current = $derived(
  Site.issues.findIndex(issue => issue.index && issue.index[0] === $page.data.index[0])
);

// issue 0 (#1) has no previous
let issue_prev = $derived(
  (index_current != null) && (index_current < Site.issues.length -1) &&
  Site.issues[index_current +1]
);

// latest issue has no next
let issue_next = $derived(
  (index_current != null) && (index_current > 0) &&
  Site.issues[index_current -1]
);

</script>


<nav class="issue-nav" style:color-scheme={duality || "inherit"}>
  {#if issue_prev}
    <a class="prev" href="{base}/issues/{issue_prev.index}">
      <span class="material-symbols-outlined"> arrow_back_ios </span>
      <div>
        <p> Previous </p>
        <h4> {issue_prev.title} </h4>
      </div>
    </a>
  {/if}

  {#if issue_next}
    <a class="next" href="{base}/issues/{issue_next.index}">
      <span class="material-symbols-outlined"> arrow_forward_ios </span>
      <div>
        <p> Next </p>
        <h4> {issue_next.title} </h4>
      </div>
    </a>
  {/if}
</nav>


<style lang="scss">

.issue-nav {
  margin: 0 auto;
  max-width: max(70%, 800px);
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
}

a {
  min-width: 10em;
  padding: 0.5em 1em;
  display: flex;
  &.prev { flex-direction: row; }
  &.next { flex-direction: row-reverse; }
  justify-content: start;
  align-items: center;
  gap: 0.5rem;

  text-decoration: none;
  background-color: transparent;
  border: none;
  border-radius: 1rem;
  transition: #{fade-interact()};
  
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

  &:where(:hover, :focus, :active) {
    // h4 {
    //   color: light-dark($col-prot, $col-deut);
    // }
    
    span.material-symbols-outlined {
      color: light-dark($col-prot, $col-deut);
    }
  }

  &.prev { text-align: left; }
  &.next { text-align: right; }
}
 
p {
  @include font-ui;
  color: light-dark($grey-nova, white);
  font-size: 120%;
}

h4 {
  @include font-ui;
  margin: 0.25em 0;
  padding: 0;
  color: $pink-elec;
  font-size: 150%;
}

.material-symbols-outlined {
  color: light-dark($grey-nova, $blue-deep);
  transition: #{fade-interact()};
}

</style>
