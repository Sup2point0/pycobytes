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
  action?: () => void;
  collapse?: boolean;
  children?: any;
}

let {
  text, body,
  pict,
  link, intern, extern,
  action,
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


<div class="nav-link" class:collapse>
  {#if action}
    <button id={text} class="trigger" onclick={action}>
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
    <div class="dropdown">
      <div class="dropdown-content">
        {@render children()}
      </div>
    </div>
  {/if}
</div>


<style lang="scss">

.nav-link {
  padding: 0.25em 0;
}

.trigger {
  padding: 0 1em;
  &:has(img) { padding: 0 0.5em; }
  display: flex;
  justify-content: center;
  align-items: center;
  text-decoration: none;
  background: transparent;
  border: none;
  border-radius: 0.5em;
  transition: #{fade-duality()}, #{fade-interact()};

  p {
    padding: 0.75em 0;
    @include font-ui;
    color: white;
    transition: #{fade-interact()};
  }

  img {
    // margin-top: -3px;
    max-height: 1.6em;
  }

  img ~ p {
    padding-left: 0.5em;
  }

  &:hover, &:focus {
    cursor: pointer;
    background: rgb(black, 20%);

    p {
      color: $col-prot;
    }
  }

  &:active {
    cursor: pointer;
    background-color: rgb(white, 8%);
  }
}

@media (max-width: 5rem) {
  .nav-link.collapse {
    display: none;
  }
}


.dropdown {
  min-width: 5em;
  position: absolute;
  z-index: 22;
  display: flex;
  flex-direction: column;
  gap: 0.2rem;
  visibility: hidden;
  opacity: 0;
  transition: opacity 0.2s ease;
  
  .nav-link:is(:hover, :focus, :focus-within) &,
  &:hover {
    display: flex;
    flex-direction: column;
    visibility: visible;
    opacity: 1;
    transform: none;
  }
}

.dropdown-content {
  padding: 0.5em 0.5em 0.75em 0.5em;
  background: rgb($blue-night, 80%);
  outline: 1.5px solid white;
  // backdrop-filter: blur(12px);  // FIXME will need to use pseudoelement
  border-radius: 0.5em;
  transform: translateY(1.2em);
  transition: transform 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);

  .nav-link:is(:hover, :focus) .dropdown &,
  &:hover {
    transform: translateY(0.8em);
  }
}


button#duality {
  color: light-dark($col-deut, $lilac-nova);
}

</style>
