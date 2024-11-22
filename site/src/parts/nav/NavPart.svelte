<!-- @component NavPart

The content within a `NavLink`.
-->

<script lang="ts">

import { duality } from "#scripts/stores";

import type { MouseEventHandler } from "svelte/elements";

export let text: string | undefined = "–";
export let body: string | undefined = undefined;
export let pict: string | undefined = undefined;
  export let light: string | undefined = undefined;
  export let dark: string | undefined = undefined;
export let button: MouseEventHandler<HTMLButtonElement> | undefined = undefined;

export let collapsible: boolean = false;

</script>


<div class="nav-part" class:collapsible>
  {#if pict || light || dark}
    <img alt={text}
      src={$duality == "light" ? (light ?? pict) : (dark ?? pict)}>

  {:else if button}
    <button id={text} on:click={button}>
      {#if $$slots}
        <slot />
      {:else}
        {text}
      {/if}
    </button>

  {:else if body}
    <span> {@html body} </span>
  
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
  &:not(:has(button)) { padding: 0 1em; }
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  text-align: center;
  vertical-align: middle;

  &:hover button#duality {
    color: light-dark($lilac-nova, $col-flavour);
  }
}

img {
  height: 30px;
  min-height: 30px;
  max-height: 30px;
  aspect-ratio: 1;
}

button {
  font: inherit;
  height: 100%;
  width: 100%;
  padding: 0 1em;
  background: none;
  border: none;
  cursor: pointer;

  &#duality {
    color: light-dark($col-accent, $lilac-nova);
  }
}

ul.nav-dropdown {
  display: none;
  // opacity: 0;
  list-style-type: none;
  // transition: opacity 0.2s ease-out;
}

.nav-part:hover ~ ul.nav-dropdown,
ul.nav-dropdown:hover
{
  position: absolute;
  top: $nav-height - 0.2rem;
  padding: 0 0.5rem;
  display: block;
  background-color: $col-idle;
  // opacity: 1;
  border-bottom-left-radius: 0.75rem;
  border-bottom-right-radius: 0.75rem;
}

@media (max-width: 36rem) {
  .nav-part.collapsible {
    display: none;
  }
}

</style>
