import adapter from "@sveltejs/adapter-static";
import sveltePreprocess from "svelte-preprocess";

import { mdsvex } from "mdsvex";
import { remarkAlert } from "remark-github-blockquote-alert";

import scssConfig from "../site/scss-config.js";

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
    },
    prerender: {
      entries: [
        "*",
        "/issues",
        "/issues/1",
      ],
      handleHttpError: "warn",
    },
  },

  extensions: [".svelte", ".md", ".svx"],

  preprocess: [
    mdsvex({
      extensions: [".svelte", ".md", ".svx"],
      rehypePlugins: [remarkAlert],
    }),
    sveltePreprocess({
      scss: {
        prependData: scssConfig,
      }
    }),
  ],
};

export default config;
