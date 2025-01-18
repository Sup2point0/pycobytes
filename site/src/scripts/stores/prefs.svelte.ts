class UserPrefs
{
  duality: "light" | "dark" = $state("light");
}


export const prefs = new UserPrefs();
