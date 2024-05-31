export async function load({ params }) {
  if (params == null) return;
  const route = `../../../export/${params.issueIndex}.md`;
  const issue = await import(route);
  const { title, index, date } = issue.metadata;
  const content = issue.default;

  return { content, title, index, date }
}
