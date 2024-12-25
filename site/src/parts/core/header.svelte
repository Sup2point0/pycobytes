<script lang="ts">

import { page } from "$app/stores";

interface Props {
  type?: "issue" | undefined;
  title?: string;
  desc?: string;
  children?: any;
}

let { type, title, desc, children }: Props = $props();

</script>


<header>
  <div class="dark-overlay">
    {#if type === "issue"}
      <code> #{$page.data.index} </code>
      <h1 class="pyco-full-flavour"> {@html $page.data.head} </h1>

      <ul class="shards">
        {#each $page.data.shard ?? [] as shard}
          <li class={shard}> {shard} </li>
        {/each}
      </ul>

    {:else}
      <h1> {@html title} </h1>
      {#if desc}
        <p class="caption"> {@html desc} </p>
      {/if}
    
    {/if}

    {@render children?.()}
  </div>
</header>


<style lang="scss">

header {
  margin: 0 0 2rem;
  position: relative;
  text-align: center;
  background-color: $blue-night;
  background-image: url("/pycobytes-back.png");
  background-size: 80%;
  background-repeat: no-repeat;
}

.dark-overlay {
  width: 100%;
  height: 100%;
  padding: 4rem 0 3rem;
  background: linear-gradient(to right in srgb, rgb(black, 50%), black 69%);
}


code {
  font-size: 125%;
  color: light-dark($col-deut, $col-prot);
}

h1 {
  @include font-head;
  padding: 1rem 0 1.5rem;
  margin: 0;
  font-size: 300%;

  &:not(.pyco-full-flavour) {
    color: white;
  }
}

p {
  @include font-ui;
  margin: 0;
  font-size: 150%;
  color: white;
}

ul.shards {
  margin: 3rem 0 1rem;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  list-style: none;
}

li {
  @include font-ui;
  margin: 0 0.2rem;
  padding: 0.25em 0.8em;
  color: white;
  background-color: rgb($col-prot, 42%);
  border-radius: 1em;

  transition: all 0.12s ease-out;

  &:hover {
    cursor: pointer;
    background-color: $pink-elec;
  }

  &:not(:hover) {
    &.syntax { background-color: rgb($pink-spirit, 69%); }
    &.tricks { background-color: rgb($lilac-nova, 69%); }
    &.quickies { background-color: rgb($blue-sky, 69%); }
    &.challenge { background-color: rgb($teal-elec, 69%); }
  }
}

</style>
