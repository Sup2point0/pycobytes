<div class="content">
  <main>
    <slot>
      Um, what happened here?
    </slot>
  </main>
</div>


<style>

.content {
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  align-items: center;
}

main {
  min-width: 500px;
  max-width: min(80%, 800px);
  padding: 1em 0;
}

</style>
