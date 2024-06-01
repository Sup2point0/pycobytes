<script>

export let title;
export let date;

</script>


<div class="header">
  <h1> {title} </h1>
  <p> {date} </p>
</div>


<style lang="scss">

h1 {
  @include font-head;
  color: $col-flavour;
}

p {
  @include font-flavour;
  color: $grey-nova;
}

</style>
