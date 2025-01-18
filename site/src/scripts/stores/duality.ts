import { PersistedState } from "#scripts/types";


/** A light/dark colour theme preference. `null` indicates no preference, in which case the theme is automatically synced with system preferences. */
export type Duality = "light" | "dark" | null;

export let duality = new PersistedState<Duality>("pyco.duality", null)


/** Get system theme preference. */


/** If the theme is not set, set it to the system theme. */
export function setFromLocalDuality(window): Duality
{
  if (!duality) {
    duality = getLocalDuality(window);
  }
  return duality;
}

/**
 * Switch the theme. If none has been set, do nothing.
 */
export function swapDuality()
{
  duality.update(d => d ? (d == "light" ? "dark" : "light") : null)
}
