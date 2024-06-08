<script>

import Header from "#src/parts/Header.svelte";
import Markdown from "#src/parts/Markdown.svelte";

export let data;

</script>


<svelte:head>
  <title> FAQ · pycobytes </title>
</svelte:head>

<article>
  <Header title="Fervently Anticipated Questions" />

  {data.text}

  <!-- <Markdown src="#src/routes/faq/content.md" /> -->
</article>
