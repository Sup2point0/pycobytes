<!-- @component
The global site navigation bar.
-->

<script>

import { base } from "$app/paths";
import NavLink from "#parts/nav/NavLink.svelte";

import ISSUES from "#src/issues-config";
import duality from "#scripts/duality";
import { swapDuality } from "#scripts/duality";


const pyco = "<span class=\"pyb-flavour left\">pyco</span><span class=\"pyb-flavour centre\">:</span><span class=\"pyb-flavour right\">bytes</span>"


function pickIssue() {
  let index = ISSUES[Math.random() * ISSUES.length | 0].issueIndex;
  window.location.href = `${base}/issues/${index}`;
}

</script>


<nav>
  <ul class="left">
    <NavLink text="i" pict="{base}/pycobytes-icon.png" link="https://sup2point0.github.io/pycobytes" />
    <NavLink body={pyco} link="https://sup2point0.github.io/pycobytes" />

    <NavLink text="duality" button={swapDuality} collapsible={true}>
      <span class="material-symbols-outlined">
        {#if $duality == "dark"}
          dark_mode
        {:else}
          light_mode
        {/if}
      </span>
    </NavLink>
  </ul>

  <ul class="right">
    <NavLink text="About" link="{base}/faq" collapsible={true} >
      <NavLink text="FAQ" link="{base}/faq" />
      <NavLink text="Synopsis" link="{base}/dev" />
      <NavLink text="decoded" link="{base}/edu" />
    </NavLink>

    <NavLink text="Issues" link="{base}/issues" collapsible={true} >
      <NavLink text="Index" link="{base}/issues" />
      <NavLink text="Latest" link="{base}/issues/{ISSUES[ISSUES.length -1].issueIndex}" />
      <NavLink text="Random" button={pickIssue}>
        Random
      </NavLink>
    </NavLink>

    <NavLink text="Contact" extern="https://github.com/Sup2point0/pycobytes/discussions" collapsible={true} >
      <NavLink text="Discuss" extern="https://github.com/Sup2point0/pycobytes/discussions" />
      <NavLink text="Submit Idea" extern="https://github.com/Sup2point0/pycobytes/issues" />
      <NavLink text="Report Bug" extern="https://github.com/Sup2point0/pycobytes/issues" />
    </NavLink>

    <NavLink text="GitHub"
      light="{base}/github-dark.svg"
      dark="{base}/github-light.svg"
      extern="https://github.com/Sup2point0/pycobytes"
      collapsible={true}
    />
  </ul>
</nav>


<style lang="scss">

nav {
  position: fixed;
  top: 0;
  z-index: 2;
  width: 100%;
  max-width: 100%;
  height: $nav-height;
  min-height: $nav-height;
  max-height: $nav-height;
  padding: 0.1rem 4rem 0.1rem auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  background-color: $col-idle;
  border-bottom: 2px solid $col-flavour;
  @include fade-duality;
}

nav ul {
  display: flex;
  flex-direction: row;
  padding-right: 2rem;
}

ul {
  margin: 0;
  list-style-type: none;
}

</style>
