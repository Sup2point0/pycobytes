<script lang="ts">

import Header from "#parts/core/header.svelte";

import { page } from "$app/stores";

interface Props {
  children?: import('svelte').Snippet;
}

let { children }: Props = $props();

</script>


<Header
  title={$page.data.head ?? "404 Not Found"}
  desc={$page.data.desc}
/>

{#if children}
  {@render children?.()}
{:else}
  <p class="error"> Uh, something went wrong! </p>
{/if}
