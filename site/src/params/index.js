/** @type {import('@sveltejs/kit').ParamMatcher} */
export function match(param) {
  return /[0-9]{1,2}/.test(param)
}
