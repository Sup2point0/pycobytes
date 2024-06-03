<script>

import { base } from "$app/paths";

import { ISSUES } from "$src/issues.config.js";

const navParts = [
  {
    align: "left", text: "pycobytes", pict: `${base}/pycobytes-title.png`,
    link: ".",
  },
].concat([
  {
    align: "right", text: "About",
    link: "./about",
  },
  {
    align: "right", text: "Issues",
    dropdown: [
      { text: "Index",
        link: "./issues" },
      { text: "Latest",
        link: `./issues/${ISSUES[ISSUES.length -1]}` },
      { text: "Random",
        button: pickIssue },
    ],
  },
  {
    align: "right", text: "Contact",
    dropdown: [
      { text: "Discuss",
        link: "https://sup2point0.github.io/pycobytes/discussions" },
      { text: "Submit an Idea",
        link: "https://sup2point0.github.io/pycobytes/issues" },
      { text: "Report a Bug",
        link: "https://sup2point0.github.io/pycobytes/issues" },
    ],
  },
].reverse());

function pickIssue() {
  let index = ISSUES[Math.random() * ISSUES.length | 0];
  window.location.href = "https://sup2point0.github.io/pycobytes/issues/{index}";
}

</script>

<nav>
  <ul>
    {#each navParts as part}
      <li id={part.text} class={part.align}>
        {#if part.link}
          <a href={part.link}>
            {#if part.pict}
              <img src={part.pict} alt={part.text}>
            {:else}
              {part.text}
            {/if}
          </a>
        {:else if part.button}
          <button on:click={part.button}> {part.text} </button>
        {:else}
          {part.text}
        {/if}
      </li>
    {/each}
  </ul>
</nav>

<style lang="scss">

nav {
  position: fixed;
  top: 0;
  z-index: 2;
  width: 100%;
  max-width: 100%;
  height: 4rem;
  padding-right: 4rem;
  background-color: $blue-night;
  background: linear-gradient(to bottom, $blue-night, color-mix(in srgb, $blue-night 90%, transparent));
}

nav ul {
  padding-right: 2rem;
}

.left { float: left; }
.right { float: right; }

ul {
  list-style-type: none;
}

li {
  padding: 0 1rem;
  color: white;
  background-color: color-mix(in srgb, from $blue-night 100%, transparent);

  &:hover {
    background-color: color-mix(in srgb, from $col-accent 69%, transparent);
  }
}

li img {
  height: 2rem;
}

</style>
