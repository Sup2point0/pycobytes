import adapter from "@sveltejs/adapter-static";
import sveltePreprocess from "svelte-preprocess";

import { mdsvex } from "mdsvex";
import { remarkAlert } from "remark-github-blockquote-alert";

import scssConfig from "./scss-config.js";


const config = {
  kit: {
    adapter: adapter({
      pages: "build",
      assets: "build",
      fallback: "error.html",
      precompress: false,
      strict: true,
    }),
    paths: {
      base: process.argv.includes("dev") ? "" : process.env.BASE_PATH
    },
    alias: {
      "#src": "./src/",
      "#parts": "./src/parts",
      "#styles": "./src/styles",
      "#scripts": "./src/scripts",
    },
    prerender: {
      handleHttpError: "warn",
      handleMissingId: "warn",
    },
  },

  preprocess: [
    mdsvex({
      extensions: [".svelte", ".md", ".svx"],
      remarkPlugins: [remarkAlert],
    }),
    sveltePreprocess({
      scss: scssConfig,
    }),
  ],

  extensions: [".svelte", ".md", ".svx"],
};

export default config;
