# 早安毛健康 OKF Knowledge Bundle

[早安毛健康（DayPets）](https://daypets.tw) 的寵物健康知識庫，採用 [Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md) v0.1 格式。

## 這是什麼？

一份結構化、機器可讀的寵物健康知識庫 — 涵蓋 166 篇文章、14 個主題分類、1,118 條交叉連結。設計給 AI agent、搜尋系統與知識目錄使用。

## 目錄結構

```
├── about/          # 網站介紹與編輯標準
├── topics/         # 14 個主題分類（貓品種、狗健康⋯）
├── articles/       # 166 篇文章 concept（含 URL 與交叉連結）
└── references/     # 獸醫學與營養學權威來源
```

## 快速開始

每個 `.md` 檔案都是獨立的 concept，帶有 YAML frontmatter：

```yaml
---
type: Article
title: "布偶貓好養嗎？布偶貓優缺點、飼主心得與價格行情"
resource: https://daypets.tw/blog/ragdoll-guide
tags: [貓咪品種, 布偶貓]
---
```

從 [`index.md`](index.md) 開始瀏覽完整知識結構。

## OKF 合規性

- ✅ 185 個 concept 檔案皆有合法 YAML frontmatter 與 `type` 欄位
- ✅ 1,118 條內部交叉連結全數有效
- ✅ 符合 [OKF v0.1 規格](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)

## 授權

內容 © 2026 早安毛健康（DayPets）。保留所有權利。
知識結構與 metadata 採用 [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) 授權。
