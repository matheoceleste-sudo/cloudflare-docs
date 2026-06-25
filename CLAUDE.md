# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

> **Canonical AI agent reference:** `AGENTS.md` contains the full, authoritative guide for this repo — content conventions, component APIs, common mistakes, CI rules, and more. Read it before making changes. This file summarises the key points and adds Claude Code–specific guidance.

## What this repo is

Source for [developers.cloudflare.com](https://developers.cloudflare.com). It is an **Astro + Starlight** documentation site, authored in **MDX**, deployed as a Cloudflare Worker.

- **Primary branch**: `production` (not `main`)
- **Package manager**: pnpm — use `pnpm install --frozen-lockfile`
- **Node.js**: 24.x

## Commands

```bash
# Install
pnpm install --frozen-lockfile

# Development
pnpm run dev              # Local dev server (runs fetch-skills prebuild first)
pnpm run sync             # Regenerate Astro content collection types

# Validation (use these; do NOT run a full build in CI — it times out)
pnpm run check            # Astro + Worker type-check (validates frontmatter schemas)
pnpm run lint             # ESLint
pnpm run format:core:check  # Prettier check

# Full local validation (not for CI)
pnpm run build            # Full build + MDX parsing + internal link validation
pnpm run test             # All Vitest suites
pnpm exec tsm bin/validate-redirects.ts  # Only needed when public/__redirects changes

# Auto-fix formatting
pnpm run format           # Fix .js/.ts/.css files
pnpm run format:content   # Fix .md/.mdx/.astro files
pnpm run format:data      # Fix .json/.yaml/.yml files

# Run a specific test suite
vitest --project Node      # Node suite only (*.node.test.ts)
vitest --project Workers   # Workers suite only (*.worker.test.ts)
vitest --project Astro     # Astro suite only (*.astro.test.ts)

# Directory entry IDs (src/content/directory/ files)
node tools/directory-entry-ids        # Validate
node tools/directory-entry-ids --fix  # Auto-generate missing IDs
```

## Architecture overview

```
src/
  content/docs/         # 5 400+ MDX pages — one directory per product
  content/partials/     # 1 200+ reusable MDX snippets (used via <Render>)
  content/changelog/    # Product changelogs
  content/glossary/     # Glossary terms (YAML)
  content/products/     # Product metadata (YAML, 135 files)
  content/directory/    # Product/feature directory entries (YAML, need generated IDs)
  components/           # Custom Astro + React components
    index.ts            # Barrel export — all MDX component imports come from here
    overrides/          # Starlight component overrides (Banner, Footer, Head…)
  schemas/              # Zod schemas for all content collections (incl. tags allowlist)
  plugins/              # Remark, Rehype, Starlight, Expressive Code plugins
  pages/                # Dynamic routes (changelog, glossary, search)
  util/                 # Shared utilities
worker/                 # Cloudflare Worker that serves the built site
public/__redirects      # Redirect rules (source URLs must end in `/`, `*`, `.xml`, etc.)
bin/fetch-skills.ts     # Downloads Agent Skills (auto-runs on predev/prebuild)
skills/                 # Generated — do not commit, in .gitignore
```

### Content collections

Defined in `src/content.config.ts` with Zod schemas in `src/schemas/`. The 20 collections include `docs`, `partials`, `changelog`, `glossary`, `products`, `plans`, `workers-ai-models`, `directory`, `fields`, and `learning-paths`.

### Testing

Three Vitest projects defined in `vitest.config.ts`:

| Suite | File pattern | Runtime |
|---|---|---|
| Workers | `*.worker.test.ts` | `@cloudflare/vitest-pool-workers` |
| Node | `*.node.test.ts` | Node (happy-dom) |
| Astro | `*.astro.test.ts` | Astro Vite config |

## The most important MDX rules

**Unescaped `{`, `}`, `<`, `>` in prose is the #1 cause of build failures.** MDX parses these as JSX. Wrap in backticks or use `\{` `\}` / `&lt;` `&gt;`.

Other build-breakers:
- Components must be imported from `~/components` inside the file (after frontmatter).
- Code block language names must be **lowercase** (`json` not `JSON`).
- Internal links use absolute paths without file extensions: `/workers/get-started/` — never `./page` or full `https://developers.cloudflare.com/...` URLs.
- Images go in `src/assets/images/`, never `src/content/`.
- Tags must be in the allowlist at `src/schemas/tags.ts`.
- `src/content/directory/` YAML files need a generated 6-char `id` on line 1 — always use `node tools/directory-entry-ids --fix`, never hand-write IDs.

## Key component APIs

All MDX components are imported from `~/components`.

```mdx
import { Render, TypeScriptExample, WranglerConfig, Details, Tabs, TabItem } from "~/components";
```

| Component | What it does |
|---|---|
| `<Render file="name" product="workers" />` | Inserts a partial from `src/content/partials/{product}/{file}.mdx` |
| `<TypeScriptExample filename="…">` | Shows TS + auto-transpiled JS in synced tabs |
| `<WranglerConfig>` | Shows TOML + JSONC config in synced tabs; use `$today` for `compatibility_date` |
| `<Details header="…">` | Collapsible section |
| `<PackageManagers type="exec" pkg="…">` | npm / yarn / pnpm command tabs |
| `<Plan type="enterprise" />` | Plan availability badge |
| `<InlineBadge preset="beta" />` | Status badge |
| `<GlossaryTooltip term="…">` | Inline hover tooltip |

## Style guide essentials

- Active voice, present tense, no contractions.
- **"select"** not "click"; **"go to"** not "navigate"; **"turn on/off"** not "enable/disable".
- **Bold** for UI elements; monospace for code, paths, HTTP verbs, status codes.
- No `$` prefix on terminal commands (the copy button copies the whole block).
- Headings must be sequential (H2 → H3 → H4, never skip levels).
- Placeholder values: `example.com`, `192.0.2.0/24`, `<YOUR_DOMAIN>`.

## Commit format

```
[Product] Short description
# or
type: short description
```

Examples: `[Workers] Fix broken link in get-started`, `docs: clarify rate limiting behaviour`, `fix: correct TypeScript example`.
