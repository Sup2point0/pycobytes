<script>

import Header from "#parts/layout/Header.svelte";
import Main from "#parts/layout/Main.svelte";

import Content from "../../../../faq.md";

</script>


<svelte:head>
  <title> FAQ · pycobytes </title>
</svelte:head>

<article>
  <Header title="Fervently Anticipated Questions" />

  <Main>
    <Content />
  </Main>
</article>
