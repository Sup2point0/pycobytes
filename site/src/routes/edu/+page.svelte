<script>

  import Header from "#src/parts/Header.svelte";
  import Main from "#src/parts/Main.svelte";
  import Content from "../edu/_Content.svx";
  
  </script>
  
  
  <svelte:head>
    <title> decoded · pycobytes </title>
  </svelte:head>
  
  <article>
    <Header
      title = "decoded - <em>pyco:bytes</em>"
      caption = "Difficulties and learnings"
    />
  
    <Main>
        <Content />
    </Main>
  </article>
  