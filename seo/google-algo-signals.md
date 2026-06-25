---
type: SEO Guide
title: Google 演算法信號指南
description: Helpful Content System、People-first 測試、內容透明度要求
tags: [seo, google-algorithm, helpful-content, search-signals]
timestamp: 2026-06-23T00:00:00Z
---

# Google 演算法訊號 · 大改檢核用

> 用途：分析既有文章時，用這份檔案對照 Google 排名系統的喜好與懲罰訊號。
> 來源：Google Search Central（Helpful Content System、Spam Policies 2024.03、Reviews System、Quality Rater Guidelines、Core Updates 2026.02 / 2026.03）。
> 設計：本檔聚焦「Google 為什麼會壓 / 拉這篇」的訊號；E-E-A-T 4 大支柱見 `eeat-checklist.md`。

## 一、底層認知（決定整篇文章命運）

### 1.1 Helpful Content System 是站點級分類器

- Helpful Content 自 2024 年 3 月已**整合進核心排名系統**，不再是獨立 update。
- 不是單篇判斷：Google 會對「整個網站」做 unhelpful 內容比例評估。
- 一個站若 unhelpful 比例高，會拉低站上**所有**文章——即使這篇本身寫得不錯。
- 大改的意義因此放大：每改好一篇，等於在拉高整站分母。
- 行動含義：如果這篇文章「不夠 helpful」，最好不只是改、是順便檢視同類型的其他舊文章。

### 1.2 People-first vs Search-first 判準（最關鍵兩問）

Google 自評題裡最關鍵的兩個：

1. **「拿掉這篇是否會讓搜尋體驗變差？」** 如果不會 → 文章本身屬 unhelpful。
2. **「讀者讀完後，是否覺得學到實際的東西？還是還要再 Google 一次？」**

大改時必問：這篇文章帶給讀者「實際可用的東西」是什麼？答不出來 → 文章有更深層問題，不只是改寫表達層面。

### 1.3 Who / How / Why（內容透明度）

Google QRG（Quality Rater Guidelines）特別重視：

- **Who 寫的**：作者 / 機構是否清楚？早安毛健康屬集體聲音「我們」，但站點層級必須清楚是誰在發聲。
- **How 寫的**：怎麼寫的？有沒有揭露使用 AI、有沒有說明研究方法？
- **Why 寫的**：為什麼寫？要服務讀者還是吸流量？

大改時若文章感覺像「不知道誰寫、寫來幹嘛」→ 標問題，建議補作者標示 / 編輯立場。

## 二、Google 特別獎勵的訊號（補了會加分）

| 訊號 | 大改時要怎麼補 |
|------|-------------|
| 第一手經驗（Experience） | 補「我們養過 / 我們爬文時發現 / 飼主在 PTT 反映」具體經驗描述 |
| 原創資訊 / 原創觀察 | 不只是 SERP 前 10 名重組；補一個獨家角度、彙整、對比 |
| 完整深度（Comprehensive） | 寫到「讀者不需要再搜下一個關鍵字」的完整度 |
| 清楚的作者 / 機構（Who） | 文末或 H1 下交代是誰寫的 / 編輯團隊背景 |
| 在地化（YMYL 額外加分） | 台灣飼主情境、台幣、台灣機構、台灣獸醫資源 |
| 結構化資料 / Schema | 文章類型對應的 schema markup（建議加在 Part 2 後台操作，但本 skill 不分 Part，會放在「其他」類） |

## 三、Google 嚴打的訊號（出現任一條 → 必標問題並建議大改）

### 3.1 Scaled Content Abuse 訊號（2024.03 政策後尤其敏感）

> Google 政策更新後，**用 AI 還是用人寫**已不是重點，重點是「為了排名而大量產出低值內容」。

- 段落結構高度公式化（每個 H2 都是「定義 → 原因 → 解決 → 結論」）
- 大量同義反覆、把同一句話用三種說法重述
- 內容厚但資訊密度低（讀完不知道學到什麼）
- 連續出現「綜觀整體 / 總結來說 / 由此可見」這類空洞收束句
- AI 排比句堆疊（不僅… 還… / 不只是… 而是… / 不僅…而且…）
- 每個 H3 結尾都用 3-4 個同格式 bullet 重述段落要點（目錄感）
- 過度修飾：「全方位 / 一站式 / 全面性 / 深度解析 / 完整指南」標題與段內反覆出現

### 3.2 Helpful Content 反訊號

- **寫給搜尋引擎不是寫給人**：關鍵字硬塞、為了 SEO 加長段落
- **摘要他人說法但沒加自己的觀點**：通篇都是 SERP 共識重組
- **錯估讀者程度**：搜「進階」需求卻寫基礎介紹，或反過來
- **字數膨脹**：用形容詞填、用客套話拖、用「眾所周知 / 大家都知道」開場
- **讀完讀者必須再搜一次**：給的資訊不夠完整、結論不明確
- **點擊誘餌標題**：「99% 飼主不知道」「震驚！」「必看！」

### 3.3 YMYL（寵物健康全屬此類）特別風險

> 寵物健康為 YMYL（Your Money / Your Life），Trust 標準特別嚴格。

- 醫療建議下得太重 / 太斷然（用「絕對 / 一定 / 必須」）
- 沒有「以獸醫診斷為準」這類免責提示
- 引用「研究指出」但沒有具體機構與年份
- 數據沒單位、沒年份、沒來源
- 用藥 / 劑量建議未經獸醫指示
- 把「品種傾向」寫成「個體必然」（例：「布偶貓一定很黏人」）
- 危險錯誤資訊：貓不能用犬類除蚤藥（permethrin 致命）、巧克力 / 葡萄 / 木糖醇對狗有毒等基礎事實寫錯

### 3.4 Reviews System 反訊號（介紹品種 / 推薦用品 / 比較類文章）

> Reviews System 評估「具備推薦 / 比較 / 評析意圖」的第一方原創內容。

- 只報優點不講缺點
- 沒有清楚的選擇標準
- 沒有實際使用 / 觀察 / 比較依據
- 「最好的 / 最推薦的 / Top 10」清單沒有評選邏輯
- 缺乏與替代選項的比較（用了 X 對比 Y 才好）
- 沒有作者本身的立場或結論

### 3.5 Site Reputation Abuse（站點層級警示）

如果早安毛健康站上有一些「外包寫稿」或「明顯非團隊聲音」的內容夾雜其中 → 整站可能被判 site reputation abuse。建議大改時順手檢查：

- 文章是否與站點主題（寵物健康）一致？
- 是否有明顯偏題的內容（旅遊、3C、人物八卦）混入？
- 各文章作者聲音是否一致？

不一致 → 在自審紀錄中標「站點層級風險」提醒主管。

## 四、檢核行動（大改建議產出時的具體做法）

讀完文章後對 Google 演算法層的問題列出指令時，**務必落到具體做法**——不要寫空話：

| 問題 | 不要寫 | 要寫 |
|------|------|------|
| Helpful Content 不足 | 「補強 helpful content」 | 「H2 第 X 段補一個『我們爬文』案例，並對比 PTT 飼主常反應的情境」 |
| 沒原創觀點 | 「加原創角度」 | 「在 H2 後段補一段早安毛的觀察 / 對比 / 立場（指定對比的兩件事）」 |
| AI 感過重 | 「降低 AI 感」 | 點出具體段落，給「改前 / 改後」對照（範例參 brand-voice.md § 3） |
| 缺第一手經驗 | 「補實際經驗」 | 指定「在開場 / 結語段插入 1-2 句『我們…』」具體位置 |
| 沒在地化 | 「加在地化內容」 | 「把第 X 段的舉例改為台灣情境（價格改台幣、品牌指定 XX、平台指定 PTT/Dcard）」 |
| 缺 Trust 訊號 | 「補 E-E-A-T」 | 「文末補一段免責；H2 第 X 段補引用 VCA / Cornell（指定具體機構）」 |
| Reviews System 缺優劣 | 「平衡優劣」 | 「H3『XX 品種優點』後新增 H3『XX 品種需要注意的地方』，包含 N 個具體面向」 |

## 五、Core Update 失分文章的常見診斷

Core Update 後流量掉的文章，常見原因排序：

1. **內容深度不夠** → 補完整度（不是補字數）
2. **沒有明確的人格 / 觀點** → 補編輯第一人稱、補早安毛的立場
3. **過度依賴 SERP 共識** → 補原創角度、對比
4. **YMYL 信任訊號弱** → 補來源、補免責、補機制
5. **整站 unhelpful 比例高** → 大改個別文章 + 提醒主管做整站盤點

不應該做的事：
- 只改標題 / meta description 不改內文 → Core Update 看的是內容本身
- 加幾段 AI 生成內容試圖填厚 → 反而踩 scaled content abuse
- 把所有舊文章一次大量重新生成 → 同樣是 scaled content abuse
- 把不夠好的段落「合併」進其他段落想藏起來 → Google 看的是整體結構

## 六、最新動態追蹤（建議季度更新本檔）

可能需要追蹤的官方資訊源（這份檔案的更新依據）：

- [Google Search Central Blog](https://developers.google.com/search/blog?hl=zh-tw) — 政策與系統更新公告
- [Google Search Status Dashboard](https://status.search.google.com/products/rGHU1u87FJnkP6W2GwMi/history?hl=zh-cn) — Ranking Update 推出與完成日期
- [Search Central Updates](https://developers.google.com/search/updates) — Documentation 更新記錄
- [Quality Rater Guidelines（PDF）](https://services.google.com/fh/files/misc/hsw-sqrg.pdf) — 評分員手冊（最具體的判準來源）

每次 Google 釋出新 Core Update 或政策時，更新本檔的 § 三（嚴打訊號）；早安毛若觀察到流量異常，回頭比對本檔是否漏列新訊號。

## 七、與 eeat-checklist.md 的分工

| 維度 | 在哪份檔 |
|------|---------|
| Experience / Expertise / Authoritativeness / Trust 4 大支柱 | eeat-checklist.md |
| 寵物健康 YMYL 紅線（醫療診斷、用藥、繁殖、疫苗） | eeat-checklist.md § 五 |
| Helpful Content 站點級訊號 | 本檔 § 一 |
| People-first vs Search-first 判準 | 本檔 § 一、§ 三 |
| Scaled Content / Spam Policy（2024.03） | 本檔 § 三.1 |
| Reviews System（評析類內容） | 本檔 § 三.4 |
| Core Update 應對策略 | 本檔 § 五 |
| Site Reputation Abuse | 本檔 § 三.5 |

**兩份檔同時讀**：eeat-checklist 是「內容支柱要補什麼」、本檔是「演算法在抓什麼」。同一條建議可能兩邊都觸發，但兩邊的視角不同——產出大改建議時，每條問題標出對應的 reference 編號（例：`eeat-checklist § 三 / google-algo § 三.1`）方便日後追溯。