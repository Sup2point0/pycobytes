<script>

import { base } from "$app/paths";

import { ISSUES } from "$src/issues.config.js";

const navParts = [
  {
    align: "left", text: "icon",
    pict: `${base}/pycobytes-icon.png`,
    link: ".",
  },
  {
    align: "left", text: "pyco:bytes",
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
  {
    align: "right", text: "GitHub",
    pict: `${base}/github-icon.svg`
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
      <li id={part.text} class="nav-part {part.align}">
        {#if part.link}
          <a href={part.link}>
            {#if part.pict}
              <img alt={part.text} src={part.pict}>
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
  padding: 1rem 4rem 1rem auto;
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

li.nav-part {
  @include font-flavour;
  padding: 0.8rem 1rem 0.5rem;
  border-radius: 0.5em;
  color: white;
  background-color: rgb(0 0 0 / 0%);

  transition: all 0.2s ease-in-out;
  @media prefers-reduced-motion {
    transition: none;
  }

  &:not(:has(img)):hover {
    color: $col-flavour;
  }
}

li.nav-part {
  color: white;
}

li img {
  height: 2rem;
}

</style>
