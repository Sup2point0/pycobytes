<!-- @component Nav

The global site navigation bar.
-->

<script lang="ts">

import Site from "#src/site";

import { duality, swapDuality } from "#scripts/stores";
import { pickRandomIssue } from "#scripts/utils";

import NavLink from "#parts/core/nav.link.svelte";
import NavDropLink from "#parts/core/nav.link.drop.svelte";

</script>


<nav>
  <section class="left">
    <NavLink pict="pycobytes-icon.png" link={Site.root}>
      {#snippet body()}
        <span class="pyco-flavour left">pyco</span><span class="pyco-flavour centre">:</span><span class="pyco-flavour right">bytes</span>
      {/snippet}
    </NavLink>

    <NavLink text="duality" button={swapDuality} collapse={true}>
      {#snippet body()}
        <span class="material-symbols-outlined">
          {#if duality == "dark"} dark_mode {:else} light_mode {/if}
        </span>
      {/snippet}
    </NavLink>
  </section>

  <section class="right">
    <NavLink text="About" intern="synopsis" collapse={true} >
      <NavDropLink text="FAQ" intern="faq" />
      <NavDropLink text="Synopsis" intern="synopsis" />
      <NavDropLink text="decoded" intern="decoded" />
    </NavLink>

    <NavLink text="Issues" intern="issues" collapse={true} >
      <NavDropLink text="Index" intern="issues" />
      <NavDropLink text="Latest" intern="issues/{Site.issues[0].index}" />
      <NavDropLink text="Random" button={() => { window.location.href = pickRandomIssue() }} />
    </NavLink>

    <NavLink text="Contact" extern="https://github.com/Sup2point0/pycobytes/discussions" collapse={true} >
      <NavDropLink text="Discuss" extern="https://github.com/Sup2point0/pycobytes/discussions" />
      <NavDropLink text="Submit Idea" extern="https://github.com/Sup2point0/pycobytes/issues" />
      <NavDropLink text="Report Bug" extern="https://github.com/Sup2point0/pycobytes/issues" />
    </NavLink>

    <NavLink text="GitHub" extern="https://github.com/Sup2point0/pycobytes" collapse={true}
      pict="github-light.svg"
    />
  </section>
</nav>


<style lang="scss">

nav {
  width: 100%;
  padding: 0 5rem;
  position: fixed;
  top: 0;
  z-index: 20;
  display: flex;
  flex-direction: row;
  justify-content: space-between;
  align-items: center;
  flex-wrap: nowrap;
  gap: 0.5rem;
  background: rgb(black, 70%);
  backdrop-filter: blur(12px);
  border-bottom: 1px solid $col-deut;
  transition: #{fade-duality()};
}

section {
  padding: 0;
  display: flex;
  flex-direction: row;
  align-items: center;
  flex-wrap: nowrap;
  gap: 0.4rem;
}

</style>
