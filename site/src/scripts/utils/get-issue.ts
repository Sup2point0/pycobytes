import Site from "#src/site";


export function getIssue(index: number | string) {
  let idx = `issues/${index}.md`;
  return Site.issues[idx];
}
