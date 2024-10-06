import { base } from "$app/paths";

import Site from "#src/site";


// TODO add return type
export function getIssue(index: number | string) {
  let idx = `issues/${index}.md`;
  return Site.issues[idx];
}


export function pickRandomIssue(): string {
  let issues = Object.values(Site.issues);
  let index = Math.floor(Math.random() * issues.length);
  return `${base}/issues/${index}`;
}
