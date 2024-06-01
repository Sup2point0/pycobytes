export async function load({ params }) {
  // if (!params || !params.issueIndex || params.issueIndex) return;

  return params.issueIndex;

  // const route = `../../../../../../../src/lib/export/${params.issueIndex}.md`;
  // const issue = await import(route);
  // const { title, index, date } = issue.metadata;
  // const content = issue.default;

  // return { content, title, index, date }
}
