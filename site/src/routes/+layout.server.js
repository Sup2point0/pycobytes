export function load({ cookies })
{
  let duality = cookies.get("duality");

  return {
    duality: duality ?? null,
  };
}
