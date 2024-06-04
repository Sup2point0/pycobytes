<script>

import { base } from "$app/paths";

import site from "$src/site-config.js";

</script>


<svelte:head>
  <title> pycobytes • {site.desc.short} </title>
</svelte:head>

<div class="header">
  <img id="welcome" alt="welcome to pycobytes" src="{base}/pycobytes-welcome.png">
</div>

<main>
  <p> Python is awesome. But much of its stacks of fascinating quirks, tricks, and other syntactic sugar good stuff tend to be hidden amidst ancient Stack Overflow posts and questionable reddit threads, which makes discovering it quite nontrivial. </p>
  
  <img id="glimpse" alt="pythonic magic" src="{base}/pycobytes-glimpse.png">

  <p> So, <span class="pyb-flavour left">pyco</span><span class="pyb-flavour centre">:</span><span class="pyb-flavour right">bytes</span> is a weekly series where we delve into interesting and useful features in Python. This isn’t a comprehensive overview of the language by any means, but I share all the cool stuff I’ve discovered through years of adventuring. </p>
</main>


<style lang="scss">

p {
  @include font-flavour;
  margin: 3em 8rem;
  font-size: 120%;
}

.header {
  padding-top: 4rem;
  background-color: $blue-night;
}

.header img {
  width: 100%;
}

</style>
