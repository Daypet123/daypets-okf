---
type: Article Library
title: 文章庫元資訊
description: 文章庫 CSV 來源、快取策略、內鏈規則
tags: [articles, content-library, internal-linking, daypets]
timestamp: 2026-06-23T00:00:00Z
---

# 早安毛健康 · 文章庫

> 來源：`早安毛健康的專屬規範.docx`（§ 文章庫）
> 用途：
> 1. 03-writer 撰文時埋字內鏈：正文提及某主題且文章庫有對應文章，必須內鏈
> 2. 03-writer 撰寫文末 CTA：從文章庫挑 3 個延伸主題加超連結

## 來源 CSV

```
https://docs.google.com/spreadsheets/d/14rrBVJru15OjNa41Slkvt8f_Ia3hJJ6JPrazvsjcgWo/export?format=csv&gid=0
```

## 快取檔

- 路徑：`clients/daypets/content-library.csv`
- **快取 + 手動 refresh 策略**：orchestrator 啟動時問使用者要不要 refresh，預設否
- 第一次使用前需先手動拉一份到上述路徑

## 內鏈規則

- 正文提及某主題且文章庫有對應文章 → **必須內鏈**
- 優先埋字內鏈，同一內鏈全文只連 1 次
- 不輸出 `[INTERNAL-LINK: ...]` 佔位符；正文引用處直接嵌入超連結
- 超連結顏色：`#1155cc`

## Refresh 腳本（預留）

```bash
# 預計放 scripts/refresh-daypets-library.sh
curl -L -o clients/daypets/content-library.csv \
  "https://docs.google.com/spreadsheets/d/14rrBVJru15OjNa41Slkvt8f_Ia3hJJ6JPrazvsjcgWo/export?format=csv&gid=0"
```