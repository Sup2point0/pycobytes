<!-- @component Pycobytes

Displays `pyco:bytes` with the canonical theming.
-->

<script lang="ts">

interface Props {
  size?: string;
}

let { size = "100%" }: Props = $props();

</script>


<span class="pyco-flavour" style:font-size={size}>
  pyco<span class="pyco-flavour-null">:</span>bytes
</span>


<style lang="scss">

.pyco-flavour {
  padding: 0;  // override parent
  display: block;
  font-family: 'Geologica', 'Fira Mono', 'Consolas', 'Overpass', 'Segoe UI Semibold', system-ui, sans-serif;
  font-weight: 400;
  color: transparent;
  background: linear-gradient(to right in oklch,
    $lilac-nova,
    $blue-cresc,
  );
  -webkit-background-clip: text;
  background-clip: text;
}

.pyco-flavour-null {
  color: rgb(128 128 128 / 50%);
}

</style>
