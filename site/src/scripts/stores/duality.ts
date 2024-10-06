import { persisted } from "svelte-persisted-store";

import { browser } from "$app/environment";


type Duality = "light" | "dark" | null;
export const duality = persisted<Duality>("pycobytes.duality", getLocalDuality());


function getLocalDuality(): string
{
  if (matchMedia) {
    if (matchMedia("(prefers-color-scheme: dark)").matches) {
      return "dark";
    } else {
      return "light";
    }
  }

  return "light";
}

// Switch the duality. If none has been set, do nothing.
function swapDuality()
{
  duality.update(d => d ? (d == "light" ? "dark" : "light") : null)
}
