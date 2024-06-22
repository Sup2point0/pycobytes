<script lang="ts">

import { onMount } from "svelte";

import requestNapkin from "#src/scripts/napkin";
import { ClickData } from "#src/scripts/napkin";


const SHARD = "pycobytes-clicky";

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
  console.log("mounted");

  if (localStorage.getItem(SHARD)) {
    clickState = ClickState.Depleted;
  } else {
    clickState = ClickState.Waiting;
  }

  try {
    clickData = await requestNapkin("GET");
    console.log(clickData);
  }
  catch (error) {
    clickData = {
      clickCount: "?",
      lastClick: "?",
    }
  }
});


async function clicky() {
  if (clickState == ClickState.Idle) return;
  
  if (localStorage.getItem(SHARD)) {
    clickState = ClickState.Depleted;
  } else {
    clickData = await requestNapkin("POST");
    clickState = ClickState.Clicked;
  }
}

</script>


<button on:click|once={clicky}>
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


<style lang="scss">

button {
  margin: 2rem 0 4rem;
  padding: 0 2em;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  @include font-flavour;
  font-size: 125%;
  color: white;
  background-color: $orange-spirit;
  border: none;
  border-radius: 1rem;
  
  transition: all 0.16s ease-out;  // ease-out cubic
  box-shadow: 0 0 16px rgba($yellow-nova, 0.5);

  &:hover {
    background-color: $pink-elec;
    box-shadow: 0 0 16px rgba($pink-elec, 0.5);
  }
  &:active {
    background-color: $purp-nova;
    box-shadow: 0 0 16px $lilac-nova;
  }
}

</style>
