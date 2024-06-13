<script lang="ts">

export let link: string;

</script>


<a class="link-button no-anim" href={link}>
  <slot>
    <p> RENDER ERROR </p>
  </slot>
</a>


<style lang="scss">

a {
  @include font-flavour;
  font-size: 125%;
  min-width: 8em;
  max-width: 50vw;
  margin: 0;
  padding: 0.5em 1em;
  color: white;
  text-align: center;
  text-decoration: none;
  background-color: light-dark($col-accent, $col-flavour);
  border-radius: 0.5em;
  outline: none;

  transition: background-color 0.16s ease-out;

  &:hover {
    background-color: light-dark($purp-nova, $pink-elec);
  }

  &:active {
    background-color: light-dark($pink-elec, $purp-nova);
  }
}

</style>
