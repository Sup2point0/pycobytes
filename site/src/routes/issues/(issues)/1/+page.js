export async function load() {
  let data = await import("./~content.svx");
  return data.metadata;
}
