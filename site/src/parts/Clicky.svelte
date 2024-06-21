<script lang="ts">

import { requestNapkin } from "#src/scripts/napkin";

const SHARD = "pycobytes-clicky";

enum ClickState {
  Idle,
  Waiting,
  Clicked,
  Depleted,
  Error,
}

let clickData;
let clickState = ClickStates.Idle;

onMount(async () => {
  if (localStorage.getItem(SHARD)) {
    clickState = ClickState.Depleted;
  } else {
    clickState = ClickState.Waiting;
  }

    clickData = await requestNapkin("get");
});

async function clicky() {
  if (clickState == ClickState.Idle) return;
  
  if (localStorage.getItem(SHARD)) {
    clickState = ClickState.Depleted;
  } else {
    let response = await requestNapkin("post");
    clickState = ClickState.Clicked;
  }
}

</script>


<button on:click|once={clicky}>
  {#if clickState == ClickState.Depleted}
    This button has been clicked by {clickData.clickCount} pips, including you!
  {:else if clickState == ClickState.Clicked}
    This button has now been clicked by {clickData.clickCount} pips!
  {:else if clickState == ClickState.Error}
    ...Something went wrong?
  {:else if clickState == ClickState.Waiting}
    This button has been clicked by {data.clickCount} pips.
  {:else}
    Oh, what’s this?
  {/if}
</button>
    
