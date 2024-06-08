<script>

import { onMount } from "svelte";

export let src;

let content;

async function loadContent() {
  let source = await import(/* @vite-ignore */ src);
  content = source.default;
  console.log(`content = ${content}`)
}

loadContent();

onMount(async () => {
  let source = await import(/* @vite-ignore */ src);
  content = source.default;
  console.log(`content = ${content}`)
});

</script>


{#if content}
  {content}
{:else}
  <p class="error" style:text-align="center"> A rendering error occurred! </p>
{/if}
