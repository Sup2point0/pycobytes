<script>

import { base } from "$app/paths";

import site from "#src/site-config";
import ISSUES from "#src/issues-config";

import LinkButton from "#src/parts/LinkButton.svelte";

import Content from "#src/routes/flavour-code.svx";

</script>


<svelte:head>
  <title> pycobytes · {site.desc.short} </title>
  <script defer src="/src/scripts/prism.js"> </script>
</svelte:head>

<main>
  <section class="hero">
    <div class="left">
      <h1> <span class="pyco-flavour"> pyco<span class="pyco-flavour-null">:</span>bytes </span> </h1>
      <p> {site.desc.long} </p>
      <div class="line" />
    </div>

    <LinkButton link="{base}/issues/{ISSUES[ISSUES.length - 1].issueIndex}">
      Read the latest issue <span class="material-symbols-outlined"> arrow_forward_ios </span>
      <span slot="hover">
        {#each {length: 3} as _, i}
          <span class="material-symbols-outlined"> arrow_forward_ios </span>
        {/each}
      </span>
    </LinkButton>
  </section>

  <section class="right">
    <h2 class="pyco-flavour"> Python is awesome. </h2>
    <p> But much of its stacks of fascinating quirks, tricks, and other syntactic sugar good stuff tend to be hidden amidst ancient Stack Overflow posts and questionable reddit threads, which makes discovering it quite nontrivial. </p>
  </section>

  <section class="flavour-code">
    <Content />
    <span class="caption"> Looks scary, right? Don’t worry, we’ll be delving into all this deliciousness ;D </span>
  </section>

  <section class="left">
    <h2 class="pyco-flavour"> So, here’s pycobytes. </h2>
    <p> A weekly series where we delve into interesting and useful features in Python. This isn’t a comprehensive overview of the language by any means, but I share all the cool stuff I’ve discovered through years of adventuring. </p>
  </section>

  <section>
    <h2 class="pyco-flavour"> An adventure into the wonders of Python. </h2>
    <p> Quick, snappy and fun! </p>
  </section>

  <LinkButton link="{base}/issues">
    Start Exploring <span class="material-symbols-outlined"> arrow_forward_ios </span>
    <span slot="hover">
      {#each {length: 3} as _, i}
        <span class="material-symbols-outlined"> arrow_forward_ios </span>
      {/each}
    </span>
  </LinkButton>

  <section>
    <img id="xkcd" alt="XKCD 353" title="XKCD 353" src="https://imgs.xkcd.com/comics/python.png">
    <p> <a href="https://xkcd.com/353"><em>XKCD, 353</em></a> </p>
  </section>
</main>


<style lang="scss">

main {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  overflow: hidden;
  
  counter-reset: sec;
}

section {
  width: 80vw;
  margin: 0 0 4rem;
  counter-increment: sec;

  &:not(.hero) {
    width: 69%;
    max-width: 69%;
  }
  
  & h2 {
    @include font-head;
    margin: 0;
    padding: 0;
    font-size: 300%;

    &.pyco-flavour {
      animation-delay: calc(counter(sec) * -13s);
    }
  }

  & p {
    @include font-flavour;
    font-size: 150%;
    color: $grey-nova;
  }
}

.left { text-align: left }
.right { text-align: right }

.hero {
  width: 100%;
  padding-bottom: 5rem;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  color: white;
  background-color: black;
}

.hero .left {
  width: 100%;
  padding: 4rem 0 4rem 20vw;

  & h1 {
    margin: 0 0 2rem;
    padding: 0;
    font-family: 'Roboto Mono', 'Fira Code', 'Consolas', 'Overpass', 'Segoe UI Semibold#', system-ui, sans-serif;
    font-size: 10vw;
  }
  & p {
    @include font-flavour;
    font-size: 2vw;
    margin: 0;
    padding: 0;
    color: white;
  }
  & .line {
    width: 20vw;
    max-width: 20vw;
    padding-top: 5rem;
    border-bottom: 3px solid light-dark($col-flavour, $col-accent);
  }
}

#xkcd {
  width: 50vw;
  max-width: 100vw;
  margin-top: 3rem;
}

</style>
