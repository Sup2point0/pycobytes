<script>

import { base } from "$app/paths";
import NavLink from "#src/parts/NavLink.svelte";

import ISSUES from "#src/issues-config";
import duality from "#src/scripts/duality";
import { swapDuality } from "#src/scripts/duality";

function pickIssue() {
  let index = ISSUES[Math.random() * ISSUES.length | 0];
  window.location.href = `https://sup2point0.github.io/pycobytes/issues/${index}`;
}

</script>


<nav>
  <ul class="left">
    <NavLink text="i" pict="{base}/pycobytes-icon.png" link="https://sup2point0.github.io" />
    <NavLink text="pyco:bytes" link="https://sup2point0.github.io/pycobytes" />

    <NavLink text="duality" button={swapDuality}>
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
    <NavLink text="About" link="{base}/faq" >
      <NavLink text="FAQ" link="{base}/faq" />
      <NavLink text="Dev" link="{base}/dev" />
    </NavLink>

    <NavLink text="Issues" link="{base}/issues" >
      <NavLink text="Index" link="{base}/issues" />
      <NavLink text="Latest" link="{base}/issues/{ISSUES[ISSUES.length -1].issueIndex}" />
      <NavLink text="Random" button={pickIssue} />
    </NavLink>

    <NavLink text="Contact" collapsible = {true} >
      <NavLink text="Discuss" link="https://sup2point0.github.io/pycobytes/discussions" />
      <NavLink text="Submit Idea" link="https://sup2point0.github.io/pycobytes/issues" />
      <NavLink text="Report Bug" link="https://sup2point0.github.io/pycobytes/issues" />
    </NavLink>

    <NavLink text="GitHub"
      light="{base}/github-light.svg"
      dark="{base}/github-dark.svg"
      extern="https://github.com/Sup2point0/pycobytes" invertible = {true}
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
