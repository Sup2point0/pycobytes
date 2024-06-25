<script lang="ts">

export let type: "issue" | null = null;
export let issueIndex: string | null = null;
export let title: string;
export let caption: string | null = null;
export let tags: string[] = [];

</script>


<header>
  <div class="dark-overlay">
    {#if type == "issue"}
      <code> #{issueIndex} </code>
      <h1 class="pyco-flavour"> {@html title} </h1>
      <p> {@html caption} </p>
    {:else}
      <h1> {@html title} </h1>
    {/if}

    <ul>
      {#each tags as tag}
        <li> {tag} </li>
      {/each}
    </ul>
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
  padding: ($nav-height + 3rem) 0 2.5rem;
  background: linear-gradient(to right in srgb, rgba(black, 0.5), black var(--overlay));

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

</style>
