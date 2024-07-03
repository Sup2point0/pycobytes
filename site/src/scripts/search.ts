import { writable } from "svelte/store";


const searchData = writable(new SearchData());


class SearchData {
  query: string = "";
  tags: string[] = [];
  sort: "date" | "relevance" = "date";
  sortInverse: boolean = false;
}
