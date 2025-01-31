<script lang="ts">

import TimeAgo from "javascript-time-ago";
import en from "javascript-time-ago/locale/en";

import { request_napkin, type ClickData } from "#scripts/napkin";

import { onMount } from "svelte";


const SHARD = "pycobytes-clicky";

try {
  TimeAgo.addDefaultLocale(en);
} catch {}
const time_ago = new TimeAgo("en-US");

enum ClickState {
  Idle,
  Waiting,
  Clicked,
  Depleted,
  Error,
}

let click_data: ClickData = $state();
let click_state: ClickState = $state(ClickState.Idle);


onMount(async () => {
  if (localStorage.getItem(SHARD)) {
    click_state = ClickState.Depleted;
  } else {
    click_state = ClickState.Waiting;
  }

  click_data = await request_napkin("GET");
});


async function clicky() {
  if (click_state == ClickState.Idle) return;
  if (click_state == ClickState.Clicked) return;
  
  if (localStorage.getItem(SHARD)) {
    click_state = ClickState.Depleted;
    return;
  }

  if (click_state == ClickState.Depleted) return;

  click_data = await request_napkin("POST");
  if (!click_data) {
    click_state = ClickState.Error;
    return;
  }

  localStorage.setItem(SHARD, click_data.click_count.toString());
  click_state = ClickState.Clicked;
}

</script>


<aside class="clicky">
  <button onclick={clicky}>
    {#if click_data}
      {#if click_state === ClickState.Depleted}
        <p> This button has been clicked by {click_data.click_count ?? "?"} pips, including you! </p>
      
      {:else if click_state === ClickState.Clicked}
        <p> This button has now been clicked by {click_data.click_count ?? "?"} pips! </p>
      
      {:else if click_state === ClickState.Error}
        <p> ...Something went wrong? </p>
      
      {:else}
        <p> This button has been clicked by {click_data.click_count ?? "?"} pips. </p>

      {/if}
    
    {:else}
      <p> Oh, what’s this? </p>
    
    {/if}
  </button>

  <p class="caption">
    {typeof click_data?.last_click === "number"
      ? "Last clicked " + time_ago.format(new Date(click_data.last_click * 1000))
      : ""
    }
  </p>
</aside>


<style lang="scss">

aside {
  padding: 3rem 0;
}

button {
  padding: 0.75em 1.5em;
  display: flex;
  justify-content: center;
  align-items: center;

  @include font-ui;
  font-size: 120%;
  color: light-dark(white, white);
  background: light-dark(black, white);
  border: none;
  border-radius: 2rem;
  transition: all 0.12s ease-out;  // ease-out cubic

  &:hover {
    cursor: pointer;
    color: $col-prot;
    box-shadow: 0 0 8px $col-prot;
  }
  &:active {
    color: $col-deut;
    box-shadow: 0 0 12px $col-deut;
  }
}

.caption {
  padding-top: 1rem;
  color: light-dark($grey-nova, $blue-deep);
}

</style>
