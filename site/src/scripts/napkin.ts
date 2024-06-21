/// Handles interactions with the Napkin API

const URL = "https://sup2point0.npkn.net/pycobytes-clicky/";


export default async function requestNapkin(
  method: string,
  body: object | null = null
) : Promise<object>
{
  if (!body) {
    body = {};
  }

  let request = {
    method: method,
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(body),
  }
  if (method == "get") {
    delete request.body;
  }

  // try {
    let response = await fetch(URL, request);
    return await response.json();
  // }
  // catch (error) {
  //   return "?";
  // }
}
