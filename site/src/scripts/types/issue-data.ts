export default interface IssueData
{
  path: string;
  last_deploy: string;
  isIndex: boolean;

  dest: string;
  title?: string | null;
  capt?: string | null;
  head?: string | null;
  desc?: string | null;
  index?: string[] | null;
  shard?: string[] | null;
  date?: string | null;
  date_display?: string | null;
}
