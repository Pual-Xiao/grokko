---
name: grokko
description: 把复杂文稿拆成 source-grounded 交互式 HTML 理解地图。保真拆解、原文依据、苏格拉底式追问。默认中文输出。
---

# Grokko

> 保真 > 结构清楚 > 理解友好 > 趣味包装

## 工作流

1. 读源文 → 提取结构
2. 按下方 schema 输出 `content.json`
3. `python3 scripts/assemble.py content.json references/templates.json output.html`
4. 验证：`sed -n '/<script>/,/<\/script>/p' output.html | sed '1d;$d' | node --check`

你只输出 content.json。HTML 全部由 assemble.py 生成。

## content.json schema

```json
{
  "title": "原文标题",
  "goals": ["能说出……", "能区分……"],
  "readingTip": "<strong>阅读建议</strong>：……",
  "backgroundConcepts": [
    {"term": "术语", "explanation": "≤120字解释", "why": "为什么读本文需要"}
  ],
  "problemPositioning": {
    "surface": "表面在讲什么",
    "deep": "深层问题",
    "deepSource": "原文引用",
    "deepSourceEn": "— §I, p.1",
    "motivation": "作者为什么写",
    "keyQuestion": "如果只记一个问题"
  },
  "structureMap": {
    "type": "机制型",
    "description": "一句话",
    "nodes": [
      {"title": "§II · 数学背景", "loc": "pp.3–9", "description": "内容+阅读建议", "nodeType": "math"}
    ]
  },
  "coreClaims": [
    {
      "title": "判断标题",
      "tags": ["事实", "判断"],
      "explanation": "正文解释",
      "sourceText": "原文直接引语或总结自§X.X",
      "sourceEn": "— §III, p.9",
      "possibleMisreading": "可能误读提示"
    }
  ],
  "keyConcepts": [
    {
      "term": "术语",
      "definition": "先严格定义，再辅助理解",
      "antiMisunderstanding": "别误解成什么",
      "relations": ["概念A → 概念B", "C → D"]
    }
  ],
  "socraticQuestions": [
    {
      "id": "q1",
      "type": "single",
      "question": "题干",
      "options": [{"val":"A","text":"A. ……"},{"val":"B","text":"B. ……"}],
      "answer": "A",
      "ok": "答对反馈：为什么对 + 原文依据",
      "no": "答错反馈：为什么错 + 可能误解 + 回哪个模块",
      "src": "原文：……",
      "review": "回到「05·核心判断与依据」复习……"
    }
  ],
  "gamifiedTasks": [
    {
      "id": "g1",
      "type": "match",
      "question": "题干",
      "pairs": [{"label":"标签","correct":"B","options":[{"val":"A","text":"……"}]}],
      "ok": "……", "no": "……", "src": "……", "review": "……"
    }
  ],
  "misunderstandings": [
    {"title":"误解标题","whyEasy":"为什么容易","actual":"真正说了什么","notSaying":"没说什么","prevention":"如何避免"}
  ],
  "knowledgeGaps": [
    {"title":"需补知识","description":"解释","necessity":"对读懂§X的必要性：★★★"}
  ],
  "nextQuestions": ["追问1","追问2","追问3","追问4"],
  "finalReminder": "读原文前的最后提醒"
}
```

## 内容规则

### 学习目标
3–5 个，以"能+动词"开头。❌ 理解全文、掌握思想。✅ 能说出作者在回答什么问题、能指出 2 个易误解处。

### 背景概念
3–5 个。explanation ≤120 字。标注为背景补充，不写成作者观点。

### 结构地图
先诊断类型：机制流程 / 论证结构 / 主题簇 / 时间线 / 问题树 / 冲突结构。nodeType: 不填=绿 / `math`=蓝 / `spec`=红。

### 核心判断
3–7 个。sourceText 优先原文直接引语，无法直接引用时注明"总结自 §X.X"。tags 标注事实/判断/推论/例子。

### 关键概念
≤6 个。definition 先严格定义再辅助理解。只用比喻不给定义 → 读者记住的是比喻而非概念。

### 题目
苏格拉底 5–8 题，难度递进：识别→分类→前提检测→反方→复述→迁移。闯关 4–5 题，覆盖单选/多选/匹配。type: `single` / `multi` / `match`。禁止 textarea。

每题 8 字段必填：id, type, question, options(或pairs), answer, ok, no, src, review。

review 编号用下表两位数（01–11）：

| 01 | 02 | 03 | 04 | 05 | 06 | 07 | 08 | 09 | 10 | 11 |
| 学习目标 | 背景包 | 问题定位 | 结构地图 | 核心判断 | 概念拆解 | 苏格拉底 | 闯关任务 | 误解边界 | 知识缺口 | 复盘报告 |

### 误解
≥3 条。actual 和 notSaying 必须不同。

### 知识缺口
4–5 项。necessity 含星级和模块标注。

### 语言
短句、主语明确、不堆抽象名词。不把复杂争议讲成单一结论。不用没有解释的英文缩写。不用"显然""本质上"跳过论证。默认中文。

**逻辑检查**：出现 但/因为/所以/而/这说明/这意味着/本质上 → 必须确认：① 前后是否同一问题 ② 中间推理是否补齐 ③ 是原文说的还是你的解释。

**保真检查**：每个核心判断必须确认——原文依据在哪里？是作者明确说的还是推出来的？有没有删掉关键限制条件？有没有为了比喻改变意思？有没有把并列写成因果？

### 术语翻译（输出前必须过）
判断标准：**目标语言从业者实际上管它叫什么**，不是字面直译。

先过 4 测试：
1. **回译**：懂行的人能反推回原词吗？
2. **社区检验**：目标语言技术内容里有人用吗？
3. **独立可懂**：母语者单独看到能猜到意思吗？
4. **失真**：直译丢限定词或改变原意了吗？

三档处理：
- **A 有通用译法**：译名（原文），如 强化学习(reinforcement learning)
- **B 圈内说原词**：保留原词 + 一句解释，如 headless Chrome、prompt、token
- **C 无公认译法/直译荒谬**：保留原词 + 人话解释，绝不硬翻，如 authoring surface

默认：拿不准归 B 或 C，宁可保留原词。反例："无头 Chrome 渲染""编写表面"。

## 自检

- [ ] 3–5 个"能+动词"目标 / 背景包 ≤120 字
- [ ] 3–7 判断各有 sourceText + tags / 推论标注"我的解释"
- [ ] ≤6 概念各有 definition + relations / 结构类型已诊断
- [ ] 题目全部闭环 / 8 字段不空 / review 编号两位数
- [ ] ≥3 误解 actual≠notSaying / knowledgeGaps 含星级
- [ ] content.json 语法有效 / assemble.py 无报错 / node --check 通过
- [ ] 术语翻译已过 4 测试 / 无生硬直译
