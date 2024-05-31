import { ISSUES } from "$lib/issues.config.js";

export const prerender = true;

/** @type {import('./$types').EntryGenerator} */
export function entries() {
  return ISSUES.map(
    issue => ({ issueIndex: toString(issue) })
  );
}
