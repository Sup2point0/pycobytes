import Site from "#src/site";

import type { IssueData } from "#scripts/types";

import { base } from "$app/paths";


// Get data for an issue by its displayed index.
export function getIssue(
  index: string
): IssueData | undefined
{
  return Site.issues.find(issue => issue.dest == index);
}

// Get link for a random issue.
export function pickRandomIssue(): string {
  let index = Math.floor(Math.random() * Site.issues.length);
  return `${base}/issues/${index}`;
}
