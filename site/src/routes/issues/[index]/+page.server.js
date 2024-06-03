import { ISSUES } from "$src/issues.config.js";

// export const prerender = true;

/** @type {import('./$types').EntryGenerator} */
export function entries() {
  return ISSUES.map(
    issue => ({ index: toString(issue) })
  );
}
