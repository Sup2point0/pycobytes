<!-- @component
A link in the navbar. Dropdown `NavLink`s can be added as a slot.
-->

<script lang="ts">

import NavPart from "#parts/nav/NavPart.svelte";

// NOTE adding intern functionality
export let link: string | undefined = undefined;
  export let intern: string | undefined = undefined;
  export let extern: string | undefined = undefined;

</script>


<li class="nav-link">
  {#if link || extern}
    <a
      class = "no-anim"
      href = {extern ? extern : link}
      target = {extern ? "_blank" : null}
    >
      <NavPart {...$$restProps}>
        <slot />
      </NavPart>
    </a>
  
  {:else}
    <NavPart {...$$restProps}>
      <slot />
    </NavPart>
  
  {/if}
</li>


<style lang="scss">

li.nav-link {
  @include font-flavour;
  max-height: $nav-part-height;
  margin: 0.5rem 0.2rem;
  padding: 0;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  overflow: visible;
  border-radius: 0.75em;
  
  transition: all 0.16s ease-out;
  @media prefers-reduced-motion {
    transition: none;
  }
  
  & a {
    height: 100%;
    text-decoration: none;
    color: light-dark(rgb(20 20 20), white);
  }

  &:where(:hover, :focus, :focus-within) {
    cursor: pointer;
    background-color: $col-hover;
    outline: none;
    border: none;
  }

  &:where(:active) {
    background-color: $col-active;
  }
}

@media (max-width: 800px) {
  li .collapsible {
    display: none;
  }
}

</style>
