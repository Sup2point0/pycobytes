/// Handles interactions with the Napkin API

const URL = "https://sup2point0.npkn.net/pycobytes-clicky/";


export interface ClickData {
  clickCount: number | string;
  lastClick: string;
}


export default async function requestNapkin(
  method: string,
  body: object | null = null
) : Promise<ClickData>
{
  if (!body) {
    body = {};
  }

  let request = {
    method: method,
    headers: {
      "Content-Type": "text/plain",
    },
  }
  if (method !== "GET") {
    request.body = JSON.stringify(body),;
  }

  // try {
    let response = await fetch(URL, request);
    return await response.json();
  // }
  // catch (error) {
  //   return "?";
  // }
}
