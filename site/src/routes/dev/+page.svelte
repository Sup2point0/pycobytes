<script>

import Header from "#src/parts/Header.svelte";
import Main from "#src/parts/Main.svelte";

// const source = await import("/content.md");
// const content = source.default;

</script>


<svelte:head>
  <title> Hacking the Mainframe · About · pycobytes </title>
</svelte:head>

<Header
  title = "Hacking the Mainframe"
  caption = "Deep dive into the internals"
/>

<Main>
  <article>
    {#if content}
      {content}
    {:else}
      <p> Uh, something went wrong! </p>
    {/if}
  </article>
</Main>
