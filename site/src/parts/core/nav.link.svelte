<!-- @component `NavLink`

A link in the navbar. Dropdown links can be provided as `NavDropLink` children.
-->

<script lang="ts">

import { duality } from "#scripts/stores";

import { base } from "$app/paths";


interface Props {
  text?: string;
    body?: any;
  pict?: string | {
    light?: string;
    dark?: string;
  };
  link?: string;
    intern?: string;
    extern?: string;
  button?: () => void;
  collapse?: boolean;
  children?: any;
}

let {
  text, body,
  pict,
  link, intern, extern,
  button,
  collapse,
  children,
}: Props = $props();

</script>


{#snippet content()}
  {#if pict}
    <img alt="" src="{base}/{
      typeof pict === 'string' ? pict
      : duality === 'light' ? pict.light : pict.dark
    }" />
  {/if}

  {#if body}
    {@render body()}
  {:else if text}
    <p> {text} </p>
  {/if}
{/snippet}


<div class="nav-link {collapse}">
  {#if button}
    <button id={text} class="trigger" onclick={button}>
      {@render content()}
    </button>
  {:else}
    <a class="trigger"
      href={link || extern || `${base}/${intern}`}
      target={extern ? "_blank" : "_self"}
    >
      {@render content()}
    </a>
  {/if}

  {#if children}
    <div class="nav-dropdown">
      {@render children()}
    </div>
  {/if}
</div>


<style lang="scss">

.nav-link {
  padding: 0.25em 0;
}

.trigger {
  padding: 0.75em;
  &:has(img) { padding: 0.25em 0.5em; }
  display: flex;
  justify-content: center;
  align-items: center;
  text-decoration: none;
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

  p {
    @include font-ui;
    color: white;
  }

  img {
    max-height: 1.75em;
  }

  img ~ p {
    padding-left: 0.5em;
    padding-right: 0.5em;
  }
}


.nav-dropdown {
  min-width: 5em;
  margin-top: 2px;
  padding: 0.5em;
  position: absolute;
  z-index: 22;
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  visibility: hidden;
  opacity: 0;

  background: black;
  border-bottom-left-radius: 0.5em;
  border-bottom-right-radius: 0.5em;
  box-shadow: 0 4px 2px -2px rgb(black, 10%);
  transform: translateY(-0.4em);
  
  .nav-link:is(:hover, :focus) &,
  &:hover {
    display: flex;
    flex-direction: column;
    visibility: visible;
    opacity: 1;
    transform: none;
  }
}


button#duality {
  color: light-dark($col-prot, $lilac-nova);
}

</style>
