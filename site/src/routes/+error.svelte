<script>

import Meta from "#parts/core/meta.svelte";
import Header from "#parts/core/header.svelte";
import Main from "#parts/core/main.svelte";

</script>


<Meta title="Error" />

<Header title="Error" />

<Main>
  <div style:text-align="center">
    <p class="error"> Oops, something has gone wrong! </p>
    <br>
    <p> If a link sent you here, I'm probably still working on the page, please bear with me! </p>
    <br>
    <p> If you think it might be an obscure or serious issue, <a target="_blank" href="https://github.com/Sup2point0/pycobytes/issues">let me know on GitHub</a>. </p>
  </div>
</Main>


<style lang="scss">

@use './src/styles/links' as *;

</style>
  