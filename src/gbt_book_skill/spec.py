"""The capability contract, copied verbatim from the GBT V8 registry.

Do not hand-edit: ``tests/test_spec.py`` pins every field against the
registry snapshot so drift fails the build instead of shipping quietly.
"""

from __future__ import annotations

import json
from dataclasses import dataclass, field
from typing import Any, Dict, List, Tuple

_RAW = r"""{
 "name": "book_skill",
 "domain": "recon",
 "desc": "**书→技能**（主人令 2026-10-16：把 book-to-skill 变成我们的原生能力）：蒸自 **virgiliojr94/book-to-skill**（MIT）—— 把任何技术书/文档集（PDF·EPUB·DOCX·MD·HTML·RTF·MOBI）变成**结构化技能、按需加载**：提取器（确定性）与生成器（spec 驴动）分开；产物五件（SKILL.md 心智模型+章节索引 · 章节文件按需加载 · 术语表 · 模式表 · 决策表）；**提结构不提摘要**，每条能指回章节:行；按需加载对比全文省 **24×–51×** token（对方实测，未复现）。我们刻意不同：只落**自己的托管目录**、必指出处、必回读验证。op=plan/contract/extract/pack/budget/check/route（**全只读·零作用域**）。",
 "handler": "book_skill",
 "safe": false,
 "external": false,
 "requires_params": false,
 "params": [],
 "params_hint": "",
 "multi_op": true,
 "ops": [
  "plan",
  "contract",
  "extract",
  "pack",
  "budget",
  "check",
  "route"
 ],
 "ops_hint": ""
}"""


@dataclass(frozen=True)
class CapSpec:
    """Immutable description of one capability bit."""

    name: str
    domain: str
    desc: str
    handler: str
    safe: bool
    external: bool
    requires_params: bool
    params: Tuple[str, ...] = ()
    params_hint: str = ""
    multi_op: bool = False
    ops: Tuple[str, ...] = ()
    ops_hint: str = ""

    @property
    def gated(self) -> bool:
        """True when the registry marks this bit ``safe: false``.

        Gated does not mean "dangerous"; it means the action can change state
        that cannot be restored by running the inverse action.
        """
        return not self.safe

    @property
    def summary(self) -> str:
        """First clause of the description, for one-line listings."""
        for sep in ("\uff08", "\uff1b", "\u3002", ";"):
            if sep in self.desc:
                head = self.desc.split(sep, 1)[0].strip()
                if head:
                    return head
        return self.desc.strip()

    def as_dict(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "domain": self.domain,
            "desc": self.desc,
            "handler": self.handler,
            "safe": self.safe,
            "gated": self.gated,
            "external": self.external,
            "requires_params": self.requires_params,
            "params": list(self.params),
            "params_hint": self.params_hint,
            "multi_op": self.multi_op,
            "ops": list(self.ops),
            "ops_hint": self.ops_hint,
        }


_data = json.loads(_RAW)

SPEC = CapSpec(
    name=_data["name"],
    domain=_data["domain"],
    desc=_data["desc"],
    handler=_data["handler"],
    safe=_data["safe"],
    external=_data["external"],
    requires_params=_data["requires_params"],
    params=tuple(_data["params"]),
    params_hint=_data["params_hint"],
    multi_op=_data["multi_op"],
    ops=tuple(_data["ops"]),
    ops_hint=_data["ops_hint"],
)
