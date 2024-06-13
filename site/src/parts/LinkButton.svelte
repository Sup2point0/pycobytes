<script lang="ts">

export let link: string;

</script>


<div class="link-button">
  <a class="link-button no-anim" href={link}>
    <slot>
      <p> RENDER ERROR </p>
    </slot>
  </a>
</div>


<style lang="scss">

a {
  @include font-flavour;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  min-width: 8em;
  max-width: 50vw;
  margin: 0;
  padding: 0.5em 1em;
  font-size: 125%;
  color: white;
  text-align: center;
  text-decoration: none;
  background-color: light-dark($col-accent, $col-flavour);
  border-radius: 0.8em;
  outline: none;

  transition: all 0.16s cubic-bezier(0.33, 1, 0.68, 1);  // ease-out cubic

  &:hover {
    justify-content: space-evenly;
    background-color: light-dark($purp-nova, $pink-elec);
    border-radius: 0.6em;
  }

  &:active {
    background-color: light-dark($pink-elec, $purp-nova);
  }
}

</style>
