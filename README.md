# Grokko

> Turn dense, hard-to-read material into a **source-grounded, interactive HTML "understanding map."**
> 把难啃的干货，拆成一张有原文依据、能追问、能复述的交互式理解地图。

Grokko is an agent skill that takes a hard article / interview / paper / long technical write-up and produces a single self-contained `.html` page that helps a beginner actually *understand* it — not just skim a summary. Every key claim is tied back to the source text, ambiguous spots become Socratic questions, and the page ships with working closed-form quizzes, a progress bar, a wrong-answer review, and a copyable study report.

**Output language defaults to Chinese**, regardless of the source language. Source quotes can remain in the original language with Chinese explanation. If the user explicitly asks for English or another language, use that language instead.

---

## What makes it different

- **Fidelity first.** Priority order is *fidelity > clear structure > friendliness > gamification*. Every core claim carries its `原文依据 / source quote`; the model's own inferences are labeled separately so you never mistake a paraphrase for the author's words.
- **Fact / judgment / inference / example tagging.** Trains the reader to tell what the author *stated* from what was *inferred*.
- **No forced causal chains.** It detects the source's actual structure (argument map, theme clusters, timeline, mechanism flow…) instead of flattening everything into one storyline.
- **Cross-language term handling.** A built-in rule decides when a technical term should be translated, kept in the original, or kept-with-a-gloss — so you never get nonsense literal translations.
- **Cross-model stable interactions.** Quizzes use one fixed, paste-verbatim, event-delegation engine. The model only fills `data-*` attributes; the logic is identical across Opus, Codex, etc., which removes the common "click does nothing" bug.
- **Locked layout.** Left fixed sidebar (title + progress + nav) and a strictly single-column main area — no surprise multi-column grids.

---

## The 11 modules every page contains

1. Goals & reading path
2. Zero-background pack (3–5 must-know concepts)
3. What the source is really asking
4. Source structure map
5. Core claims + evidence
6. Key concepts
7. Socratic reading levels
8. Quest-style tasks (annotate / match / correct / transfer)
9. Misconceptions & boundaries
10. Background gaps
11. Recap & study report

---

## Install / Use

Grokko is a skill for agent environments that have file tools (e.g. Claude Code / Cowork-style setups).

1. Copy the `grokko/` folder (containing `SKILL.md`) into your skills directory.
2. Invoke it by giving the agent a piece of source text (paste, file path, or URL) and asking it to "build an understanding map" / "用 Grokko 拆解这篇".
3. The agent outputs a self-contained `.html` you can double-click open. No backend, no build step.

**Prerequisites**

- An agent host with read/write file tools.
- `node` available if you want the self-check step (`node --check` on the embedded script).

---

## Customization

- **Footer signature.** By default the page shows only a small project credit (`由 Grokko 生成 · github.com/<your-username>/grokko`) and no personal name. To add your own name/link, tell the agent — it will append an optional personal signature line. Nothing personal is injected by default.
- **Language.** Defaults to Chinese; override by asking for a specific language.

---

## Known limitations

- Best for material that has a real argument or structure. Not meant for breaking-news blurbs, API parameter references, or pure step-by-step how-tos.
- It is a **preview / comprehension aid**, not a replacement for fully studying the source.
- Generated pages may quote source text; if you publish example outputs, mind the copyright of the original material.

---

## License

MIT — see [LICENSE](./LICENSE). Use it, fork it, ship it.
