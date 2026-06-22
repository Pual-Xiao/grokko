#!/usr/bin/env python3
import sys, json, html
from pathlib import Path

if len(sys.argv) != 4:
    print("Usage: assemble.py <content.json> <templates.json> <output.html>", file=sys.stderr)
    sys.exit(1)

content_path, templates_path, output_path = sys.argv[1:]

C = json.loads(Path(content_path).read_text())
T = json.loads(Path(templates_path).read_text())
SHELL = Path(__file__).resolve().parent.parent.joinpath("references", "template.html").read_text()

esc = html.escape
fmt = str.format

def opts_html(options):
    return "\n".join(fmt(T["opt_btn"], val=esc(o["val"]), text=esc(o["text"])) for o in options)

def task_html(q, tkey):
    if q["type"] == "match":
        rows = "\n".join(
            fmt(T["match_row"],
                label=esc(r["label"]), correct=esc(r["correct"]),
                options="".join(fmt(T["match_opt"], val=esc(o["val"]), text=esc(o["text"])) for o in r["options"]))
            for r in q["pairs"])
        return fmt(T[tkey], id=esc(q["id"]), question=esc(q["question"]),
                   ok=esc(q["ok"]), no=esc(q["no"]), src=esc(q.get("src","")), review=esc(q.get("review","")), rows=rows)
    opts = opts_html(q["options"])
    return fmt(T[tkey], id=esc(q["id"]), question=esc(q["question"]),
               answer=esc(q["answer"]), ok=esc(q["ok"]), no=esc(q["no"]),
               src=esc(q.get("src","")), review=esc(q.get("review","")), options=opts)

def rel_tags(rels):
    return "\n    ".join(fmt(T["rel_tag"], text=esc(r)) for r in rels)

# ── 11 modules ──

sec = []
sec.append(fmt(T["module_section"], sid="s1", num="01", title="学习目标与阅读路径",
    desc="读完这篇「理解地图」后，你应该能做到：",
    body="\n\n".join(fmt(T["goal_item"], num=str(i+1), text=esc(g)) for i,g in enumerate(C.get("goals",[]))) +
         (fmt(T["tip"], text=esc(C["readingTip"])) if C.get("readingTip") else "")))

sec.append(fmt(T["module_section"], sid="s2", num="02", title="零基础背景包",
    desc="读之前先补几个基础概念。每个都标注了「为什么读本文需要它」。",
    body="\n\n".join(fmt(T["bg_supplement"], term=esc(c["term"]), explanation=esc(c["explanation"]), why=esc(c["why"])) for c in C.get("backgroundConcepts",[]))))

p = C.get("problemPositioning",{})
src = fmt(T["src_block"], text=esc(p.get("deepSource","")), en=esc(p.get("deepSourceEn","")))
sec.append(fmt(T["module_section"], sid="s3", num="03", title="原文问题定位", desc="",
    body=fmt(T["card"], title="表面在讲什么？", body=f"<p>{esc(p.get('surface',''))}</p>") + "\n\n" +
         fmt(T["card"], title="深层在回答什么问题？", body=f"<p>{esc(p.get('deep',''))}</p>\n    {src}") + "\n\n" +
         fmt(T["card"], title="作者为什么要写这篇？", body=f"<p>{esc(p.get('motivation',''))}</p>") + "\n\n" +
         fmt(T["card"], title="如果只记一个问题", body=f"<p><strong>「{esc(p.get('keyQuestion',''))}」</strong></p>")))

sm = C.get("structureMap",{})
sec.append(fmt(T["module_section"], sid="s4", num="04", title="原文结构地图",
    desc=f"结构类型：<strong>{esc(sm.get('type',''))}</strong>。{esc(sm.get('description',''))}",
    body="\n\n".join(fmt(T["struct_node"], nodeClass=esc(n.get("nodeType","")), title=esc(n["title"]), loc=esc(n["loc"]), description=esc(n["description"])) for n in sm.get("nodes",[]))))

sec.append(fmt(T["module_section"], sid="s5", num="05", title="核心判断与依据", desc="",
    body="\n\n".join(
        fmt(T["card"], title=f"判断：{esc(c['title'])}",
            body=" ".join(fmt(T["tag"], type=["fact","judgment","inference","example"][i%4], label=esc(t)) for i,t in enumerate(c.get("tags",[]))) +
                 f"<p style=\"margin-top:8px\">{esc(c['explanation'])}</p>\n    " +
                 fmt(T["src_block"], text=esc(c.get("sourceText","")), en=esc(c.get("sourceEn",""))) +
                 (f"<p style=\"font-size:0.82rem;color:var(--brick);margin-top:6px\">可能误读：{esc(c['possibleMisreading'])}</p>" if c.get("possibleMisreading") else ""))
        for c in C.get("coreClaims",[]))))

sec.append(fmt(T["module_section"], sid="s6", num="06", title="关键概念拆解", desc="",
    body="\n\n".join(
        fmt(T["concept_card"], term=esc(c["term"]), definition=esc(c["definition"]),
            antiMisunderstanding=esc(c.get("antiMisunderstanding","")),
            relations=rel_tags(c.get("relations",[])))
        for c in C.get("keyConcepts",[]))))

sq = C.get("socraticQuestions",[])
sec.append(fmt(T["module_section"], sid="s7", num="07", title="苏格拉底式阅读关卡",
    desc="按难度递进。每题都带原文依据和反馈。",
    body="\n\n".join(task_html(q, "task_single" if q["type"]=="single" else "task_multi") for q in sq)))

gt = C.get("gamifiedTasks",[])
sec.append(fmt(T["module_section"], sid="s8", num="08", title="闯关式任务",
    desc="覆盖标注、匹配、纠错、补全、迁移。",
    body="\n\n".join(task_html(q, {"single":"task_single","multi":"task_multi","match":"task_match"}[q["type"]]) for q in gt) +
         "\n\n" + T["wrong_box"]))

sec.append(fmt(T["module_section"], sid="s9", num="09", title="误解与边界", desc="",
    body="\n\n".join(fmt(T["misunderstand"], title=esc(m["title"]), whyEasy=esc(m["whyEasy"]), actual=esc(m["actual"]), notSaying=esc(m["notSaying"]), prevention=esc(m["prevention"])) for m in C.get("misunderstandings",[]))))

sec.append(fmt(T["module_section"], sid="s10", num="10", title="背景知识缺口",
    desc="要完全理解还需要补这些。但先读也没关系——碰到不懂的再回来。",
    body="\n\n".join(fmt(T["gap_card"], title=esc(g["title"]), description=esc(g["description"]), necessity=esc(g.get("necessity",""))) for g in C.get("knowledgeGaps",[])) +
         "\n\n" + fmt(T["gap_card"], title="推荐下一步追问",
             description="<br>".join(f"（{i+1}）{esc(q)}" for i,q in enumerate(C.get("nextQuestions",[]))),
             necessity="")))

sec.append(fmt(T["module_section"], sid="s11", num="11", title="复盘与学习报告",
    desc="做完所有题目后，点击生成报告查看学习记录。",
    body=T["report_section"] +
         (fmt(T["card"], title="读原论文前的最后提醒", body=f"<p>{esc(C['finalReminder'])}</p>") if C.get("finalReminder") else "")))

# ── Assemble ──
title = esc(C.get("title","Untitled"))
task_count = len(sq) + len(gt)
html = (SHELL
    .replace("TITLE_PLACEHOLDER", title)
    .replace("<!-- CONTENT_PLACEHOLDER -->", "\n\n".join(sec))
    .replace('<div class="progress-num" id="barNum">0 / 0</div>',
             f'<div class="progress-num" id="barNum">0 / {task_count}</div>'))

Path(output_path).write_text(html)
print(f"Done: {output_path}  (modules: 11, tasks: {task_count})")
