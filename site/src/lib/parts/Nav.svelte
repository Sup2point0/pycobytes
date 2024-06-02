<script>

import { base } from "$app/paths";

import { ISSUES } from "$lib/issues.config.js";

const navParts = [
  {
    align: "left", text: "pycobytes", pict: `${base}/pycobytes-title.png`,
    link: "https://sup2point0.github.io/pycobytes",
  },
].concat([
  {
    align: "right", text: "About",
    link: "https://sup2point0.github.io/pycobytes/about",
  },
  {
    align: "right", text: "Issues",
    dropdown: {
      { text: "Index",
        link: "https://sup2point0.github.io/pycobytes/issues" },
      { text: "Latest",
        link: `https://sup2point0.github.io/pycobytes/issues/${ISSUES[ISSUES.length -1]}` },
      { text: "Random",
        button: pickIssue },
    },
  },
  {
    align: "right", text: "Contact",
    dropdown: {
      { text: "Discuss",
        link: "https://sup2point0.github.io/pycobytes/discussions" },
      { text: "Submit an Idea",
        link: "https://sup2point0.github.io/pycobytes/issues" },
      { text: "Report a Bug",
        link: "https://sup2point0.github.io/pycobytes/issues" },
    },
  },
].reverse());

</script>

<nav>
  <ul>
    {#each navParts as each}
      <li id={each.text} class={each.align}>
        {#if each.link}
          <a href={each.link}>
            {#if each.pict}
              <img src={each.pict} alt={each.text}>
            {:else}
              {each.text}
            {/if}
          </a>
        {:else if each.button}
          <button on:click={each.button}> {each.text} </button>
        {:else}
          ?
        {/if}
      </li>
    {/each}
  </ul>
</nav>

<style lang="scss">

nav {
  position: fixed;
  top: 0;
  max-width: 100%;
  height: 3rem;
  z-index: 2;
  padding: 0.5rem 20vw;
  /* display: flex;
  flex-direction: row;
  align-items: center; */
  background-color: $blue-night;
  background: linear-gradient(to bottom, $blue-night, color-mix(in srgb, $blue-night 90%, transparent));
}
.left { float: left; }
.right { float: right; }

ul {
  list-style-type: none;
}

li {
  padding: 0.5rem 1rem;
  background-color: color-mix(in srgb, from $blue-night 100%, transparent);

  &:hover {
    background-color: color-mix(in srgb, from $col-accent 69%, transparent);
  }
}

img {
  height: 2rem;
}

</style>
