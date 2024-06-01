<script>

// import { issues } from "fetch-issues.js";

const navParts = [
  {
    align: "left", text: "pycobytes", pict: "/pycobytes-title.png",
    link: "https://sup2point0.github.io/pycobytes",
  },
  {
    align: "right", text: "Issues",
    link: "https://sup2point0.github.io/pycobytes/issues",
  },
  {
    align: "right", text: "About",
    link: "https://sup2point0.github.io/pycobytes/about",
  }
];

</script>

<nav>
  <ul>
    {#each navParts as each}
      <li id={each.text} class={each.align}>
        <a href={each.link}>
          {#if each.pict}
            <img src={each.pict} alt={each.text}>
          {:else}
            {each.text}
          {/if}
        </a>
      </li>
    {/each}
  </ul>
</nav>

<style lang="scss">

nav {
  position: fixed;
  top: 0;
  width: 100%;
  height: 4rem;
  z-index: 2;
  padding: 1rem;
  background-color: $blue-night;
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
  height: 4rem;
}

</style>
