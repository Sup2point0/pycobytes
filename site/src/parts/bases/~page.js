export async function load() {
  let data = await import("./%{file}.svx");
  return data.metadata;
}
