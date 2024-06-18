import ISSUES from "#src/issues-config.js";


export function entries() {
  return ISSUES.map(
    issue => ({ issueIndex: issue.issueIndex })
  );
}

export const prerender = false;  // FIXME
