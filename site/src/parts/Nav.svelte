<script>

import { base } from "$app/paths";
import NavPart from "#src/parts/NavPart.svelte";

import ISSUES from "#src/issues-config";
import duality from "#src/scripts/duality";
import { swapDuality } from "#src/scripts/duality";

const navLeft = [
  {
    text: "icon",
    pict: `${base}/pycobytes-icon.png`,
    link: `${base}`,
  },
  {
    text: "pyco:bytes",
    link: `${base}`,
  },
]

const navRight = [
  {
    text: "About",
    link: `${base}/faq`,
    dropdown: [
      { text: "FAQ",
        link: `${base}/faq` },
      { text: "Dev",
        link: `${base}/dev`},
    ],
  },
  {
    text: "Issues",
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
    text: "Contact",
    extern: true,
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
    text: "GitHub",
    pict: `${base}/github-icon.svg`,
    link: "https://github.com/Sup2point0/pycobytes",
    extern: true,
  },
];

function pickIssue() {
  // @ts-ignore
  let index = ISSUES[Math.random() * ISSUES.length | 0];
  window.location.href = "https://sup2point0.github.io/pycobytes/issues/${index}";
}

</script>

<nav>
  <ul class="left">
    {#each navLeft as part}
      <NavPart {part} />
    {/each}

    <li>
      <button on:click={swapDuality}>
          <span class="material-symbols-outlined">
          {#if $duality == "dark"}
            dark_mode
          {:else}
            light_mode
          {/if}
        </span>
      </button>
    </li>
  </ul>

  <ul class="right">
    {#each navRight as part}
      <NavPart {part} />
    {/each}
  </ul>
</nav>

<style lang="scss">

nav {
  position: fixed;
  top: 0;
  z-index: 2;
  width: 100%;
  height: $nav-height;
  max-width: 100%;
  padding: 0.1rem 4rem 0.1rem auto;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
  background-color: $col-idle;
  background: linear-gradient(to bottom, $col-idle, color-mix(in srgb, $col-idle 90%, transparent));
  border-bottom: 2px solid $col-flavour;
  @include fade-duality;
}

nav ul {
  max-height: $nav-height;
  display: flex;
  flex-direction: row;
  padding-right: 2rem;
}

ul {
  margin: 0;
  list-style-type: none;
}

li:has(button) {
  width: 30px;
  margin: 0;
  padding: 0.25rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  border-radius: 100%;
  background-color: $col-idle;

  transition: all 0.16s ease-out;
  @media prefers-reduced-motion {
    transition: none;
  }

  & button {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    background: none;
    color: light-dark($lilac-nova, $mellow-cresc);
    border: none;
  }

  &:hover {
    background-color: $col-hover;
    & > button {
      color: light-dark($mellow-cresc, $lilac-nova);
    }
  }
}

</style>
