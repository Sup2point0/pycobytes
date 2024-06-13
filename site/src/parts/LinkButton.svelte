<script lang="ts">

export let link: string;

</script>


<a class="link-button no-anim" href={link}>
  <div class="content">
    <slot> ... </slot>
  </div>
  <div class="content-hover">
    <slot name="hover"> ... </slot>
  </div>
</a>


<style lang="scss">

.link-button {
  min-width: 13em;
  max-width: 40vw;
  min-height: 1.6em;
  max-height: 50vh;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;

  .content {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: center;
  }
  .content-hover { display: none; }

  &:hover {
    min-width: 15em;

    .content { display: none; }
    .content-hover {
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
    }
  }
}

a {
  @include font-flavour;
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
