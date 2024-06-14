<!-- The content within a `NavLink`. -->

<script lang="ts">
  
import type { MouseEventHandler } from "svelte/elements";

import { duality } from "#src/scripts/duality";

export let text: string | null = "–";
export let body: string | null = null;
export let pict: string | null = null;
  export let light: string | null = null;
  export let dark: string | null = null;
export let button: MouseEventHandler<HTMLButtonElement> | null = null;

export let invertible: boolean = false;
export let collapsible: boolean = false;

</script>


<div class="nav-part">
  {#if pict}
    <img alt={text}
      src={invertible ?
        ($duality == "light" ? (light ?? pict) : (dark ?? pict))
      : pict}>

  {:else if button}
    <button on:click={button}>
      {#if $$slots}
        <slot />
      {:else}
        {text}
      {/if}
    </button>

  {:else}
    <span> {text} </span>

  {/if}
</div>

{#if !button && $$slots}
  <ul class="nav-dropdown">
    <slot />
  </ul>
{/if}


<style lang="scss">

.nav-part {
  height: 100%;
  height: $nav-part-height;
  max-height: $nav-part-height;
  padding: 0 1em;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  text-align: center;
}

img {
  height: 30px;

  & .invert-duality {
    -webkit-filter: invert(1);
    filter: invert(1);
  }
}

button:not(#increase#specificity) {
  padding: 0;
  color: light-dark($col-accent, $col-flavour);
  background: none;
  border: none;
  cursor: pointer;

  & :not(#non#exist#ent) {
    padding: 0;
  }

  &:hover {
    color: light-dark($col-flavour, $col-accent);
  }
}

.nav-dropdown {
  display: none;
  list-style-type: none;
}

// li:hover > .nav-dropdown {
//   display: block;
// }

</style>
