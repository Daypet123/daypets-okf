---
type: Migration Plan
title: Phase 0 掃描報告
description: OKF bundle 建立前的全面掃描報告，記錄搬遷清單與引用更新清單
tags: [migration, phase0, planning]
timestamp: 2026-06-23T00:00:00Z
---

# Phase 0 掃描報告：搬遷清單 + 引用更新清單

> 掃描日期：2026-06-23
> 掃描範圍：7 個 SKILL 資料夾（contentful-uploader 僅參考）

---

## 一、搬遷清單

### A. 已確認搬遷（來自 welly-seo-writer，為各檔案的最完整版本）

| # | 來源資料夾 | 來源檔案 | 內容摘要 | 搬到 bundle 位置 | 其他資料夾的重複版本 |
|---|-----------|---------|---------|-----------------|-------------------|
| 1 | welly-seo-writer | `clients/daypets/brand.md` | 品牌定位、語氣光譜、目標受眾、禁止事項 | `brand/brand-positioning.md` | seo-major-revision 有擴充版 `brand-voice.md`（⚠️ 見下方衝突說明） |
| 2 | welly-seo-writer | `clients/daypets/tone-and-manner.md` | 語氣人設、口語/書面平衡、H2/H3 格式慣例 | `brand/tone-and-manner.md` | seo-major-revision 的 `brand-voice.md` 合併了此檔 + brand.md 並擴充 |
| 3 | welly-seo-writer | `clients/daypets/cta-template.md` | CTA 公版：FAQ 後收尾段、3 條延伸閱讀連結 | `brand/cta-template.md` | seo-major-revision `cta-template.md`（完全相同） |
| 4 | welly-seo-writer | `clients/daypets/content-library.md` | 文章庫 CSV 來源、快取策略、內鏈規則 | `articles/content-library.md` | seo-major-revision `content-library.md`（完全相同） |
| 5 | welly-seo-writer | `references/punctuation-rules.md` | 台灣教育部標點符號規範 | `editorial/punctuation-rules.md` | 推薦文 ✅相同、小文 ref/ ✅相同、小文 references/ ✅相同 |
| 6 | welly-seo-writer | `references/writing-rules.md` | 通用寫作規範（段落結構、粗體、去 AI 感） | `editorial/writing-rules.md` | 推薦文 ⚠️缺少「中英並列」規則和「嚴守段落主題」段落（welly 版最完整） |
| 7 | welly-seo-writer | `references/richness-principles.md` | Parity + Gap-Fill 內容豐富度框架 | `editorial/richness-principles.md` | 推薦文 ✅相同 |
| 8 | welly-seo-writer | `references/structure-rules.md` | 架構規則、標題策略、15 條檢核清單 | `editorial/structure-rules.md` | 推薦文 ✅相同 |
| 9 | welly-seo-writer | `references/structure-examples.md` | 10 篇人類文章架構分析 | `editorial/structure-examples.md` | 推薦文 ⚠️缺少 cross-reference 註記且內容區段略有不同（welly 版較新） |
| 10 | welly-seo-writer | `memory.md` | 決策日誌、規則變更記錄 | `log.md` | 無重複（各資料夾各有自己的 memory.md，內容不同） |

### B. 需要你決定的版本衝突

| # | 檔案 | 衝突說明 | 建議 |
|---|------|---------|------|
| 11 | `quality-standards.md` | **三個版本不一致**：welly-seo-writer 版有「五、事實查證」段落；小文撰寫者/references/ 版多了「段落長度規範」（每段 ≤6 行）；推薦文版 = 小文 ref/ 版 = 最精簡版。三個版本的核心內容（魚骨法、金字塔、T1-T6）相同。 | **合併** welly 的事實查證 + 小文的段落長度規範 → bundle 版最完整 |
| 12 | `brand-voice.md`（seo-major-revision） | 這是 welly-seo-writer 的 `brand.md` + `tone-and-manner.md` 的**超集**，額外加了：AI 詞黑名單、必修改模式表、魚骨法整合、Experience 句型模板、句子節奏規則（約多 30 條規則）。但它是專為「改稿」場景寫的。 | **方案 A**：brand-positioning.md + tone-and-manner.md 保持原樣，另建 `brand/brand-voice-revision-addendum.md` 收錄擴充部分。**方案 B**：直接以 brand-voice.md 作為 bundle 的主要品牌文件，取代 brand.md + tone-and-manner.md。 |

### C. 新發現：應搬入 bundle 的檔案

| # | 來源資料夾 | 來源檔案 | 內容摘要 | 建議搬到 bundle 位置 | 重複版本 |
|---|-----------|---------|---------|---------------------|---------|
| 13 | seo-major-revision | `references/eeat-checklist.md` | E-E-A-T 品質檢核（寵物健康 YMYL 內容）| `seo/eeat-checklist.md` | 無 |
| 14 | seo-major-revision | `references/google-algo-signals.md` | Google 演算法信號指南（HCU、People-first 測試）| `seo/google-algo-signals.md` | 無 |
| 15 | seo-major-revision | `references/lagging-analysis-framework.md` | SEO 落後分析框架（6 維度診斷）| `seo/lagging-analysis-framework.md` | 無 |
| 16 | 小文撰寫者 | `references/type-kouBei.md` | 口碑小文類型規格（300-500 字、第一人稱）| `brand/article-types/type-kouBei.md` | 無 |
| 17 | 小文撰寫者 | `references/type-touGao.md` | 投稿小文類型規格（500-850 字、第三人稱）| `brand/article-types/type-touGao.md` | 無 |
| 18 | 小文撰寫者 | `references/type-waiLian.md` | 外鏈小文類型規格（400-800 字、部落客風）| `brand/article-types/type-waiLian.md` | 無 |
| 19 | 小文撰寫者 | `references/sample-kouBei.md` | 口碑文範例（布偶貓/緬因貓/挪威森林貓）| `brand/article-types/sample-kouBei.md` | 無 |
| 20 | 小文撰寫者 | `references/sample-touGao.md` | 投稿文範例（季節性狗狗照護）| `brand/article-types/sample-touGao.md` | 無 |
| 21 | 毛健康關鍵字策略 | `spec.md` | 關鍵字策略方法論（6 階段分析流程、信心評分、分群規則）| `seo/keyword-clusters/strategy-spec.md` | 無 |

### D. 不搬遷的檔案（確認排除）

| 來源資料夾 | 檔案 | 排除原因 |
|-----------|------|---------|
| welly-seo-writer | `references/skill-design-principles.md` | Meta 設計原則，非內容知識 |
| welly-seo-writer | `SKILL.md`, `prompts/`, `scripts/` | Pipeline 指令 |
| welly-seo-writer | `daypets-internal-link-phase4-prompt.md` | Contentful 批次更新的 handoff prompt |
| welly-seo-writer | `output/` 全部 | 歷史產出，非知識 |
| welly-seo-writer | `clients/yt-market/` | 非 daypets 品牌 |
| 小文撰寫者 | `SKILL.md`, `agents/`, `scripts/` | Pipeline 指令 |
| 小文撰寫者 | `ref/skill-design-principles.md` | 同 welly 的 skill-design-principles（排除） |
| 小文撰寫者 | `ref/punctuation-rules.md`, `ref/quality-standards.md` | 內部重複（references/ 已有）→ 搬遷後一併清理 |
| 小文撰寫者 | `memory.md` | 含文章庫快照 + 已完成生產紀錄，屬專案狀態非共用知識 |
| 推薦文 | `spec.md` | Pipeline 指令 |
| 推薦文 | `memory.md` | 含競品分析 + references 摘要彙整，屬專案狀態 |
| 推薦文 | `references/skill-design-principles.md` | Meta 設計原則 |
| seo-major-revision | `SKILL.md`, `session-issues-log.md` | Pipeline 指令 |
| seo-major-revision | `references/revision-types.md` | 改稿指令模板（6 種），屬 pipeline 專用 |
| seo-major-revision | `references/self-review-rules.md` | QA 流程規則，屬 pipeline 專用 |
| seo-major-revision | `output/` 全部 | 歷史產出 |
| 大小改自動化 | 全部 4 檔 | 全為監控系統的 pipeline 指令和偵測規則 |
| 毛健康關鍵字策略 | `keyword-strategy/SKILL.md` | Pipeline 指令 |
| 毛健康關鍵字策略 | `memory.md` | 含 API key、專案狀態，非共用知識 |
| 毛健康關鍵字策略 | `keyword-strategy/` 下的 scripts/, assets/ | 腳本和設定 |
| 毛健康關鍵字策略 | `.xlsx` 檔案 | 二進位產出，不適合 OKF |
| contentful-uploader | 全部 | API 工具，不搬遷 |

---

## 二、引用更新清單

搬遷後，以下 SKILL 檔案裡的路徑需要改指向 bundle：

### welly-seo-writer

| 需更新的檔案 | 原始引用路徑 | 改為指向 bundle |
|-------------|-------------|----------------|
| `SKILL.md` | `clients/{CLIENT}/brand.md` | `→ OKF bundle: brand/brand-positioning.md` |
| `SKILL.md` | `clients/{CLIENT}/cta-template.md` | `→ OKF bundle: brand/cta-template.md` |
| `SKILL.md` | `clients/{CLIENT}/content-library.csv` / `.md` | `→ OKF bundle: articles/content-library.md` |
| `SKILL.md` | `references/structure-rules.md` | `→ OKF bundle: editorial/structure-rules.md` |
| `SKILL.md` | `references/structure-examples.md` | `→ OKF bundle: editorial/structure-examples.md` |
| `SKILL.md` | `references/richness-principles.md` | `→ OKF bundle: editorial/richness-principles.md` |
| `SKILL.md` | `references/writing-rules.md` | `→ OKF bundle: editorial/writing-rules.md` |
| `SKILL.md` | `references/quality-standards.md` | `→ OKF bundle: editorial/quality-standards.md` |
| `SKILL.md` | `references/punctuation-rules.md` | `→ OKF bundle: editorial/punctuation-rules.md` |
| `prompts/claude-structure-system.md` | `references/structure-rules.md` | `→ OKF bundle: editorial/structure-rules.md` |
| `prompts/claude-structure-system.md` | `references/structure-examples.md` | `→ OKF bundle: editorial/structure-examples.md` |
| `prompts/claude-structure-system.md` | `references/richness-principles.md` | `→ OKF bundle: editorial/richness-principles.md` |
| `prompts/claude-writer-qa.md` | `clients/{CLIENT}/brand.md` | `→ OKF bundle: brand/brand-positioning.md` |
| `prompts/claude-writer-qa.md` | `clients/{CLIENT}/cta-template.md` | `→ OKF bundle: brand/cta-template.md` |
| `prompts/claude-writer-qa.md` | `clients/{CLIENT}/content-library.md` | `→ OKF bundle: articles/content-library.md` |
| `prompts/claude-writer-qa.md` | `references/writing-rules.md` | `→ OKF bundle: editorial/writing-rules.md` |
| `prompts/claude-writer-qa.md` | `references/richness-principles.md` | `→ OKF bundle: editorial/richness-principles.md` |
| `prompts/claude-writer-qa.md` | `references/quality-standards.md` | `→ OKF bundle: editorial/quality-standards.md` |
| `prompts/claude-writer-qa.md` | `references/punctuation-rules.md` | `→ OKF bundle: editorial/punctuation-rules.md` |

搬遷後刪除：`clients/daypets/` 整個資料夾、`references/` 下 6 個已搬檔案（保留 `skill-design-principles.md`）

### 小文撰寫者

| 需更新的檔案 | 原始引用路徑 | 改為指向 bundle |
|-------------|-------------|----------------|
| `agents/02-outline.md` | `references/quality-standards.md` | `→ OKF bundle: editorial/quality-standards.md` |
| `agents/02-outline.md` | `references/type-kouBei.md` | `→ OKF bundle: brand/article-types/type-kouBei.md` |
| `agents/02-outline.md` | `references/type-touGao.md` | `→ OKF bundle: brand/article-types/type-touGao.md` |
| `agents/02-outline.md` | `references/type-waiLian.md` | `→ OKF bundle: brand/article-types/type-waiLian.md` |
| `agents/03-writer.md` | `references/punctuation-rules.md` | `→ OKF bundle: editorial/punctuation-rules.md` |
| `agents/03-writer.md` | `references/quality-standards.md` | `→ OKF bundle: editorial/quality-standards.md` |
| `agents/03-writer.md` | `references/type-kouBei.md` + `sample-kouBei.md` | `→ OKF bundle: brand/article-types/` |
| `agents/03-writer.md` | `references/type-touGao.md` + `sample-touGao.md` | `→ OKF bundle: brand/article-types/` |
| `agents/03-writer.md` | `references/type-waiLian.md` | `→ OKF bundle: brand/article-types/type-waiLian.md` |

搬遷後刪除：`ref/` 整個資料夾、`references/` 下所有已搬檔案

### 推薦文

| 需更新的檔案 | 原始引用路徑 | 改為指向 bundle |
|-------------|-------------|----------------|
| `spec.md` | `references/punctuation-rules.md` | `→ OKF bundle: editorial/punctuation-rules.md` |
| `spec.md` | `references/quality-standards.md` | `→ OKF bundle: editorial/quality-standards.md` |
| `spec.md` | `references/richness-principles.md` | `→ OKF bundle: editorial/richness-principles.md` |
| `spec.md` | `references/structure-examples.md` | `→ OKF bundle: editorial/structure-examples.md` |
| `spec.md` | `references/structure-rules.md` | `→ OKF bundle: editorial/structure-rules.md` |
| `spec.md` | `references/writing-rules.md` | `→ OKF bundle: editorial/writing-rules.md` |

搬遷後刪除：`references/` 下 7 個檔案全部（含 skill-design-principles.md，因推薦文用不到）

### seo-major-revision-daypets

| 需更新的檔案 | 原始引用路徑 | 改為指向 bundle |
|-------------|-------------|----------------|
| `SKILL.md` | `references/brand-voice.md` | `→ OKF bundle: brand/brand-positioning.md` + 擴充 addendum（視決定） |
| `SKILL.md` | `references/content-library.md` | `→ OKF bundle: articles/content-library.md` |
| `SKILL.md` | `references/cta-template.md` | `→ OKF bundle: brand/cta-template.md` |
| `SKILL.md` | `references/eeat-checklist.md` | `→ OKF bundle: seo/eeat-checklist.md` |
| `SKILL.md` | `references/google-algo-signals.md` | `→ OKF bundle: seo/google-algo-signals.md` |
| `SKILL.md` | `references/lagging-analysis-framework.md` | `→ OKF bundle: seo/lagging-analysis-framework.md` |

搬遷後刪除：`references/` 下已搬的 6 個檔案（保留 `revision-types.md` 和 `self-review-rules.md`）

### 毛健康關鍵字策略

| 需更新的檔案 | 原始引用路徑 | 改為指向 bundle |
|-------------|-------------|----------------|
| `keyword-strategy/SKILL.md` | `../spec.md`（隱性引用）| `→ OKF bundle: seo/keyword-clusters/strategy-spec.md` |

搬遷後刪除：根目錄的 `spec.md`（SKILL.md 和 memory.md 保留原位）

### 大小改自動化

無需更新（所有檔案皆為 pipeline 專用，不引用共用知識檔）。

---

## 三、Bundle 結構（Phase 0 後修訂版）

掃描發現小文撰寫者有獨立的文章類型規格，seo-major-revision 有 SEO 策略知識，因此新增子目錄：

```
20260623-daypets-okf/
├── index.md
├── log.md
│
├── brand/
│   ├── index.md
│   ├── brand-positioning.md          ← welly-seo-writer/clients/daypets/brand.md
│   ├── tone-and-manner.md            ← welly-seo-writer/clients/daypets/tone-and-manner.md
│   ├── cta-template.md               ← welly-seo-writer/clients/daypets/cta-template.md
│   └── article-types/                ★ 新增
│       ├── index.md
│       ├── type-kouBei.md            ← 小文撰寫者
│       ├── type-touGao.md            ← 小文撰寫者
│       ├── type-waiLian.md           ← 小文撰寫者
│       ├── sample-kouBei.md          ← 小文撰寫者
│       └── sample-touGao.md          ← 小文撰寫者
│
├── editorial/
│   ├── index.md
│   ├── punctuation-rules.md          ← welly-seo-writer（全資料夾相同）
│   ├── writing-rules.md              ← welly-seo-writer（最完整版）
│   ├── quality-standards.md          ← ⚠️ 需合併三版本
│   ├── richness-principles.md        ← welly-seo-writer（全資料夾相同）
│   ├── structure-rules.md            ← welly-seo-writer（全資料夾相同）
│   └── structure-examples.md         ← welly-seo-writer（較新版）
│
├── articles/
│   ├── index.md
│   ├── content-library.md            ← welly-seo-writer/clients/daypets/content-library.md
│   ├── dog/
│   │   └── index.md
│   └── cat/
│       └── index.md
│
├── categories/
│   └── index.md
│
├── seo/
│   ├── index.md
│   ├── keyword-clusters/
│   │   ├── index.md
│   │   └── strategy-spec.md          ← 毛健康關鍵字策略/spec.md ★ 新增
│   ├── eeat-checklist.md             ← seo-major-revision ★ 新增
│   ├── google-algo-signals.md        ← seo-major-revision ★ 新增
│   ├── lagging-analysis-framework.md ← seo-major-revision ★ 新增
│   ├── internal-linking.md
│   ├── pillar-pages.md
│   └── content-gaps.md
│
└── references/
    ├── index.md
    ├── veterinary-sources.md
    └── nutrition-guidelines.md
```

---

## 四、待你決定的事項

1. **quality-standards.md 版本合併**：建議合併 welly 的「事實查證」段落 + 小文的「段落長度規範」→ 產出最完整版。OK？

2. **brand-voice.md 處理方式**：
   - **方案 A**（推薦）：保留 `brand-positioning.md` + `tone-and-manner.md` 作為基礎，另建 `brand/brand-voice-revision-addendum.md` 收錄 seo-major-revision 擴充的 30+ 條規則（AI 詞黑名單、必修改模式等）。好處：保持原始品牌檔的簡潔性。
   - **方案 B**：以 brand-voice.md 合併取代 brand.md + tone-and-manner.md 成為單一檔案。好處：減少檔案數。

3. **小文撰寫者的 article-types**：這些是小文專屬的文章規格（口碑/投稿/外鏈），搬入 bundle 後其他 SKILL 也能引用。確認放在 `brand/article-types/` 還是另建 `articles/types/`？

4. **推薦文 memory.md**：裡面含 18 篇競品分析和 references 摘要彙整，有部分品牌知識價值。要搬入 bundle 的某個位置，還是視為專案狀態不搬？

請 review 後告訴我決定，我就開始 Phase 1。
