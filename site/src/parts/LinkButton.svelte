<script lang="ts">

export let link: string;

</script>


<a class="link-button" href={link}>
  <slot>
    <p> RENDER ERROR </p>
  </slot>
</a>


<style lang="scss">

button {
  @include font-flavour;
  min-width: 8em;
  max-width: 50vw;
  margin: 0;
  padding: 0.2em 0.5em;
  color: white;
  background-color: light-dark($col-accent, $col-flavour);
  border-radius: 0.5rem;
  outline: none;

  transition: color 0.12s ease-out;

  &:hover {
    background-color: $pink-elec;
  }

  &:active {
    background-color: $purp-nova;
  }
}

</style>
