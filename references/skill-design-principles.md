---
type: Reference
title: SKILL 設計原則
description: 三層分離架構（Persona-Config / Prompt-Skill / Script）、output 結構設計、token 節省策略
tags: [reference, skill-design, architecture, meta]
timestamp: 2026-06-23T00:00:00Z
---

# Skill / Prompt 設計原則

> 來源：`skills設計原則.docx`
> 用途：本 welly-seo-writer 專案所有 sub-agent、script、reference 的架構總綱。

## 架構三層分離

1. **Persona / Config（共用設定）**
   - 跨 prompt 複用的身份、偏好、規則，獨立成檔案
   - 各 prompt 用 reference 載入，不重複貼上

2. **Prompt = Skill（職責定義）**
   - 每個 prompt/skill 只負責一件事：觸發時機、核心目標（1-2 句）、輸入資料、輸出格式、執行步驟、要跑的 script
   - 不放 Q&A、不放冗長說明、不放重跑邏輯（統一放主控 SKILL.md）

3. **Script（可規範化的規則）**
   - 規則類、驗證類一律轉成 script
   - Prompt 只保留 AI 需要做語意判斷的指引
   - Script 不加註解、不寫 README

## 輸出結構設計原則

- 每個段落/章節有明確交付物
- 支援動態分支
- 規則用具體數字（「3-5 次」「≤ 2 處」「80-120 字」）

## Token 節省策略

- 同一條規則只存在一個地方
- Reference 只保留語意指引，可程式檢查的規則移到 script
- 每個 step 只載入該 step 的 references
- 共用資料用 JSON 供 script 讀取