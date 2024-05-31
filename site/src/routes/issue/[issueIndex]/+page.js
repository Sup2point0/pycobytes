export async function load({ params }) {
  if (params == null) return;
  const issue = await import(`./src/export/${params.issueIndex}.md`);
  const { title, index, date } = issue.metadata;
  const content = issue.default;

  return { content, title, index, date }
}
