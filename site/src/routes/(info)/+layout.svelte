<script lang="ts">

import Header from "#parts/layout/Header.svelte";

import { page } from "$app/stores";

</script>

<Header title="{$page.data.title ?? "404 Not Found"}" />

<slot />
