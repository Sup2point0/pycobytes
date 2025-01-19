import { prefs } from "#scripts/stores";
import type { Duality } from "#scripts/types";


export function load({ cookies })
{
  let duality: Duality = cookies.get("duality") as Duality;
  duality = duality || "light";

  prefs.duality = duality;
  return { duality };
}
