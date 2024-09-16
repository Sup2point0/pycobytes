import { persisted } from "svelte-persisted-store";


type Duality = "light" | "dark" | null;
export const duality = persisted<Duality>("pycobytes.duality", null);
