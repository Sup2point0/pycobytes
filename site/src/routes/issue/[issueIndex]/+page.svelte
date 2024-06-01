<script>

import Header from "$lib/parts/Header.svelte";

export let data;

let content;
if (data.issueIndex) {
  content = import(`$lib/export/${data.issueIndex}.md`);
} else {
  content = {}
}

</script>

<article>
  <Header title="test" />

  {#if content}
    <svelte:component this={content.default} />
  {:else}
    <h1> ERROR </h1>
  {/if}
</article>
