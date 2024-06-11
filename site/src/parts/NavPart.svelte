<script>

export let part;

</script>


<li class="nav-part">
  {#if part.link}
    <a class="nav-link" href={part.link} target={part.extern ? "_blank" : null}>
      {#if part.pict}
        <img alt={part.text} src={part.pict}>
      {:else}
        {part.text}
      {/if}
    </a>
    
  <!-- Unfortunately there's no cleaner way than just repeating this -->
  {:else}
    {#if part.pict}
      <img alt={part.text} src={part.pict}>
    {:else}
      {part.text}
    {/if}
  
  {/if}

  <!-- {#if part.dropdown}
    <ul class="nav-dropdown">
      {#each part.dropdown as part}
        <li>
          <a class="nav-link" href={part.link} target={part.extern ? "_blank" : null}>
            {part.text}
          </a>
        </li>
      {/each}
    </ul>
  {/if} -->
</li>


<style lang="scss">

li {
  margin: 0;
  padding: 0.25rem 1rem;
  display: flex;
  flex-direction: row;
  align-items: center;
  justify-content: center;
  border-radius: 0.7em;
  background-color: rgb(0 0 0 / 0%);
}

li, a {
  @include font-fun;
  text-decoration: none;
  color: light-dark(rgb(20 20 20), white);

  transition: all 0.16s ease-out;
  @media prefers-reduced-motion {
    transition: none;
  }

  &:not(:has(img)):hover {
    cursor: pointer;
    background-color: $col-hover;

    & > a {
      color: light-dark($col-accent, $col-flavour);
    }
  }
}

li img {
  height: 30px;
  max-height: $nav-height;
}

li > ul.nav-dropdow {
  display: none;
  list-style-type: none;
}

li:hover > .nav-dropdown {
  display: block;
}

</style>
