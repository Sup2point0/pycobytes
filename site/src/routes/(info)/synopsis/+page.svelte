<script>

import { page } from "$app/stores";

import Content from "./~content.svx";

import Main from "#parts/core/main.svelte";

</script>


<svelte:head>
  <title> {$page.data.title ?? "404 Not Found"} · pycobytes </title>
</svelte:head>


<article>
  <Main>
    <Content />
  </Main>
</article>
