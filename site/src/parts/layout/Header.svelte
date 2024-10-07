<script lang="ts">

import { page } from "$app/stores";

export let type: "issue" | null = null;
export let title: string | undefined = undefined;

</script>


<header>
  <div class="dark-overlay">
    {#if type === "issue"}
      <code> #{$page.data.index} </code>
      <h1 class="pyco-flavour"> {@html $page.data.head} </h1>

      <ul>
        {#each $page.data.shard ?? [] as shard}
          <li class={shard}> {shard} </li>
        {/each}
      </ul>

    {:else}
      <h1> {@html title} </h1>
    
    {/if}

    <slot />
    
  </div>
</header>


<style lang="scss">

header {
  margin-top: 0rem;
  margin-bottom: 2rem;
  text-align: center;
  background-color: $blue-night;
  background-image: url("/pycobytes-back.png");
  background-size: 80%;
  background-repeat: no-repeat;
}

.dark-overlay {
  width: 100%;
  height: 100%;
  padding: ($nav-height + 2rem) 0 2.5rem;
  background: linear-gradient(to right in srgb, rgba(black, 0.5), black 69%);

  &:hover {
  }
}

code {
  font-size: 125%;
  color: light-dark($col-flavour, $col-accent);
}

h1 {
  @include font-head;
  padding: 1rem 0 1.5rem;
  margin: 0;
  font-size: 300%;

  &:not(.pyco-flavour) {
    // color: light-dark($col-accent, $col-flavour);
    color: white;
  }
}

p {
  @include font-flavour;
  margin: 0;
  font-size: 150%;
  color: white;
}

ul {
  margin-top: 4rem;
  padding: 0;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  list-style-type: none;
}

li {
  @include font-flavour;
  margin: 0 0.2rem;
  padding: 0.25em 0.8em;
  color: white;
  background-color: rgba($col-accent, 0.42);
  border-radius: 1rem;

  transition: all 0.12s ease-out;

  &:hover {
    background-color: $pink-elec;
  }

  &:not(:hover) {
    &.syntax { background-color: rgba($pink-spirit, 0.69); }
    &.tricks { background-color: rgba($lilac-nova, 0.69); }
    &.quickies { background-color: rgba($blue-sky, 0.69); }
    &.challenge { background-color: rgba($teal-elec, 0.69); }
  }
}

</style>
