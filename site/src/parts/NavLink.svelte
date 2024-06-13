<!-- A link in the navbar, potentially with a dropdown menu too. -->

<script lang="ts">

import NavPart from "#src/parts/NavPart.svelte";

export let link: string | null = null;
export let extern: string | null = null;

</script>


<li class="nav-link">
  {#if link}
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
  margin: 0.5rem 0.2rem;
  padding: 0;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  border-radius: 0.7em;
  
  & a {
    @include font-fun;
    height: 100%;
    text-decoration: none;
    color: light-dark(rgb(20 20 20), white);
  }
}

li {
  transition: all 0.16s ease-out;

  @media prefers-reduced-motion {
    transition: none;
  }

  &:hover {
    cursor: pointer;
    background-color: $col-hover;

    & > a {
      color: light-dark($col-accent, $col-flavour);
    }
  }
}

</style>
