import Site from "#src/site";

import type { IssueData } from "#scripts/types";

import { base } from "$app/paths";


// Get data for an issue by its displayed index.
export function getIssue(
  index: number | string
): IssueData | undefined
{
  return Site.issues.find(issue => issue.index && issue.index[0] == index);
}

// Get link for a random issue.
export function pickRandomIssue(): string {
  console.log("picking issue");
  let index = Math.floor(Math.random() * Site.issues.length);
  console.log(index);
  return `${base}/issues/${index}`;
}
