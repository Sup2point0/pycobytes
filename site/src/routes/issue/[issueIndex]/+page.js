export async function load({ params }) {
  const issue = await import(`/${params.issueIndex}.md`);
  const { title, index, date } = issue.metadata;
  const content = issue.default;

  return { content, title, index, date }
}
