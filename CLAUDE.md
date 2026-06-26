# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Stack

- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript (strict mode — `allowJs: false`, `noUnusedLocals`, `noUnusedParameters`)
- **Styling**: Tailwind CSS v3 + CSS variables (HSL tokens for dark mode)
- **UI components**: shadcn/ui (Radix UI primitives + `class-variance-authority`)
- **Icons**: lucide-react
- **Package manager**: pnpm

## Commands

```bash
pnpm dev          # Dev server on http://localhost:3000
pnpm build        # Production build
pnpm lint         # ESLint (next lint)
pnpm type-check   # tsc --noEmit
```

## Architecture

```
app/              # Next.js App Router — layouts, pages, route handlers
components/
├── ui/           # shadcn/ui primitives (Button, Dialog, etc.) — do not edit generated files
└── ...           # Composed, domain-specific components
lib/
└── utils.ts      # cn() helper (clsx + tailwind-merge)
```

### App Router conventions

- Every route segment needs `page.tsx` (and optionally `layout.tsx`, `loading.tsx`, `error.tsx`).
- Server Components by default — add `"use client"` only when you need browser APIs, event handlers, or React hooks.
- Data fetching goes directly in Server Components (`async` functions, `fetch` with cache options).
- Route handlers live in `app/api/**/route.ts`.

### Component conventions

- All shadcn/ui components live in `components/ui/`. Add new ones with `pnpm dlx shadcn@latest add <component>`.
- Import `cn` from `@/lib/utils` to merge Tailwind classes conditionally.
- Use `lucide-react` for all icons — import individually (`import { Search } from "lucide-react"`).
- Prefer `asChild` pattern from Radix UI over wrapping elements unnecessarily.

## TypeScript rules

- No `any` — use `unknown` and narrow, or define a proper type.
- Always use `import type` for type-only imports (`@typescript-eslint/consistent-type-imports`).
- No non-null assertions (`!`) — use optional chaining or explicit null checks.
- Unused variables must be prefixed with `_` or removed.

## Styling conventions

- Colors are defined as CSS variables in `app/globals.css` and referenced via Tailwind tokens (`bg-background`, `text-foreground`, `border-border`, etc.).
- Dark mode uses the `.dark` class strategy (toggle via `class` on `<html>`).
- Never hard-code color values — use the semantic tokens from `tailwind.config.ts`.
- Use `cn()` instead of string concatenation for conditional classes.

## ESLint — enforced rules

| Rule | Level |
|---|---|
| `@typescript-eslint/no-explicit-any` | error |
| `@typescript-eslint/no-non-null-assertion` | error |
| `@typescript-eslint/consistent-type-imports` | error |
| `no-console` (except `warn`/`error`) | warn |
| `react/self-closing-comp` | error |
| `react/jsx-curly-brace-presence` | error |

## shadcn/ui

- `components.json` configures the CLI — style `default`, CSS variables enabled, alias `@/components/ui`.
- Do not edit files in `components/ui/` by hand unless patching a bug; re-run the CLI to update.
- Available Radix primitives already installed: `Dialog`, `DropdownMenu`, `Label`, `Separator`, `Slot`, `Toast`, `Tooltip`.
