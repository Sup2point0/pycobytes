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
  },
  preprocess: [
    sveltePreprocess({
      scss: {
        prependData: `
          @import './src/lib/styles/Nova.scss';
          @import './src/lib/styles/variables.scss';
        `,
      }
    }),
    mdsvex({
      extensions: [".md"]
    })
  ]
};

export default config;
