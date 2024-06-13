<!-- The content within a `NavLink`. -->

<script lang="ts">
  
import type { MouseEventHandler } from "svelte/elements";

export let text: string | null = "–";
export let body: string | null = null;
export let pict: string | null = null;
export let button: MouseEventHandler<HTMLButtonElement> | null = null;
export let invertible: boolean = false;
export let collapsible: boolean = false;

</script>


<div class="nav-part">
  {#if pict}
    <img alt={text} src={pict} class={invertible ? "invert-duality" : ""}>

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

  & [color-scheme='light'] {
    -webkit-filter: invert(1);
    filter: invert(1);
  }
}

button {
  background: none;
  border: none;
  cursor: pointer;

  & :not(#non#exist#ent) {
    padding: 0;
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
