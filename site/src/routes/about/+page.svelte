<script>

import Header from "$src/parts/Header.svelte";
import Article from "$src/parts/Article.svelte";

</script>


<svelte:head>
  <title> {data.title ?? "404"} · pycobytes[{data.issueIndex ?? "?"}] </title>
</svelte:head>

<article>
  <Header title="pyco:bytes" />

  <Article>
  </Article>
</article>
