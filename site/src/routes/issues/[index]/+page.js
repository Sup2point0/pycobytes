export async function load({ params }) {
  if (params.index == "[object Undefined]") return {};

  let route = `../../../../../../../src/exported/${params.index}.svx`;
  let issue = await import(/* @vite-ignore */ route);

  let content = issue.default;
  let { title, index, date } = issue.metadata;
  if (!date) {
    date = "Unreleased!";
  }

  return { content, title, index, date }
}
