<!-- A link in the navbar, potentially with a dropdown menu too. -->

<script lang="ts">

import NavPart from "#src/parts/NavPart.svelte";

export let link: string | null = null;
export let extern: string | null = null;

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

// * {
//   outline: $lilac-nova solid 1px;
// }

li.nav-link {
  @include font-fun;
  margin: 0.5rem 0.2rem;
  padding: 0;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  border-radius: 0.7em;
  
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

    & button#duality {
      color: light-dark($lilac-nova, $col-flavour);
    }
  }
}

@media (max-width: 800px) {
  li .collapsible {
    display: none;
  }
}

</style>
