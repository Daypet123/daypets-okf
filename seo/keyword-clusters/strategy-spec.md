---
type: Keyword Strategy
title: 關鍵字策略方法論
description: 6 階段 SEO 關鍵字分析流程：資料收集、分類評分、SERP 分群、品質門檻、擴展、產出
tags: [seo, keywords, strategy, methodology]
timestamp: 2026-06-23T00:00:00Z
---

# 關鍵字策略分析 Skill — 規格文件 (spec.md)

> 版本：v1.1 | 建立日期：2026-05-27 | 更新日期：2026-06-15

---

## 1. 概述

本 Skill 接收一批關鍵字（每次 20–50 個，總量約 200 個），透過 Ahrefs MCP 與 SerpAPI 取得 SERP 資料，依序執行六步分析，最終輸出格式化的 Excel (.xlsx) 報表。

---

## 2. 資料來源與 API 使用

### 2.1 Ahrefs MCP（主要資料源）

| 工具名稱 | 用途 | 回傳欄位 |
|---|---|---|
| `serp-overview` | 取得 SERP 前 10 筆有機結果 | DR, refdomains, page_type, URL, title, traffic |
| `keywords-explorer-overview` | 取得關鍵字搜尋量與流量潛力 | volume, traffic_potential |
| `keywords-explorer-related-terms` | 擴展相關關鍵字 | 相關關鍵字列表與搜尋量 |
| `keywords-explorer-matching-terms` | 發現長尾關鍵字 | 匹配關鍵字列表與搜尋量 |

- **國家參數**：一律使用 `country=tw`（台灣）
- **API 消耗預估**：每個關鍵字約 200 units，200 個關鍵字 ≈ 40,000 units

### 2.2 SerpAPI（補充資料源）

- **端點**：`https://serpapi.com/search.json`
- **呼叫方式**：bash curl
- **用途**：取得 PAA（People Also Ask / related_questions）與相關搜尋（related_searches）
- **參數**：`engine=google`, `gl=tw`, `hl=zh-TW`

---

## 3. 六步分析流程

### Phase 0：初始化
- 接收關鍵字清單
- 驗證輸入格式

### Phase 1：資料收集
- 對每個關鍵字呼叫 Ahrefs `serp-overview`（取得 SERP 有機結果）
- 對每個關鍵字呼叫 Ahrefs `keywords-explorer-overview`（取得搜尋量）
- 對每個關鍵字呼叫 SerpAPI（取得 PAA 和相關搜尋）

### Phase 2：分類與評分

#### 3.1 信心度評分（Confidence Scoring）

根據 SERP 前 10 筆有機結果的 DR 和 refdomains 進行評分：

| 條件 | 信心度 |
|---|---|
| DR < 20 的結果 ≥ 2 個 | **信心度極高** |
| DR < 20 的結果 1–2 個 **且** refdomains < 10 的結果 > 5 個 | **信心度高** |
| DR < 20 的結果 = 0 個 **且** refdomains < 10 的結果 > 5 個 | **信心度中** |
| DR < 20 的結果 = 0 個 **且** refdomains < 10 的結果 ≤ 5 個 | **信心度低** |

- **DR**：Domain Rating，從 Ahrefs serp-overview 的有機結果取得
- **refdomains**：Referring Domains（反向連結的獨立網域數），從 Ahrefs serp-overview 的有機結果取得

#### 3.2 文章類型判讀（Article Type Classification）

根據 SERP 有機結果的 URL 路徑、標題關鍵字、Ahrefs `page_type` 欄位進行啟發式分類。

**四種文章類型**：

| 類型 | 說明 |
|---|---|
| 一般文章頁 | 知識型、教學型內容（如：/blog/, /article/, /knowledge/） |
| 推薦文章頁 | 比較、推薦、排行類內容（如：標題含「推薦」「比較」「排行」「TOP」） |
| 產品頁 | 電商產品詳情頁（如：/product/, /item/, /shop/） |
| 產品介紹文章頁 | 以文章形式介紹單一產品（混合型） |

**分類優先順序**：URL 路徑 > 標題關鍵字 > Ahrefs page_type

> ⚠️ 注意：Ahrefs `page_type` 經常為 null，不能單獨依賴。以 URL 路徑模式為首要判斷依據。

**排除規則**：以下類型的結果在分類時排除：
- 社群 / UGC 頁面（PTT、Dcard、Facebook、Instagram、Threads、Reddit、YouTube、TikTok、LINE 社群等）
- 百科頁面（維基百科、百度百科等）

**文章類型判讀規則**（基於排除後的有機結果）：

| 狀況 | 判讀方式 | 輸出說明範例 |
|---|---|---|
| 狀況1：⅔ 以上為同一類型 | 以該類型操作 | 「SERP 結果以『一般文章頁』為主（佔 70%），建議以一般文章頁操作」 |
| 狀況2：兩種類型各佔約半 | 優先選文章類（一般/推薦）；若一般 vs 推薦各半 → SEO 顧問判斷 | 「『產品頁』與『一般文章頁』各佔約半，優先選擇『一般文章頁』操作」 |
| 狀況3：三種以上比例相近 | 比照狀況2邏輯 | 「三種類型比例相近，建議優先以『一般文章頁』操作，需 SEO 顧問進一步判斷」 |

> ⚠️ 判讀說明必須是完整的中文描述，不可只寫「狀況2」之類的代號。

#### 3.3 權威網站計數（Authority Site Counting）

統計 SERP 有機結果中以下類型網站的**出現次數**（非去重）：
- 政府網站（.gov.tw）
- 組織網站（.org, .org.tw）
- 教育網站（.edu, .edu.tw）

### Phase 3：SERP 意圖分群（Intent Grouping）

#### 3.4 SERP 搜尋意圖重疊度

**URL Key 提取方式**：`domain + 第一層路徑`（精確 URL 路徑比對）

> ⚠️ **重要**：必須用精確 URL（domain + 第一層路徑）比對，**不可用 domain-level 比對**。Domain-level 會嚴重高估重疊度（例如將同一網站的不同文章都算成重疊）。實測案例：緬因貓壽命 vs 緬因貓，domain-level 高估為 ~40-50%，URL-level 實際僅 ~23%。

**比較邏輯**：
1. 取每個關鍵字的 SERP 有機結果 URL 列表（排除社群/UGC/百科）
2. 兩兩比對 URL Key 的交集比例（精確 URL 路徑，非 domain）
3. 重疊度 ≥ 40% → 判定為相同搜尋意圖，可在同一篇文章操作

**分群規則**：
- 同一意圖群組中，搜尋量最高者 = **核心關鍵字**
- 其餘 = **長尾關鍵字**
- 與任何其他關鍵字重疊度均 < 40% = **獨立關鍵字**

### Phase 3.5：品質閘門（Quality Gates）

> v1.1 新增（2026-06-15）

在推薦關鍵字之前，需通過以下品質檢查：

#### 3.4a 電商 / 品牌導航 SERP 意圖排除

檢查每個候選關鍵字的 SERP 有機結果，識別以下問題意圖：

| 問題類型 | 判斷依據 | 處理方式 |
|---|---|---|
| 品牌導航意圖 | SERP 前 10 中 ≥ 5 筆來自同一品牌官網或其子網域 | 標記為「品牌導航」，建議排除 |
| 電商購買意圖 | SERP 前 10 中 ≥ 5 筆為電商平台（momo、PChome、蝦皮、Amazon 等）或產品頁 | 標記為「電商意圖」，建議排除 |
| 混合意圖 | 品牌官網 + 電商通路合計佔 SERP ≥ 60% | 標記為「品牌導航+電商混合」，建議排除 |

**典型案例**：「一錠除」（NexGard）— SERP 被品牌官網和電商通路佔據，不適合資訊型 SEO 文章。

> ⚠️ 此檢查在 Phase 2 完成後、最終推薦前執行。未通過的關鍵字需尋找替補。

#### 3.4b Cluster 長尾字 SERP 驗證

推薦 cluster 長尾字時，必須驗證其與 pillar 核心字的 SERP 重疊度 < 40%。重疊度 ≥ 40% 表示搜尋意圖相同，cluster 文章會與 pillar 文章互相競爭排名。

#### 3.4c 聚合/Hub 頁面策略

搜尋量高的聚合型關鍵字（如「狗狗品種」「貓品種」）可作為 pillar page，透過內部連結串接到個別品種文章。判斷依據：
- SERP 前 10 中出現大量清單型 / 聚合型頁面
- 關鍵字的 traffic_potential 明顯高於 volume（表示有大量子話題流量）
- 網站已有多篇相關子話題文章可供內部連結

### Phase 4：關鍵字擴展

#### 3.5 對稱 / 母關鍵字發現

針對輸入關鍵字，透過 Ahrefs `keywords-explorer-matching-terms` 搜尋是否存在：
- 母關鍵字（更廣泛的上層詞）
- 對稱關鍵字（同義或近義的替代詞）

#### 3.6 相關關鍵字擴展

透過 Ahrefs `keywords-explorer-related-terms` 取得語義相關的延伸關鍵字及搜尋量。

### Phase 5：輸出

產出格式化的 Excel 檔案（詳見第 4 節）。

---

## 4. 輸出格式規格

### 4.1 Excel 檔案結構

檔案格式：`.xlsx`（使用 openpyxl 產生）

**Sheet 1：關鍵字分析**

| 欄位 | 說明 |
|---|---|
| 關鍵字 | 輸入的關鍵字 |
| 搜尋量 | 月均搜尋量（Ahrefs） |
| 流量潛力 | Traffic Potential（Ahrefs） |
| 信心度 | 極高 / 高 / 中 / 低 |
| DR<20 數量 | SERP 中 DR<20 的結果數 |
| Refdomains<10 數量 | SERP 中 refdomains<10 的結果數 |
| 文章類型判讀 | 完整中文描述（非代號） |
| 權威網站 | gov/org/edu 出現次數 |
| PAA | People Also Ask（換行分隔） |
| 相關搜尋 | Related Searches（換行分隔） |

**Sheet 2：SERP 意圖分群**

| 欄位 | 說明 |
|---|---|
| 意圖群組 | 群組編號 |
| 關鍵字 | 關鍵字名稱 |
| 搜尋量 | 月均搜尋量 |
| 角色 | 核心關鍵字 / 長尾關鍵字 / 獨立關鍵字 |

### 4.2 格式要求

- **粗邊框分群**：同一意圖群組的列用 medium 粗邊框圍起來（openpyxl Border side style='medium'）
- **顏色標記**：
  - 核心關鍵字：淺藍底色
  - 長尾關鍵字：淺綠底色
  - 獨立關鍵字：淺灰底色
- **群組內排序**：核心關鍵字在最上方，長尾依搜尋量降序排列
- **多值欄位換行**：PAA 和相關搜尋欄位中，不同關鍵字以換行 (`\n`) 分隔，儲存格設定 `wrap_text=True`
- **表頭語言**：全部使用繁體中文
- **不包含**：Keyword Difficulty 欄位

### 4.3 展示格式

採用**扁平式分群列表**（非 A vs B 配對矩陣）：
- 關鍵字垂直列出
- 以意圖群組分段
- 核心關鍵字在群組最上方
- 用粗邊框區隔不同群組

---

## 5. 工作流程架構

```
Phase 0: 初始化
    ↓ 接收關鍵字清單
Phase 1: 資料收集
    ↓ Ahrefs serp-overview + keywords-explorer-overview + SerpAPI
    ↓ （中文關鍵字 overview 回空時 fallback 到 matching-terms）
Phase 2: 分類與評分
    ↓ 信心度 + 文章類型 + 權威網站
Phase 3: 意圖分群
    ↓ SERP 重疊度比對（URL-level）→ 核心/長尾/獨立
Phase 3.5: 品質閘門 ← v1.1 新增
    ↓ 電商/品牌意圖排除 + Cluster SERP 驗證 + Hub 頁面判斷
Phase 4: 關鍵字擴展
    ↓ 對稱/母關鍵字 + 相關關鍵字
Phase 5: 輸出
    ↓ 產生 Excel 檔案
```

---

## 6. 已知限制與注意事項

1. **Ahrefs page_type 經常為 null**：文章類型分類需以 URL 路徑為主要判據
2. **ipetgroup.com 誤判問題**：`/article/` 路徑應優先判定為文章頁，即使標題含有購買相關詞彙
3. **API 呼叫量大**：建議每次跑 20–50 個關鍵字，避免一次消耗過多 API quota
4. **沙盒檔案刪除限制**：掛載資料夾中的舊檔案需使用者手動刪除
5. **Ahrefs keywords-explorer-overview 對中文關鍵字常回空**（v1.1 新增）：查詢中文關鍵字時經常回傳 `{ "keywords": [] }`。替代方案：改用 `keywords-explorer-matching-terms`，使用 `keywords` 參數（JSON array 格式 `["term"]`，注意是複數 `keywords` 不是單數 `keyword`）
6. **Ahrefs word_count filter 不支援中文**（v1.1 新增）：中文字不被 Ahrefs 斷詞計數，`word_count` filter 無法有效篩選中文關鍵字長度
7. **SERP 重疊度必須用 URL-level 比對**（v1.1 釐清）：domain-level 比對會嚴重高估重疊度，務必使用 domain + 第一層路徑的精確比對
8. **部分 SERP position 資料品質差**（v1.1 新增）：某些混合 SERP features 的關鍵字（如黑色柴犬）會回傳所有結果 position=1，需過濾 organic position 2-10
9. **Ahrefs filter 語法**（v1.1 備註）：JSON 格式，例如 `{"and":[{"field":"difficulty","is":["eq",0]},{"field":"volume","is":["gte",1000]}]}`