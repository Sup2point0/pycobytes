import Site from "#src/site";

import type { IssueData } from "#scripts/types";

import { base } from "$app/paths";


// Get data for an issue by its displayed index.
export function getIssue(index: number | string): IssueData {
  let idx = `issues/${index}.md`;
  return Site.issues[idx];
}

// Get link for a random issue.
export function pickRandomIssue(): string {
  let issues = Object.values(Site.issues);
  let index = Math.floor(Math.random() * issues.length);
  return `${base}/issues/${index}`;
}
