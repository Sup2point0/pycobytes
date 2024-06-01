<script>

import Nav from "$lib/parts/Nav.svelte";
import Footer from "$lib/parts/Footer.svelte";

</script>


<Nav />

<slot />

<Footer />


<style lang="scss">

@import '$lib/styles/essence.scss';

</style>
