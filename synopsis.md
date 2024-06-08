# Synopsis

pyco:bytes was a pretty involved project, and tons of fun to work on!


<br>


## Site

The site is made using [Svelte](https://svelte.dev) and [SvelteKit](https://kit.svelte.dev). Code is mostly in JavaScript with a few standalone modules in [TypeScript](https://www.typescriptlang.ory) (I love type hinting, tho not static typing). We’re using [SCSS](https://sass-lang.com) for stylesheets, which is an incredible upgrade over plain CSS.

It’s built with Svelte’s SSG prerendering, and then deployed to [GitHub Pages](https://pages.github.com), all automated through [GitHub Actions](https://github.com/features/actions). We’ve also got a couple of Python helper scripts automating some tasks during the build process, which has proven to be indispensably convenient.


<br>


## Issues

Issues are written in Markdown, before being injected into Svelte using the [MDSveX](https://github.com/features/actions) plugin. [PrismJS](https://prismjs.com) is used for syntax highlighting code blocks.

Emails in the email newsletter are created using the [Ecosend](https://ecosend.io) email builder, which provides rich formatting capabilities. This then exports to raw HTML (with embedded CSS) which can be sent as a deliciously styled email!


<br>


## Clicky

Oh, you found the clicky, did you? That’s connected to a [Napkin](https://napkin.io) cloud function implemented in Python, which handles requests to track and save how many pips have pressed that clicky. Have I mentioned Napkin is awesome, btw?


<br>


## Assets

All assets were lovingly crafted in PowerPoint 2016 offline~
