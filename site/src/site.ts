import type { IssueData } from "#scripts/types";


const data = await import("./data/site.json");
const pages = Object.values(data.default.pages);


interface SiteData {
  root: string;
  desc: {
    short: string;
    long: string;
  };
  issues: IssueData[];
}

const Site: SiteData = {
  root: "https://sup2point0.github.io/pycobytes",

  desc: {
    short: "exploring the magic of Python",
    long: "exploring the magic of Python, week by week",
  },

  issues: (pages
    .filter(page => page.index.length)
    .sort((prot, deut) => new Date(deut.date) - new Date(prot.date))
  ),
}
export default Site;
