<script>

import Header from "#src/parts/Header.svelte";
import Main from "#src/parts/Main.svelte";
import Content from "../dev/_Content.svx";

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
    <Content />
  </article>
</Main>
