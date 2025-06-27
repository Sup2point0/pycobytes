<!-- @component Nav

The global site navigation bar.
-->

<script lang="ts">

import * as cookies from "cookie";

import Site from "#src/site";
import { prefs } from "#scripts/stores";
import { pickRandomIssue } from "#scripts/utils";

import NavLink from "#parts/core/nav.link.svelte";
import NavDropLink from "#parts/core/nav.link.drop.svelte";

import Pycobytes from "#parts/misc/pyco.svelte";

import { goto } from "$app/navigation";

</script>


<nav>
  <section class="left">
    <NavLink link={Site.root}
      pict="pycobytes-icon.png"
    >
      {#snippet body()}
        <span style:padding="0.5em 0.25em">
          <Pycobytes size="1.25rem" />
        </span>
      {/snippet}
    </NavLink>

    <NavLink text="duality" action={() => {
      let current = cookies.parse(document.cookie)?.duality;
      let changed: "light" | "dark" = (current === "dark" ? "light" : "dark");

      prefs.duality = changed;
      document.cookie = cookies.serialize("duality", changed, { path: "/" });
    }}>
      {#snippet body()}
        <span class="material-symbols-outlined" style:padding="0.4em 0">
          {#if prefs.duality === "dark"}
            dark_mode
          {:else}
            light_mode
          {/if}
        </span>
      {/snippet}
    </NavLink>
  </section>

  <section class="right">
    <NavLink text="About" intern="synopsis" >
      <NavDropLink text="FAQ" intern="faq" />
      <NavDropLink text="decoded" intern="decoded" />
      <NavDropLink text="License" intern="license" />
      <NavDropLink text="Privacy" intern="privacy" />
    </NavLink>

    <NavLink text="Issues" intern="issues" collapse={true} >
      <NavDropLink text="Index" intern="issues" />
      <NavDropLink text="Latest" intern="issues/{Site.issues[0].index}" />
      <NavDropLink text="Random" button={() => goto(pickRandomIssue())} />
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
  flex-flow: row nowrap;
  justify-content: space-between;
  align-items: center;
  gap: 0.5rem;
  
  font-size: 110%;
  background: rgb($blue-night, 80%);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid $col-prot;
}

section {
  display: flex;
  flex-flow: row nowrap;
  align-items: center;
  gap: 0.4rem;
}

</style>
