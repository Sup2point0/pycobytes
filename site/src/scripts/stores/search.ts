import { writable } from "svelte/store";

import type { IssueData } from "#scripts/issue";


const searchData = writable(new SearchData());


class SearchData {
  query: string = "";
  tags: string[] = [];
  sort: "date" | "relevance" = "date";
  sortInverse: boolean = false;

  filterFunction: (IssueData[] => IssueData[]) = issues => issues;
}
