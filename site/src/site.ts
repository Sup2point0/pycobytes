const data = await import("./data/site.json");


const Site = {
  desc: {
    short: "exploring the magic of Python",
    long: "exploring the magic of Python, week by week",
  },

  issues: data.default.pages,
}
export default Site;
