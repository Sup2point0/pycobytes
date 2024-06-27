<script lang="ts">

import { onMount } from "svelte";

import TimeAgo from "javascript-time-ago";
import en from "javascript-time-ago/locale/en";

import requestNapkin from "#src/scripts/napkin";
import ClickData from "#src/scripts/napkin";


const SHARD = "pycobytes-clicky";

TimeAgo.addDefaultLocale(en);
const timeAgo = new TimeAgo("en-US");

enum ClickState {
  Idle,
  Waiting,
  Clicked,
  Depleted,
  Error,
}

let clickData: ClickData;
let clickState: ClickState = ClickState.Idle;


onMount(async () => {
  if (localStorage.getItem(SHARD)) {
    clickState = ClickState.Depleted;
  } else {
    clickState = ClickState.Waiting;
  }

  clickData = await requestNapkin("GET");
});


async function clicky() {
  if (clickState == ClickState.Idle) return;
  if (clickState == ClickState.Clicked) return;
  
  if (localStorage.getItem(SHARD)) {
    clickState = ClickState.Depleted;
    return;
  }

  if (clickState == ClickState.Depleted) return;

  clickData = await requestNapkin("POST");
  if (!clickData) {
    clickState = ClickState.Error;
    return;
  }

  localStorage.setItem(SHARD, clickData.clickCount.toString());
  clickState = ClickState.Clicked;
}

</script>


<div class="clicky">
  <button on:click={clicky}>
    {#if clickData}
      {#if clickState == ClickState.Depleted}
        <p> This button has been clicked by {clickData.clickCount ?? "?"} pips, including you! </p>
      
      {:else if clickState == ClickState.Clicked}
        <p> This button has now been clicked by {clickData.clickCount ?? "?"} pips! </p>
      
      {:else if clickState == ClickState.Error}
        <p> ...Something went wrong? </p>
      
      {:else}
        <p> This button has been clicked by {clickData.clickCount ?? "?"} pips. </p>

      {/if}
    
    {:else}
      <p> Oh, what’s this? </p>
    
    {/if}
  </button>

  <p class="caption"> {clickData?.lastClick
    ? "Last clicked " + timeAgo.format(new Date(clickData.lastClick * 1000))
    : ""
  } </p>
</div>


<style lang="scss">

.clicky {
  margin: 2rem 0 4rem;
}

button {
  margin: 0;
  padding: 0 2em;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  @include font-fun;
  font-size: 125%;
  color: white;
  background-color: $orange-spirit;
  border: none;
  border-radius: 1rem;
  
  transition: all 0.16s ease-out;  // ease-out cubic
  box-shadow: 0 0 16px light-dark(rgba($yellow-nova, 0.5), rgb(0 0 0));

  &:hover {
    background-color: $pink-elec;
    box-shadow: 0 0 16px rgba($pink-elec, 0.5);
  }
  &:active {
    background-color: $purp-nova;
    box-shadow: 0 0 16px light-dark($lilac-nova, rgba($lilac-nova, 0.5));
  }
}

.caption {
  color: light-dark($grey-nova, $blue-deep);
}

</style>
