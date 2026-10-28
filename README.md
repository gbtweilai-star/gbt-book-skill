# book_skill

**One capability bit from GBT V8, packaged standalone.** No. 193 of 341,
`recon` domain (Recon).

<p>
<img alt="python" src="https://img.shields.io/badge/python-3.9%2B-blue">
<img alt="license" src="https://img.shields.io/badge/license-MIT-green">
<img alt="deps" src="https://img.shields.io/badge/runtime%20dependencies-0-brightgreen">
</p>

> **书→技能**（主人令 2026-10-16：把 book-to-skill 变成我们的原生能力）：蒸自 **virgiliojr94/book-to-skill**（MIT）—— 把任何技术书/文档集（PDF·EPUB·DOCX·MD·HTML·RTF·MOBI）变成**结构化技能、按需加载**：提取器（确定性）与生成器（spec 驴动）分开；产物五件（SKILL.md 心智模型+章节索引 · 章节文件按需加载 · 术语表 · 模式表 · 决策表）；**提结构不提摘要**，每条能指回章节:行；按需加载对比全文省 **24×–51×** token（对方实测，未复现）。我们刻意不同：只落**自己的托管目录**、必指出处、必回读验证。op=plan/contract/extract/pack/budget/check/route（**全只读·零作用域**）。

That description is copied verbatim from the registry. `tests/test_spec.py` pins it,
so documentation drift fails the build instead of shipping quietly.

## What this package actually is

It is the **contract** for one capability: its name, its parameters, the values it
accepts, and whether it can change state that cannot be restored. It is not the
implementation — that lives in the runtime this bit was extracted from.

So `run()` goes through a narrow `Backend` protocol, and the default backend is a
stub that **says so**:

```
status="validated"   backend="stub"   data={"executed": false}
```

Never `status="ok"`. A stub that reports success is worse than no stub, because the
caller stops looking for the real thing.

## Install

```bash
git clone https://github.com/gbtweilai-star/gbt-book-skill.git
cd gbt-book-skill
python -m pip install -e ".[dev]"
```

## Use

```bash
python -m gbt_book_skill info                  # capability card
python -m gbt_book_skill spec --json           # machine-readable contract
python -m gbt_book_skill check --payload '{}'
python -m gbt_book_skill run   --payload '{}'
```

Real `info` output from this machine:

```text
book_skill  (recon)  v1.0.0
----------------------------------------
**书→技能**（主人令 2026-10-16：把 book-to-skill 变成我们的原生能力）：蒸自 **virgiliojr94/book-to-skill**（MIT）—— 把任何技术书/文档集（PDF·EPUB·DOCX·MD·HTML·RTF·MOBI）变成**结构化技能、按需加载**：提取器（确定性）与生成器（spec 驴动）分开；产物五件（SKILL.md 心智模型+章节索引 · 章节文件按需加载 · 术语表 · 模式表 · 决策表）；**提结构不提摘要**，每条能指回章节:行；按需加载对比全文省 **24×–51×** token（对方实测，未复现）。我们刻意不同：只落**自己的托管目录**、必指出处、必回读验证。op=plan/contract/extract/pack/budget/check/route（**全只读·零作用域**）。

gated      : True   <- needs explicit consent
external   : False
multi-op   : True
params     : (none)
values     : plan, contract, extract, pack, budget, check, route
```

Wire a real implementation:

```python
from gbt_book_skill import run

class MyBackend:
    name = "my-backend"
    def invoke(self, cap, payload):
        return {"cap": cap, "handled": sorted(payload)}

result = run({}, backend=MyBackend())
assert result.status == "ok"
```

## Parameters

| name | required | notes |
|---|---|---|
| — | no | the registry declares no required parameters |

Registry hint (`params_hint`): (empty)

**注册表登记的取值 / 子动作（7 个）**：`plan`、`contract`、`extract`、`pack`、`budget`、`check`、`route`

Types are deliberately absent: the registry does not declare them, and an invented
type is worse than no type, because callers believe it.

## Boundaries

- Gated: this bit is marked `safe: false` in the registry — it can change state that no inverse action restores.
- No external service dependency declared.
- Multi-op (`multi_op: true`): several sub-actions share one name — read `op` before calling.
- No implementation ships here. Bring a backend; the protocol is one method.

## What this is not

Not a wrapper around a hosted API. Not a model. Not a promise that calling it does
anything on its own. It is the typed seam plus the validation, which is the part that
stays correct even when the implementation changes.

## Tests

```bash
python -m pytest
```

```text
20 passed, 3 skipped in 0.13s
```

## Provenance

| field | value |
|---|---|
| capability | `book_skill` |
| domain | `recon` |
| handler | `book_skill` |
| safe | `False` (gated = `True`) |
| external | `False` |
| atlas page | [recon/book_skill](https://github.com/gbtweilai-star/gbt-caps/blob/main/caps/recon/book_skill.md) |
| full index | [https://github.com/gbtweilai-star/gbt-caps](https://github.com/gbtweilai-star/gbt-caps) |

The parent README says 348 capabilities; an AST pass over the registry enumerates
`341 + 0 unimplemented + 0 disabled = 341`. The extra 7 are historical duplicates.
Numbering here follows 341 and matches the `gbt-caps` index one-to-one.

## License

MIT.
