<!-- @component FlavourButton

A really *nice* button.
-->

<script lang="ts">

import { base } from "$app/paths";

interface Props {
  text: string;
  intern: string;
}

let { text, intern }: Props = $props();

</script>


<a href="{base}/{intern}">
  <span class="content"> {text} </span>
</a>


<style lang="scss">

a {
  width: max-content;
  $margin: 2px;
  display: block;
  position: relative;
  z-index: 1;
  background-clip: padding-pox;
  border: $margin solid transparent;
  border-radius: 2em;
  text-decoration: none;

  span.content {
    display: block;
    padding: 0.8em 2em 0.75em;
    @include font-ui;
    font-size: 120%;
    color: white;
    background: black;
    border-radius: inherit;
    transition: all 0.4s cubic-bezier(0.19, 1, 0.22, 1);  // ease-out-exp
  }

  &::before {
    content: '';
    margin: -$margin;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;
    z-index: -1;
    background: linear-gradient(
      109deg in oklch,
      $teal-elec,
      $blue-nova,
      $lilac-nova,
      $pink-elec,
      $red-nova,
      $orange-spirit,
      $yellow-solar,
    ) 0 0 / 200% no-repeat;
    border-radius: inherit;
    transition: all 1.8s cubic-bezier(0.19, 1, 0.22, 1);  // ease-out-exp
  }
}

a:hover {
  span.content {
    padding-left: 2.5em;
    padding-right: 2.5em;
    background: none;
  }

  &::before {
    background-position-x: 100%;
  }
}

</style>
