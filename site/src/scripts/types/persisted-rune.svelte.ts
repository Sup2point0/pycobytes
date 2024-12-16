/**
 * Implementst the `PersistedState` class for creating `$state()` runes persisted to `localStorage`.
 */

import { browser } from "$app/environment";


/**
 * A $state() rune persisted to `localStorage`.
 */
export class PersistedState<T>
{
  key: string;
  value = $state<T>() as T;

  constructor(key: string, init: T)
  {
    this.key = key ?? "";
    this.value = init;

    if (browser) {
      let data = localStorage.getItem(this.key);
      if (data) {
        this.value = JSON.parse(data);
      }
    }

    $effect(() => {
      localStorage?.setItem(this.key, JSON.stringify(this.value));
    });
  }
}
