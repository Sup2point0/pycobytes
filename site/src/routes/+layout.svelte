<script>

import "#styles/essence.scss";
import "#styles/prism-night-owl.scss";
import "#styles/a11y.scss";

import { duality, setFromLocalDuality } from "#scripts/stores";

import Nav from "#parts/core/nav.svelte";
import Footer from "#parts/core/footer.svelte";

import { browser } from "$app/environment";


let { children } = $props();


// let currentDuality = (
//   $derived($duality ? ($duality == "dark" ? "dark" : "light")
//   : browser ? setFromLocalDuality(window) : "light")
// );

</script>


<div class="duality-container"
>
<!-- style="color-scheme: {currentDuality}" -->
  <Nav />

  {#if children}
    {@render children()}
  {:else}
    <p> Uh, something has gone really wrong! </p>
  {/if}

  <Footer />
</div>
