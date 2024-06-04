export async function load({ params }) {
  if (params.issueIndex == "[object Undefined]") return {};

  let route = `../../../../../../../src/exported/${params.issueIndex}.svx`;
  let issue = await import(/* @vite-ignore */ route);

  let content = issue.default;
  let { title, issueIndex, date } = issue.metadata;
  if (!date) {
    date = "Unreleased!";
  }

  return { content, title, issueIndex, date }
}
