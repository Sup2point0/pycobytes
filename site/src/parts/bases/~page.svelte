<script>

import { page } from "$app/stores";

import Content from "./%{file}.svx";

import Header from "#parts/layout/Header.svelte";
import Main from "#parts/layout/Main.svelte";

</script>


<svelte:head>
  <title> {$page.data.title ?? "404 Not Found"} · pycobytes </title>
</svelte:head>


<article>
  <Main>
    <Content />
  </Main>
</article>
