const Site = {
  desc: {
    short: "exploring the magic of Python",
    long: "exploring the magic of Python, week by week",
  }
}
export default Site;

const issues = await import("data/site-data.json");
export const Issues = issues.default;
