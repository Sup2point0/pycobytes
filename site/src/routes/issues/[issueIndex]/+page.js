import ISSUES from "$src/issues-config.js"

export async function load({ params }) {
  if (params.issueIndex == "[object Undefined]") return {};

  let route = `../../../../../../../src/exported/${params.issueIndex}.svx`;
  let issue = await import(/* @vite-ignore */ route);

  let content = issue.default;
  let issueInfo = ISSUES.find(issue => issue.issueIndex == params.issueIndex);

  if (issueInfo == undefined) {
    throw new Error("Issue not found");
  }

  let { name, issueIndex, title, date } = issueInfo;

  return { content, name, issueIndex, title, date };
}
