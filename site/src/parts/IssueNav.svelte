<script lang="ts">

import { base } from "$app/paths";

import ISSUES from "#src/issues-config";
import type IssueData from "#src/scripts/issue";

export let issue: IssueData;


const indexCurrent = issue.orderIndex;

// issue 0 (#1) has no previous
const issuePrev: IssueData =
    (indexCurrent > 0)
  ? ISSUES[indexCurrent -1]
  : undefined;

// latest issue has no next
const issueNext: IssueData =
    (indexCurrent < ISSUES.length -1)
  ? ISSUES[indexCurrent +1]
  : undefined;

</script>


<div class="issue-nav">
  {#if issuePrev !== undefined}
    <a href="{base}/issues/{issuePrev.issueIndex}">
      <button class="prev">
        <div class="material-symbols-outlined"> left_arrow_ios </div>
        <div>
          <p> Previous </p>
          <h4> {issuePrev.titleText} </h4>
        </div>
      </button>
    </a>
  {/if}

  {#if issueNext !== undefined}
    <a href="{base}/issues/{issueNext.issueIndex}">
      <button class="next">
        <div class="material-symbols-outlined"> right_arrow_ios </div>
        <div>
          <p> Next </p>
          <h4> {issueNext.titleText} </h4>
        </div>
      </button>
    </a>
  {/if}
</div>


<style lang="scss">

.issue-nav {
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: baseline;
}

a {
  min-width: 5rem;
  color: normal;
  text-decoration: none;
}

button {
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
  border-radius: 1rem;
  
  transition: all 0.12s ease-out;
  
  &:hover {
    background-color: $grey-swallow;
  }

  &:focus, &:active {
    background-color: $grey-spirit;
  }
  
  div {
    padding: 0 0.5rem;
    color: grey;
  }

  &.prev { text-align: left; }
  &.next { text-align: right; }
}
 
p {
  margin: 0;
}

h4 {
  margin: 0;
  padding: 0;
  color: $pink-elec;
}

</style>
