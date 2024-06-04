export async function load({ params }) {
  if (params.index == "[object Undefined]") return {};

  const route = `../../../../../../../src/exported/${params.index}.svx`;
  const issue = await import(/* @vite-ignore */ route);

  const { title, index, date } = issue.metadata;
  const content = issue.default;

  return { content, title, index, date }
}
