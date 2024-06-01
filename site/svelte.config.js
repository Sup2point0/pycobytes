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
    // alias: {
    //   $src: "./src/"
    // },
    prerender: {
      entries: ["*", "/",
        "/issue/1",
      ]
    },
  },

  extensions: [".svelte", ".md"],

  preprocess: [
    sveltePreprocess({
      scss: {
        prependData: `
          @import './src/lib/styles/nova.scss';
          @import './src/lib/variables.scss';
          @import './src/lib/mixins/fonts.scss';
        `,
      }
    }),
    mdsvex({
      extensions: [".md"]
    })
  ]
};

export default config;
