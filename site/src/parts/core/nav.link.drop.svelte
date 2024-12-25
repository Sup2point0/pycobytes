<!-- @component NavDropLink

-->

<script lang="ts">

import { base } from "$app/paths";

interface Props {
  text?: string;
  link?: string;
    intern?: string;
    extern?: string;
  button?: () => void;
}

let { text, link, intern, extern, button }: Props = $props();

</script>


{#if button}
  <button class="nav-drop-link" onclick={button}>
    {text}
  </button>

{:else}
  <a class="nav-drop-link"
    href={link || extern || `${base}/${intern}`}
    target={extern ? "_blank" : "_self"}
  >
    {text}
  </a>

{/if}


<style lang="scss">

.nav-drop-link {
  padding: 0.5em;
  display: block;
  
  @include font-ui;
  color: $col-text;
  text-decoration: none;
  text-align: left;
  background: none;
  border: none;
  border-radius: 0.5em;
  transition: #{fade-duality()}, #{fade-interact()};

  &:hover, &:focus {
    cursor: pointer;
    background-color: $col-hover;
  }

  &:active {
    cursor: pointer;
    background-color: $col-click;
  }
}

</style>
