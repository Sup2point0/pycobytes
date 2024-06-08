import ISSUES from "#src/issues-config.js";

/** @type {import('./$types').EntryGenerator} */
export function entries() {
  return ISSUES.map(
    issue => ({ issueIndex: issue.issueIndex })
  );
}

export const prerender = true;
