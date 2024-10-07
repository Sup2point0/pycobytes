<script>

import Header from "#parts/layout/Header.svelte";
import Main from "#parts/layout/Main.svelte";

import Content from "../dev/_Content.svx";

</script>


<svelte:head>
  <title> Hacking the Mainframe · About · pycobytes </title>
</svelte:head>

<article>
  <Header
    title = "Hacking the Mainframe"
    caption = "Deep dive into the internals"
  />

  <Main>
      <Content />
  </Main>
</article>
