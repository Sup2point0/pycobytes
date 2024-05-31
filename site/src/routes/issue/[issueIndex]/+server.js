import ISSUES from "$lib/issues.config.js";

export function entries() {
  return ISSUES.map(
    issue => { issueIndex: issue.index }
  );
}
