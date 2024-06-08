<script>

import { base } from "$app/paths";

import ISSUES from "#src/issues-config.js";
import duality from "#src/scripts/duality";
import { swapDuality } from "#src/scripts/duality";

const navParts = [
  {
    align: "left", text: "icon",
    pict: `${base}/pycobytes-icon.png`,
    link: `${base}`,
  },
  {
    align: "left", text: "pyco:bytes",
    link: `${base}`,
  },
// @ts-ignore
].concat([
  {
    align: "right", text: "About",
    link: `${base}/about`,
    dropdown: [
      { text: "FAQ",
        link: `${base}/faq` },
      { text: "Dev",
        link: `${base}/dev`}
    ],
  },
  {
    align: "right", text: "Issues",
    link: `${base}/issues`,
    dropdown: [
      { text: "Index",
        link: `${base}/issues` },
      { text: "Latest",
        link: `${base}/issues/${ISSUES[ISSUES.length -1]}` },
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
  // @ts-ignore
  let index = ISSUES[Math.random() * ISSUES.length | 0];
  window.location.href = "https://sup2point0.github.io/pycobytes/issues/${index}";
}

</script>

<nav>
  <ul>
    {#each navParts as part}
      <li id={part.text} class="nav-part {part.align}">
        {#if part.link}
          <a class="nav-link" href={part.link}>
            {#if part.pict}
              <img alt={part.text} src={part.pict}>
            {:else}
              {part.text}
            {/if}
          </a>
        {:else}
          {part.text}
        {/if}
      </li>
    {/each}

    <li id="swapDuality" class="nav-part left">
      <button on:click={swapDuality}>
        <span class="material-symbols-outlined">
          {#if $duality == "dark"} dark_mode
          {:else} light_mode
          {/if}
        </span>
      </button>
    </li>
  </ul>
</nav>

<style lang="scss">

nav {
  position: fixed;
  top: 0;
  z-index: 2;
  width: 100%;
  // height: $nav-height;
  max-width: 100%;
  padding: 0 4rem 0 auto;
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
  padding: 0.8rem 1rem 0.5rem;
  border-radius: 0.5em;
  background-color: rgb(0 0 0 / 0%);
}

li.nav-part, a.nav-link {
  @include font-fun;
  text-decoration: none;
  color: white;

  transition: all 0.16s ease-out;
  @media prefers-reduced-motion {
    transition: none;
  }

  &:not(:has(img)):hover {
    cursor: pointer;
    color: $col-flavour;
  }
}

li img {
  height: 2rem;
}

li button {
  background-color: rgb(0 0 0 / 0);
  border: none;
}

</style>
