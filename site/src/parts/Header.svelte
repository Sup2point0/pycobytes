<script lang="ts">

export let type: "issue" | null = null;
export let issueIndex = null;
export let title;
export let date = null;

</script>


<div class="header">
  {#if type == "issue"}
    <code> {issueIndex} </code>
    <h1> {title} </h1>
    <p> {date} </p>
  {:else}
    <h1> {title} </h1>
  {/if}
</div>


<style lang="scss">

.header {
  margin-top: 0rem;
  margin-bottom: 2rem;
  padding: ($nav-height + 3rem) 0 2.5rem;
  text-align: center;
  background-color: $blue-cresc;
  background: linear-gradient(to right, $lilac-cresc, $blue-cresc);
}

h1 {
  @include font-head;
  padding: 1rem 0 1.5rem;
  margin: 0;
  font-size: 300%;
  color: $col-accent;
}

p {
  @include font-flavour;
  margin: 0;
  font-size: 120%;
  color: $grey-nova;
}

</style>
