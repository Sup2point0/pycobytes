/// Theme setting

import { browser } from "$app/environment";
import { writable } from "svelte/store";


const SHARD = "pycobytes-duality"


const duality = writable<string>("light");

duality.subscribe((value) => {
  if (browser) {
    localStorage.setItem(SHARD, value);
  }
});

export default duality;


const dualities = {
  light: "dark",
  dark: "light",
}

export function swapDuality() : void {
  duality.update((value) => dualities[value]);
}


export function syncDuality() : void {
  duality.set(getLocalDuality());
}

function getLocalDuality() : string {
  if (browser) {
    let localDuality = localStorage.getItem(SHARD);
    if (localDuality == "light" || localDuality == "dark") {
      return localDuality;
    }
  }

  if (matchMedia) {
    if (matchMedia("(prefers-color-scheme: dark)").matches) {
      return "dark";
    } else {
      return "light";
    }
  }

  return "light";
}