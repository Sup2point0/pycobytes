export async function load({ params }) {
  let source = await import(/* @vite-ignore */ "../faq/content.md");
  console.log(source.default);
  return {text: source.default};
}