import type { IssueData } from "#scripts/types";


const data = await import("./data/site.json");
const pages = Object.values(data.default.pages);


interface SiteData {
  desc: object;
  issues: IssueData[];
}

const Site: SiteData = {
  desc: {
    short: "exploring the magic of Python",
    long: "exploring the magic of Python, week by week",
  },

  issues: pages.sort((prot, deut) => {
    return new Date(deut.date) - new Date(prot.date);
  }),
}
export default Site;
