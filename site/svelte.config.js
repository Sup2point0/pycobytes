import adapter from "@sveltejs/adapter-static";
import sveltePreprocess from "svelte-preprocess";
import { mdsvex } from 'mdsvex';

/** @type {import('@sveltejs/kit').Config} */
const config = {
  kit: {
    adapter: adapter({
      pages: 'build',
      assets: 'build',
      fallback: "404.html",
      precompress: false,
      strict: true,
    }),
    paths: {
      base: process.argv.includes("dev") ? "" : process.env.BASE_PATH
    },
    alias: {
      $src: "./src/",
    },
    // prerender: {
    //   entries: [
    //     // "*", "/",
    //     // "/issue/1",
    //   ]
    // },
  },

  extensions: [".svelte", ".md", ".svx"],

  preprocess: [
    mdsvex({
      extensions: [".md", ".svx"]
    }),
    sveltePreprocess({
      scss: {
        prependData: `
          @use './src/styles/_nova' as *;
          @use './src/styles/_variables' as *;
          @use './src/mixins/_fonts' as *;
        `,
      }
    }),
  ],
};

export default config;
