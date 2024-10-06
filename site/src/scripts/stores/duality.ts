import { persisted } from "svelte-persisted-store";


type Duality = "light" | "dark" | null;
export const duality = persisted<Duality>("pycobytes.duality", null);


// Get system theme preference.
export function getLocalDuality(window): string
{
  if (window.matchMedia) {
    if (window.matchMedia("(prefers-color-scheme: dark)").matches) {
      return "dark";
    } else {
      return "light";
    }
  }

  return "light";
}

// Switch the theme. If none has been set, do nothing.
export function swapDuality()
{
  duality.update(d => d ? (d == "light" ? "dark" : "light") : null)
}
