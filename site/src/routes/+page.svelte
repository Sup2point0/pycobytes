<script>

import Site from "#src/site";

import processAnimations from "#scripts/anim";

import LinkButton from "#parts/LinkButton.svelte";
import Clicky from "#parts/Clicky.svelte";
import FlavourCode from "#src/routes/flavour-code.svx";

import { base } from "$app/paths";
import { onMount } from "svelte";


onMount(() => processAnimations());

</script>


<svelte:head>
  <title> pycobytes · {Site.desc.short} </title>
</svelte:head>

<main>
  <section class="hero">
    <div class="overlay">
      <div class="left anim init-only">
        <h1> <span class="pyco-flavour">
          pyco<span class="pyco-flavour-null">:</span>bytes
        </span> </h1>
        <p> {Site.desc.long} </p>
        <div class="line" />
      </div>

      <LinkButton link="{base}/issues/{Site.issues[Site.issues.length - 1].issueIndex}">
        Read the latest issue <span class="material-symbols-outlined"> arrow_forward_ios </span>
        <span slot="hover">
          {#each {length: 3} as _, i}
            <span class="material-symbols-outlined"> arrow_forward_ios </span>
          {/each}
        </span>
      </LinkButton>
    </div>
  </section>

  <section class="right anim on-scroll init-only">
    <h2 class="pyco-flavour" style:--anim-offset="-12"> Python is awesome. </h2>
    <p> But much of its stacks of fascinating quirks, tricks, and other syntactic sugar good stuff tend to be hidden amidst ancient Stack Overflow posts and questionable reddit threads, which makes discovering it quite nontrivial. </p>
  </section>

  <section class="flavour-code">
    <FlavourCode />
    <br>
    <span class="caption"> Looks scary, right? Don’t worry, we’ll be delving into all this deliciousness ;D </span>
  </section>

  <section class="left anim on-scroll init-only">
    <h2 class="pyco-flavour" style:--anim-offset="-24"> So, here’s pycobytes. </h2>
    <p> A weekly series where we delve into interesting and useful features in Python. This isn’t a comprehensive overview of the language by any means, but I share all the cool stuff I’ve discovered through years of adventuring. </p>
  </section>

  <div class="line" />

  <section class="anim on-scroll init-only">
    <h2 class="pyco-flavour" style:--anim-offset="-36"> An adventure into the wonders of Python. </h2>
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

  <Clicky />
</main>


<style lang="scss">

main {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  overflow: hidden;
}

section {
  width: 80vw;

  &:not(.hero) {
    width: 69%;
    max-width: 69%;
    margin: 2rem 0;
  }
  
  & h2 {
    @include font-head;
    margin: 0;
    padding: 0;
    font-size: 300%;

    &.pyco-flavour {
      animation-delay: calc(var(--anim-offset) * 1s);
    }
  }

  & p {
    @include font-flavour;
    font-size: 150%;
    color: light-dark($grey-storm, $grey-swallow);
  }

  & .caption {
    @include font-flavour;
    font-size: 120%;
  }
}

.left { text-align: left }
.right { text-align: right }

.line {
  width: 42vw;
  max-width: 42vw;
  margin: 2rem 0;
  border-bottom: 2px solid light-dark($col-flavour, white);
}

.hero {
  width: 100%;
  height: 100%;
  margin: 0 0 4rem;
  color: white;
  background-color: $blue-night;
  background-image: url("/pycobytes-back.png");
  background-size: cover;
  background-repeat: no-repeat;

  .overlay {
    width: 100%;
    height: 100%;
    padding-bottom: 5rem;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    background: linear-gradient(to right in srgb, black 20%, rgba(black, 0.2));
  }
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
    font-size: 200%;
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

.material-symbols-outlined {
  font-size: 1rem;
  vertical-align: middle;
}

/// NOTE putting animation styles here until needed on other pages
.anim {
  transition-property: opacity, transform;
  transition-duration: 1s;
  transition-timing-function: cubic-bezier(0.33, 1, 0.68, 1);
  transition-delay: 0.25s;

  &:not(.anim-in) {
    opacity: 0;
    &.left { transform: translateX(-3rem); }
    &.right { transform: translateX(3rem); }
    &:not(.left, .right) { transform: translateY(3rem); }
  }

  &.anim-in {
    opacity: 1;
    transform: translateX(0);
  }
}

#xkcd {
  width: 50vw;
  max-width: 100vw;
  margin-top: 3rem;
}

</style>
