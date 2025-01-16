<!-- @component 
 
-->

<script lang="ts">

interface Props {
  link: string;
  children?: import('svelte').Snippet;
  hover?: import('svelte').Snippet;
}

let { link, children, hover }: Props = $props();

</script>


<a class="link-button no-anim" href={link}>
  <div class="content">
    {#if children}{@render children()}{:else} ... {/if}
  </div>
  <div class="content-hover">
    {#if hover}{@render hover()}{:else} ... {/if}
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
  box-shadow: 0 2px 5px rgb(black, 25%);

  .content {
    width: 100%;
    display: flex;
    flex-direction: row;
    justify-content: space-evenly;
    align-items: center;
    text-align: center;
    vertical-align: middle;
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
  @include font-ui;
  margin: 0;
  padding: 0.5em 1em;
  font-size: 125%;
  color: white;
  text-align: center;
  text-decoration: none;
  background-color: light-dark($col-prot, $col-deut);
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
