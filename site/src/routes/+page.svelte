<script>

import { base } from "$app/paths";

import site from "#src/site-config.js";
import ISSUES from "#src/issues-config";

import LinkButton from "#src/parts/LinkButton.svelte";

import Content from "#src/routes/flavour-code.svx";

</script>


<svelte:head>
  <title> pycobytes · {site.desc.short} </title>
  <script defer src="/src/scripts/prism.js"> </script>
</svelte:head>

<main>
  <div class="hero left">
    <h1> <span class="pyco-flavour"> pyco:bytes </span> </h1>
    <span class="caption"> {site.desc.long} </span>
  </div>

  <LinkButton link="{base}/issues/{ISSUES[ISSUES.length - 1]}"> Read the latest issue </LinkButton>

  <div class="flavour right">
    <h2> Python is awesome. </h2>
    <p> But much of its stacks of fascinating quirks, tricks, and other syntactic sugar good stuff tend to be hidden amidst ancient Stack Overflow posts and questionable reddit threads, which makes discovering it quite nontrivial. </p>
  </div>

  <div class="flavour-code">
    <Content />
    <span class="caption"> Looks scary, right? Don’t worry, we’ll be delving into all this deliciousness ;D </span>
  </div>

  <div class="flavour left">
    <h2> So, here’s <span class="pyco-flavour">pycobytes</span>. </h2>
    <p> A weekly series where we delve into interesting and useful features in Python. This isn’t a comprehensive overview of the language by any means, but I share all the cool stuff I’ve discovered through years of adventuring. </p>
  </div>

  <div class="flavour">
    <h2> An adventure into the wonders of Python. </h2>
    <p> Quick, snappy and fun! </p>
  </div>

  <LinkButton link="{base}/issues">
    Start Exploring
  </LinkButton>
</main>


<style lang="scss">

main {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
}

p {
  @include font-flavour;
  // margin: 3em 8rem;
  font-size: 120%;
}

.left { text-align: left }
.right { text-align: right }

.hero {
  width: 100%;
  padding: 5rem 0 10rem 20vw;
  color: white;
  background-color: black;

  & h1 {
    font-family: 'Roboto Mono', 'Fira Code', 'Consolas', 'Overpass', 'Segoe UI Semibold#', system-ui, sans-serif;
  }
}

</style>
