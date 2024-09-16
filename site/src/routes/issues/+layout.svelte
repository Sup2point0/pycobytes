<script>

import { page } from "$app/stores";

</script>


<svelte:head>
  <title> {$page.data.titleText ?? "404 Not Found"} · pycobytes[{$page.data.issueIndex ?? "?"}] </title>
</svelte:head>
