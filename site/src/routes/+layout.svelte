<script lang="ts">

import "#styles/essence.scss";
import "#styles/prism-night-owl.scss";
import "#styles/a11y.scss";

import * as cookies from "cookie";

import { prefs } from "#scripts/stores";

import Nav from "#parts/core/nav.svelte";
import Footer from "#parts/core/footer.svelte";

import { onMount } from "svelte";
import { browser } from "$app/environment";


let { children, data } = $props();


let client = false;

onMount(() => {
  if (browser) {
    client = true;
    let current = cookies.parse(document.cookie)?.duality;

    if (current === undefined) {
      let pref = (
        window.matchMedia?.("(prefers-color-scheme: dark)").matches
        ? "light" : "dark"
      );
      document.cookie = cookies.serialize("duality", pref, { path: "/" });
    }
  }
})

</script>


<div class="duality-container"
  style="color-scheme: {client ? prefs.duality : data.duality}"
>
  <Nav />

  {#if children}
    {@render children()}
  {:else}
    <p> Uh, something has gone really wrong! </p>
  {/if}

  <Footer />
</div>


<style lang="scss">

.duality-container {
  background: light-dark(white, $blue-night);
}

</style>
