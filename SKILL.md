---
name: grokko
description: 把难度较高、跨领域的文稿拆成一份 source-grounded 的交互式 HTML 理解地图。适合想真正学懂复杂文章、访谈、论文、技术长文或跨学科材料的人。核心是保真拆解、原文依据、概念关系、论证结构和苏格拉底式追问；外层可用闯关式任务、关卡、进度和反馈包装，但不得为了趣味牺牲信息准确性。默认用中文输出，除非用户明确指定其他语言。
---

# Grokko

> 把难啃的干货，拆成一张有原文依据、能追问、能复述、能继续学的交互式理解地图。

## 一句话目标

Grokko 的目标不是把难内容“讲简单”，而是把难内容拆成一张**有原文依据、能追问、能复述、能继续学习**的 HTML 理解地图。

Grokko 的内核是：

- 知识拆解报告
- 研究笔记
- 苏格拉底式阅读
- source-grounded（原文依据）理解地图

Grokko 的外壳可以是：

- 闯关式学习路径
- 关卡
- 进度条
- 小任务
- 即时反馈

但优先级必须是：

**保真 > 结构清楚 > 理解友好 > 趣味包装**

---

## 适用场景

适合：

- 技术长文
- 跨领域访谈
- 投资、商业、AI、设计、社会科学类深度文稿
- 论文或研究型文章
- 用户想真正理解，而不是只要摘要

不适合：

- 纯新闻快讯
- API 参数手册
- 只需要行动步骤的教程
- 原文本身没有观点或结构的碎片材料

---

## 核心原则


### 首屏表达规则

第一屏不要写方法论说明或免责声明。

不要出现这类句子：

- “先补最少背景，再读原文判断。”
- “每个核心判断都带原文依据。”
- “背景补充不会伪装成作者原话。”

这些是生成规则，不是读者需要在首屏阅读的内容。

第一屏只保留：

- 主题标题
- 读者会学会什么
- 阅读路径

### 闭环题目规则

Grokko 的互动题必须全部是闭环题。

允许题型：

- 单选题
- 多选题
- 判断题
- 匹配题
- 排序题

禁止题型：

- 开放式文本题
- 长段落自由回答
- 需要读者自己写一段话再由脚本模糊判断的题

如果需要训练“复述”，也要做成选择题：给 3 个复述版本，让读者选择哪个最不改变原意。

### 0. 零基础入口

Grokko 面向的是跨领域深度学习，不是假设读者已经懂这个领域。

正式拆原文之前，必须先补一个“最小背景包”。

最小背景包只解释读懂本文必须知道的 3 到 5 件事。

要求：

- 背景解释必须和原文问题直接相关
- 可以拓展原文没有展开的基础知识，但必须标注为“背景补充”
- 背景补充不能替代原文判断
- 每个背景概念最多 120 字

格式：

```text
背景补充：……
为什么现在需要知道：……
它不是本文的主张，只是帮助你读懂原文。
```

### 1. 保真优先

不要为了好懂而改写作者意思。

每个核心判断后面必须标注“原文依据”。

格式：

```text
核心判断：……
原文依据：……
解释：……
```

如果是你为了帮助理解做出的推论，必须明确标注：

```text
我的解释：……
注意：这不是原文原句，而是基于前后文的理解。
```

### 2. 区分四类信息

每个重要内容都要尽量标注类型：

- 事实：原文明确说了什么
- 判断：作者认为怎样
- 推论：从原文可以推出什么
- 例子：作者用什么案例说明

不要把判断写成事实。

不要把推论写成作者原话。

### 3. 不强行套因果链

不是所有文章都是因果链。

先判断原文结构，再选择合适地图：

- 机制型文章：用流程图
- 观点型文章：用论证图
- 访谈型文章：用主题簇 + 观点线索
- 历史型文章：用时间线
- 商业分析：用问题 → 判断 → 证据 → 风险

如果原文是并列结构，不要硬凑成单一主线。

### 4. 比喻可用，但不能替代定义

比喻只是辅助理解，不是知识本身。

比喻必须标注：

```text
类比：……
它帮助理解：……
它不能代表：……
```

如果比喻会扭曲原文，宁可不用。

### 5. 苏格拉底式引导

关键处不要直接给结论，要用问题帮助读者自己发现结构。

推荐问题：

- 作者真正想回答的问题是什么？
- 这句话是事实、判断，还是推论？
- 作者为什么要在这里引入这个概念？
- 如果删掉这个条件，结论还成立吗？
- 这个例子支持了哪个主张？
- 有没有另一个可能解释？
- 我能不能复述这句话，但不改变原意？

### 6. 闯关式包装，但不游戏化过度

可以使用：

- 学习路径
- 关卡
- 进度条
- 小测
- 即时反馈
- 错题回流
- 学习报告

但所有任务必须服务理解原文。

不要出为了互动而互动的题。

不要把复杂观点压成过度简单的选择题。

---

## 输出要求

- 输出一个自包含的 `.html` 文件
- 默认保存到当前工作目录
- 如果用户要求放到下载目录，保存到 `~/Downloads/`
- 文件名格式：`<原文标题> - 理解地图.html`（默认中文；仅当用户明确要求英文或其他语言时，才使用对应语言的文件名后缀，例如 `<Title> - Understanding Map.html`）
- HTML 可直接双击打开
- 可以使用少量原生 JavaScript
- 不依赖后端
- **默认输出中文**：无论原文是中文、英文还是其他语言，默认都用中文生成理解地图；原文依据可以保留原文原句，并在必要时附中文解释。只有用户明确指定英文或其他语言时，才按用户指定语言输出。

### 页脚署名（默认）

每个生成的 HTML 在页脚放一行简短的项目署名（默认开启）：

```text
由 Grokko 生成 · github.com/<your-username>/grokko
```

要求：

- 「Grokko」可做成指向仓库的可见链接（蓝色 + 下划线，`target="_blank" rel="noopener"`）
- 默认**不输出任何个人署名**
- 另可保留一句友好的学习提醒（默认中文，除非用户指定其他语言），例如：「这个工具能帮你预习难啃的干货，但不能代替完整学习。学习愉快」

可选 · 个人署名（默认关闭）：

- 仅当用户明确要求时，才在项目署名后另起一行加入用户自己的名字/链接
- 推荐写法：`—— <a href="https://用户的网站" target="_blank" rel="noopener" style="color:#1d70b8;text-decoration:underline;font-weight:600">名字</a>`
- 用户未配置时，不要输出个人署名，也不要填入任何默认人名或网址

---

## 页面结构

必须包含下面 11 个模块。
### 页面框架建议

Grokko 默认采用这个顺序：

1. 学习目标与阅读路径
2. 零基础背景包
3. 原文问题定位
4. 原文结构地图
5. 核心判断与依据
6. 关键概念拆解
7. 苏格拉底式阅读关卡
8. 闯关式任务包装
9. 误解与边界
10. 背景知识缺口
11. 复盘与学习报告

第一屏不要放抽象说明，不要放“学习契约”。读者一进来应该立刻知道：我要学会什么，为什么要先补哪些背景。


### 1. 学习目标与阅读路径

第一屏直接告诉读者：

- 这篇内容要学会什么
- 为什么需要先补背景
- 接下来会按什么顺序学习

不要把“学习契约”单独做成一个大模块。保真原则可以放在页脚或小提示里，不要占据第一屏。

### 2. 零基础背景包

列出 3 到 5 个可检查目标。

目标必须是动作，不是口号。

好目标：

- 能说出作者在回答什么问题
- 能区分 3 个核心判断和它们的原文依据
- 能解释 4 个关键概念之间的关系
- 能指出至少 2 个容易误解的地方
- 能提出 1 个后续追问

差目标：

- 理解全文
- 掌握思想
- 学会技术


### 2. 零基础背景包

在进入原文拆解前，先解释读懂本文必须知道的基础概念。

要求：

- 只补 3 到 5 个概念
- 每个概念都说明“为什么读本文需要它”
- 明确标注为“背景补充”
- 不能把背景补充写成作者原文观点

### 3. 原文问题定位

回答：

- 这篇文稿表面在讲什么？
- 它深层在回答什么问题？
- 作者为什么要写这篇？
- 读者如果只记一个问题，应该记哪个？

每个判断都要带原文依据。

### 4. 原文结构地图

先判断文章结构类型，再画地图。

可选结构：

- 时间线
- 机制流程
- 论证结构
- 主题簇
- 问题树
- 冲突结构

要求：

- 不强行改造成因果链
- 每个节点标注原文依据
- 节点之间的关系要写清楚：因果、并列、递进、对比、例证、转折

### 5. 核心判断与依据

提取 3 到 7 个核心判断。

每个判断必须包含：

- 核心判断
- 原文依据
- 这是事实 / 判断 / 推论 / 例子
- 为什么重要
- 可能的误读

### 6. 关键概念拆解

选择最多 6 个关键概念。

每个概念包含：

- 原文术语
- 作者在文中怎么使用它
- 人话解释
- 它和其他概念的关系
- 原文依据
- 不要误解成什么

注意：

概念解释不能只靠比喻。

先给定义，再给辅助理解。

### 7. 苏格拉底式阅读关卡

设计 5 到 8 个问题。

问题按难度递进：

1. 这段在回答什么？
2. 这句话属于事实、判断还是推论？
3. 这个例子支持哪个主张？
4. 这里少了哪个隐含前提？
5. 如果反过来看，作者可能忽略了什么？
6. 我如何不改变原意地复述？
7. 这个观点能迁移到哪里？

每题必须有：

- 问题
- 输入或选择区
- 参考答案
- 原文依据
- 反馈

### 8. 闯关式任务包装

把严肃阅读包装成任务，但任务必须保真。

推荐任务类型：

- 标注题：这句话是事实、判断还是推论？
- 匹配题：把判断和原文依据配对
- 补全题：补全概念关系
- 复述题：用自己的话重写，但不能改变原意
- 纠错题：指出一个错误理解哪里错了
- 迁移题：把观点迁移到新场景

禁止任务：

- 只考生僻词拼写
- 答案明显到不用思考
- 为了好玩而脱离原文
- 用比喻替代原文概念

### 9. 误解与边界

列出至少 3 个容易误解的地方。

每条包含：

- 可能误解
- 为什么容易误解
- 原文真正说了什么
- 原文没有说什么
- 如何避免这个误解

### 10. 背景知识缺口

告诉读者：

- 要完全理解这篇，还需要补哪些背景
- 哪些背景现在可以先不补
- 每个背景知识为什么重要
- 推荐下一步学习问题

不要把背景知识展开成另一门课。

### 11. 复盘与学习报告

最后生成学习报告。

包括：

- 我现在理解了什么
- 哪些判断有原文依据
- 哪些地方仍不确定
- 我容易误解什么
- 下一步该追问什么

如果使用 JS，可以生成可复制的学习报告。

---

## 互动规则

HTML 可以使用原生 JavaScript。

推荐功能：

- 进度条
- 掌握状态
- 错题回流
- 答案折叠
- 原文依据展开
- 学习报告生成

所有互动必须服务理解，不服务炫技。


### 交互实现稳定性

互动题必须真的可用。

生成 HTML 时优先使用稳定的 `data-*` 题目系统，而不是把复杂逻辑都写进 `onclick` 字符串。

每道题至少包含：

- `data-task`
- `data-answer`
- `data-goal`
- `.feedback` 反馈区域


交互反馈必须出现在按钮附近，并且默认占位可见。

反馈区不能使用 `display:none` 作为默认状态。默认状态应该显示“选择后点击检查，这里会显示反馈”。点击后只改变文案和正确/错误样式。

生成后必须检查：

- 所有按钮都能触发反馈
- 答对和答错都有不同反馈
- 错题能进入错题回流区
- 刷新页面后进度不会破坏页面
- JS 语法检查通过

### 答题反馈

反馈必须包含：

- 为什么这个答案合理
- 它对应哪条原文依据
- 如果答错，可能误解了什么
- 回到哪个模块复习

### 错题回流

答错后不要只显示“错误”。

必须告诉读者：

- 你错在事实、判断、推论，还是概念关系
- 应该回到哪个原文依据
- 哪个模块可以复习

---

## 互动引擎（固定脚本 · 跨模型保证）

> 这是为了保证在不同模型（Opus、Codex、其他）下互动题都能正常工作。
> 不同模型自己手写互动 JS 时，常出现“点了检查没反应”的 bug（绑定时机错、选择器错、脚本中途报错）。
> 解决办法：逻辑不交给模型写，统一用下面这段固定引擎。

### 必须遵守

1. 下面的 `<script>` 引擎必须**原样复制粘贴**到 HTML 最末尾（`</body>` 前），**不许改写其中逻辑**。
2. 模型只负责写题目 HTML，并把答案与反馈全部放进 `data-*` 属性里（不要再单独维护一个 JS 答案对象，避免和题目对不上）。
3. 引擎采用 **事件委托**（在 document 上监听），所以无论 DOM 何时生成、脚本放在哪里都能工作——这是跨模型稳定的关键，不要改成逐个元素提前绑定。
4. 生成后仍要抽取 script 跑 `node --check` 确认语法。

### 题目 HTML 契约（模型只填这些）

```html
<!-- 单选：data-answer 填正确项的 data-val -->
<div class="task" data-task="q1" data-answer="B"
     data-ok="为什么对 + 原文依据" data-no="答错可能误解了什么"
     data-src="原文：……" data-review="回到「第X模块」复习">
  <div class="q">题干</div>
  <div class="opts">
    <button class="opt" data-val="A">A. ……</button>
    <button class="opt" data-val="B">B. ……</button>
  </div>
  <button class="check">检查</button>
  <div class="feedback" aria-live="polite">选择后点击检查，这里会显示反馈。</div>
</div>

<!-- 多选：data-multi="true"，data-answer 用逗号，如 "A,C" -->
<!-- 匹配/排序：data-type="selects"，每个 <select class="match" data-correct="x"> -->
```

字段说明：`data-answer` 答案；`data-multi` 多选；`data-type="selects"` 下拉匹配；`data-ok/-no/-src/-review` 是反馈文案。引擎只读这些属性，不依赖任何外部 JS 对象。

> 默认输出中文，因此契约与引擎里的中文界面文案通常保持中文即可。只有用户明确要求输出为非中文时，才把少量中文界面文案（如“选择后点击检查”“请先选择一个选项再检查”“学习报告”等）翻译成对应语言；逻辑代码不要改。

### 固定引擎（原样粘贴）

```html
<script>
(function(){
  "use strict";
  function $all(s,r){return Array.prototype.slice.call((r||document).querySelectorAll(s));}
  function selectedVals(t){return $all('.opt.selected',t).map(function(o){return o.getAttribute('data-val');}).sort();}
  function setFb(t,state,html){var fb=t.querySelector('.feedback');if(!fb)return;fb.className='feedback'+(state?(' '+state):'');fb.innerHTML=html;}
  function updateBar(){
    var all=$all('.task'),done=$all('.task[data-answered="1"]');
    var fill=document.getElementById('barFill'),num=document.getElementById('barNum');
    if(fill)fill.style.width=all.length?(done.length/all.length*100)+'%':'0%';
    if(num)num.textContent=done.length+' / '+all.length;
  }
  function renderWrong(){
    var box=document.getElementById('wrongBox');if(!box)return;
    var wrong=$all('.task[data-answered="1"][data-correct="0"]');
    if(!wrong.length){box.innerHTML='<li style="color:#888">还没有错题。答错的题会自动收集到这里。</li>';return;}
    box.innerHTML='';
    wrong.forEach(function(t){var li=document.createElement('li');li.textContent='【'+(t.getAttribute('data-task')||'')+'】'+(t.getAttribute('data-review')||'回到对应模块复习');box.appendChild(li);});
  }
  function check(t){
    var type=t.getAttribute('data-type'),ok=false;
    if(type==='selects'){
      var sels=$all('select.match',t),allok=true,empty=false;
      sels.forEach(function(s){if(!s.value)empty=true;if(s.value!==s.getAttribute('data-correct'))allok=false;});
      if(empty){setFb(t,'no','请先把每一项都选好再检查。');return;}
      ok=allok;
    }else{
      var sel=selectedVals(t);
      if(!sel.length){setFb(t,'no','请先选择一个选项再检查。');return;}
      var ans=(t.getAttribute('data-answer')||'').split(',').map(function(x){return x.trim();}).sort();
      ok=(sel.join('|')===ans.join('|'));
    }
    var body=ok?(t.getAttribute('data-ok')||'回答正确。'):(t.getAttribute('data-no')||'再想想。');
    var src=t.getAttribute('data-src');
    setFb(t,ok?'ok':'no',(ok?'✅ ':'❌ ')+body+(src?('<span class="src">'+src+'</span>'):''));
    t.setAttribute('data-answered','1');t.setAttribute('data-correct',ok?'1':'0');
    updateBar();renderWrong();
  }
  function genReport(){
    var box=document.getElementById('report');if(!box)return;
    var all=$all('.task'),done=$all('.task[data-answered="1"]'),right=$all('.task[data-answered="1"][data-correct="1"]');
    var lines=['=== 学习报告 ===','完成题目：'+done.length+' / '+all.length,'答对：'+right.length+' 题',''];
    var wrong=$all('.task[data-answered="1"][data-correct="0"]');
    if(wrong.length){lines.push('我答错的题（建议复习）：');wrong.forEach(function(t){lines.push('- '+(t.getAttribute('data-task')||'')+'：'+(t.getAttribute('data-review')||''));});}
    else{lines.push('暂无错题。');}
    box.textContent=lines.join('\n');
  }
  document.addEventListener('click',function(e){
    var c=e.target.closest?e.target:null;
    var opt=c&&e.target.closest('.opt');
    if(opt){var t=opt.closest('.task');if(!t)return;
      if(t.getAttribute('data-multi')==='true'){opt.classList.toggle('selected');}
      else{$all('.opt',t).forEach(function(o){o.classList.remove('selected');});opt.classList.add('selected');}
      return;}
    var btn=c&&e.target.closest('.check');
    if(btn){var tk=btn.closest('.task');if(tk)check(tk);return;}
    if(e.target&&e.target.id==='genReport'){genReport();return;}
    if(e.target&&e.target.id==='copyReport'){var r=document.getElementById('report');if(r&&navigator.clipboard)navigator.clipboard.writeText(r.textContent);return;}
  });
  function init(){updateBar();renderWrong();}
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
</script>
```

### 为什么这样能跨模型稳定

- 逻辑固定、原样粘贴：模型不再自己发明绑定方式，消除“点了没反应”的根因。
- 事件委托：点击通过冒泡在 document 捕获，不依赖“脚本必须在元素生成后运行”，时机问题被绕过。
- 全部数据放在 `data-*`：答案和反馈与题目同处一地，模型不会把答案对象写得和题目对不上。

---

## 语言规则

### 基本要求

- 短句
- 主语明确
- 不堆抽象名词
- 不把复杂争议讲成单一结论
- 不用没有解释的英文缩写
- 不用“显然”“本质上”来跳过论证

### 逻辑检查

重点检查这些词：

- 但
- 因为
- 所以
- 而
- 这说明
- 这意味着
- 本质上

如果出现因果或转折，必须确认：

1. 前后是否讲同一个问题
2. 中间推理是否补齐
3. 这是不是原文说的，还是你的解释

### 保真检查

每个核心判断都问：

- 原文依据在哪里？
- 这是作者明确说的，还是我推出来的？
- 有没有删掉关键限制条件？
- 有没有为了比喻改变意思？
- 有没有把并列关系写成因果关系？

### 术语翻译规则（跨语言处理）

不要逐字直译技术术语。判断标准只有一句话：**目标语言的从业者实际上管它叫什么**，而不是“这个词字面怎么译”。

字面直译会产生不知所云的伪翻译，例如把 headless Chrome 译成「无头 Chrome 渲染」、把 authoring surface 译成「编写表面」。这是必须避免的失败。

每个术语先过 4 个测试：

1. 回译测试：把你的译名给懂行的人，他能反推回原词吗？「上下文窗口」能想到 context window（通过）；「无头 Chrome」没人反推得出 headless（不通过）。
2. 社区检验：这个说法在真实的目标语言技术内容里有人用吗？临时造出来、零命中的词不要用。
3. 独立可懂测试：译名单独拿出来，母语者能猜到意思吗？「神经网络」能，「编写表面」不能。
4. 失真测试：直译有没有丢限定词或改变原意？

然后分三档处理：

- A 有通用译法：用目标语言，首次出现可附原文。例（中文）：强化学习(reinforcement learning)、上下文窗口(context window)、预训练、权重、扩散模型。
- B 圈内本就说原词：保留原词 + 一句解释。例：headless Chrome、prompt、token、agent、DOM、GSAP、vibe coding。
- C 无公认译法 / 直译荒谬：保留原词 + 一句人话解释，绝不硬翻。例：authoring surface、source of truth、round-trip、BeginFrame。

默认原则：拿不准就归到 B 或 C，宁可保留原词，也不要造一个生硬直译。

格式建议：

```text
有通用译法：译名（原文）
保留原词：原文 —— 一句解释（这是什么、读本文为什么需要）
```

---

## 视觉规则

风格：研究报告 × 学习 App。

使用下面 CSS 变量：

```css
:root{
  --cream:#FAF6EB;
  --paper:#F3EDDD;
  --forest:#1E3A24;
  --sky:#BCD8EE;
  --sage:#AFCDA8;
  --ink:#1A2018;
  --marker:#F5E08A;
  --brick:#B5482A;
  --correct:#2F7D46;
  --wrong:#B5482A;
  --font-display:"Archivo Black","Noto Sans SC","PingFang SC",sans-serif;
  --font-head:"Poppins","Noto Sans SC","PingFang SC",sans-serif;
  --font-body:-apple-system,"PingFang SC","Noto Sans SC",sans-serif;
  --font-mono:"Roboto Mono","JetBrains Mono",monospace;
  --radius-pill:999px;
  --radius-card:14px;
}
```

要求：

- 原文依据要有明显样式
- 作者观点和辅助解释要视觉区分
- 互动任务要像关卡，但不要喧宾夺主
- 每张卡片文字不要太满
- 移动端单列
- 不使用阴影、渐变、毛玻璃

### 版式与布局（强制）

整页采用「左侧固定侧边栏 + 右侧单列主区」的两栏骨架。除侧边栏外，主区内所有内容一律纵向堆叠。

1. **左侧固定侧边栏**（桌面端 `position: sticky` 或 `fixed`，随页面常驻）：
   - 顶部：主题标题
   - 任务进度条（如 `0/8`）
   - 完整导航栏（01~11 各模块的锚点链接，点击跳转）
   - 侧边栏宽度建议 240~300px，深色背景与主区区分

2. **右侧主区：严格单列、全部纵向**。
   - 学习目标（目标 1/2/3…）**纵向逐条堆叠**，禁止做成横向网格或一排多卡。
   - 背景包、核心判断、概念卡、关卡题、误解卡等，**全部一张一张竖直往下排**。
   - 禁止任何 `display:flex; flex-direction:row` 或多列 `grid` 把卡片横向并排。卡片之间只有上下关系，没有左右并排。

3. **唯一允许的并排**：只有「左侧边栏 vs 右侧主区」这一处是左右布局；主区内部不得再出现左右并排。

4. **移动端**：侧边栏收起或移到顶部，主区依旧单列纵向。

> 反例（禁止）：把目标 1~5 做成一行五个方块、把背景概念做成 2~3 列网格。
> 正例（要求）：目标 1 在上、目标 2 在下……依次竖排；每个背景概念独占一行宽度。

---

## 生成流程

1. 读完原文
2. 提取作者在回答的问题
3. 判断原文结构类型
4. 提取核心判断
5. 给每个判断找原文依据
6. 区分事实、判断、推论、例子
7. 拆关键概念和概念关系
8. 设计苏格拉底问题
9. 设计闯关式任务
10. 写误解与边界
11. 写背景知识缺口
12. 生成 HTML（左侧边栏 + 右侧单列，粘贴固定互动引擎）
13. 检查保真、语言、互动和布局

---

## 最终自检清单

- [ ] 是否有 3 到 5 个可检查学习目标？
- [ ] 是否有零基础背景包？
- [ ] 背景补充是否和原文判断分开？
- [ ] 是否判断了原文结构类型？
- [ ] 是否每个核心判断都有原文依据？
- [ ] 是否区分事实、判断、推论、例子？
- [ ] 是否没有强行套因果链？
- [ ] 是否没有用比喻替代定义？
- [ ] 是否有苏格拉底式问题？
- [ ] 是否有闯关式任务包装？
- [ ] 是否有误解与边界？
- [ ] 是否有背景知识缺口？
- [ ] 是否有复盘与学习报告？
- [ ] 是否检查了“但/因为/所以/这意味着”等逻辑连接？
- [ ] 是否避免信息失真？
- [ ] 所有互动题是否真的可点击、可反馈、可记录？
- [ ] 首屏是否删除了方法论说明和免责声明？
- [ ] 是否没有开放式文本题？
- [ ] 反馈区默认是否可见，而不是 display:none？
- [ ] 术语是否做了恰当跨语言处理，没有出现「无头 Chrome 渲染」式的生硬直译？
- [ ] 是否原样粘贴了「固定互动引擎」，没有让模型自己另写互动 JS？
- [ ] 题目是否只用 data-* 属性承载答案与反馈，且每题点击「检查」都真有反应？
- [ ] 是否左侧固定「任务进度 + 导航栏」侧边栏，右侧主区单列？
- [ ] 主区内是否全部纵向堆叠（目标 1-5、各类卡片），没有任何卡片横向并排？
- [ ] 输出语言是否默认为中文，且仅在用户明确指定时才改用其他语言？
- [ ] 页脚是否为项目署名、默认未植入任何个人名字或网址？

---

## 成功标准

读者完成后应该能做到：

- 说出作者真正回答的问题
- 列出核心判断及其原文依据
- 区分原文事实、作者判断和辅助解释
- 解释关键概念之间的关系
- 指出容易误解的地方
- 提出下一步值得追问的问题

Grokko 的目标不是“轻松看完”，而是“准确理解”。

## 互动题稳定性（与固定引擎配合）

生成 HTML 互动题时必须满足：

1. 题目只使用选择题、判断题、匹配题、排序题等可闭环题型；不要用开放式 textarea 作为题目（textarea 只能用于只读学习报告）。
2. 每个题块必须包含 data-task、data-answer、check 按钮、feedback 反馈区。
3. feedback 默认必须可见，初始文案写：选择后点击检查，这里会显示反馈。不要用 display:none。
4. 互动逻辑统一使用上文「固定互动引擎」，原样粘贴并放在 `</body>` 前；不要让模型自己另写绑定逻辑（引擎已用事件委托，不需要再逐个按钮绑定）。
5. 生成文件后必须抽取 script 内容并运行 `node --check`，确认没有语法错误。
