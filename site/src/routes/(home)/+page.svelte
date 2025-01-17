<script>

import Site from "#src/site";

import processAnimations from "#scripts/anim";

import FlavourCode from "./flavour-code.svx";
import Clicky from "./clicky.svelte";

import FlavourButton from "#src/routes/(home)/button.flavour.svelte";

import { onMount } from "svelte";
import { base } from "$app/paths";


const issues = Object.values(Site.issues);

onMount(processAnimations);

</script>


<svelte:head>
  <title> pycobytes · {Site.desc.short} </title>
</svelte:head>

<main>
  <section class="hero">
    <div class="dark-overlay">
      <div class="left anim init-only">
        <h1 class="pyco-full-flavour"> pyco:bytes </h1>
        <p> {Site.desc.long} </p>
        <div class="line"></div>
      </div>

      <div class="right">
        <FlavourButton text="Read the latest issue &thinsp; 🡪"
          intern="issues/{issues[0].index}"
        />
      </div>
    </div>

    <div style="width: max-content; position: absolute; right: 12vw; bottom: 20px; padding: 1rem; background: #145090; color: white; font-family: 'Sen';">
      Heads up: I’m still migrating the site to Svelte 5, so there may be issues. We’ll be back up soon!
    </div>
  </section>

  <section class="right anim on-scroll init-only">
    <h2 class="pyco-full-flavour" style:--anim-offset="-12"> Python is awesome. </h2>
    <p> But much of its stacks of fascinating quirks, tricks, and other syntactic sugar good stuff tend to be hidden amidst ancient Stack Overflow posts and questionable reddit threads, which makes discovering it quite nontrivial. </p>
  </section>

  <section class="flavour-code">
    <FlavourCode />
    <br>
    <span class="caption"> Looks scary, right? Don’t worry, we’ll be delving into all this deliciousness ;D </span>
  </section>

  <section class="left anim on-scroll init-only">
    <h2 class="pyco-full-flavour" style:--anim-offset="-24"> So, here’s pycobytes. </h2>
    <p> A weekly series where we delve into interesting and useful features in Python. This isn’t a comprehensive overview of the language by any means, but I share all the cool stuff I’ve discovered through years of adventuring. </p>
  </section>

  <div class="line"></div>

  <section class="anim on-scroll init-only">
    <h2 class="pyco-full-flavour" style:--anim-offset="-36"> An adventure into the wonders of Python. </h2>
    <p> Quick, snappy and fun! </p>
  </section>

  <div class="line"></div>

  <div style:padding="2rem 0">
    <FlavourButton text="Start Exploring"
      intern="issues"
    />
  </div>

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
    padding: 2rem 0;
  }
  
  & h2 {
    @include font-head;
    padding: 0 0 0.5em; // down here to override font-head
    font-weight: 350;
    font-size: 300%;

    &.pyco-full-flavour {
      animation-delay: calc(var(--anim-offset) * 1s);
    }
  }

  & p {
    @include font-body;
    font-size: 150%;
    color: light-dark($grey-ocean, $grey-swallow);
  }

  & .caption {
    @include font-ui;
    font-size: 120%;
  }
}

.left { text-align: left }
.right { text-align: right }

.line {
  width: 42vw;
  max-width: 42vw;
  margin: 2rem 0;
  border-bottom: 1px solid light-dark($col-deut, white);
}

.hero {
  width: 100%;
  height: 100%;
  margin: 0 0 4rem;
  background-color: $blue-night;
  background-image: url('/pycobytes-back.png');
  background-size: cover;
  background-repeat: no-repeat;

  .dark-overlay {
    width: 100%;
    height: 100%;
    padding: 5rem 0;
    display: flex;
    flex-direction: column;
    align-items: center;
    text-align: center;
    background: linear-gradient(to right in srgb, black 20%, rgba(black, 0.2));
  }
}
.hero .left {
  width: 100%;
  padding: 4rem 0 0 10vw;

  & h1 {
    width: 100%;
    margin: 0 -0.05em 2rem;
    padding: 0;
    font-family: 'Geologica', 'Fira Mono', 'Consolas', 'Overpass', 'Segoe UI Semibold', system-ui, sans-serif;
    font-weight: 100;
    font-size: max(10vw, 4rem);
  }

  & p {
    @include font-ui;
    font-size: 200%;
    color: white;
  }
  
  & .line {
    max-width: max(20vw, 20rem);
    padding-top: 5rem;
  }
}
.hero .right {
  width: 100%;
  padding-right: 10vw;
  display: flex;
  justify-content: end;
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
}

</style>
