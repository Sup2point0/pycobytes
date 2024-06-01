<script>

import Header from "$lib/parts/Header.svelte";

export let data;

async function load({ params }) {
  const route = `$lib/exported/${params.issueIndex}.md`;
  const issue = await import(route);

  const { title, index, date } = issue.metadata;
  const content = issue.default;

  return { content, title, index, date }
}

</script>


<article>
  <Header title="{data.title}" date={data.date} />

  {#if data.content}
    <svelte:component this={data.content} />
  {:else}
    <h1> ERROR </h1>
  {/if}
</article>
