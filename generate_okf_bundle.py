import csv
import os
import re
from datetime import datetime
from collections import defaultdict

# --- Config ---
BUNDLE_DIR = "/sessions/nifty-exciting-ride/mnt/outputs/20260623-daypets-okf"
CSV_PATH = "/sessions/nifty-exciting-ride/mnt/.claude/skills/welly-seo-writer/clients/daypets/content-library.csv"
NOW = "2026-06-23T00:00:00+08:00"

# --- Category mapping ---
CATEGORY_MAP = {
    "cat-breeds": {
        "title": "貓咪品種",
        "description": "各種貓咪品種的完整介紹，包含特徵、個性、價格與飼養建議。",
        "keywords": ["布偶貓","緬因貓","英國短毛貓","俄羅斯藍貓","美國短毛貓","暹羅貓","虎斑貓",
                     "豹貓","米克斯貓","賓士貓","曼赤肯","挪威森林貓","波斯貓","無毛貓","摺耳貓",
                     "玳瑁貓","麒麟尾","阿比西尼亞貓","埃及貓","緬甸貓","德文捲毛貓","西伯利亞貓",
                     "喜馬拉雅貓","伯曼貓"]
    },
    "dog-breeds": {
        "title": "狗狗品種",
        "description": "熱門犬種的深度介紹，涵蓋個性、智商、價格與飼養重點。",
        "keywords": ["邊境牧羊犬","比熊","馬爾濟斯","西高地白梗","貴賓狗","薩摩耶","狐狸犬",
                     "哈士奇","伯恩山犬","柴犬","秋田犬","豆柴","米格魯","臘腸狗","黃金獵犬",
                     "拉布拉多","法鬥","杜賓犬","傑克羅素","柯基","德國牧羊犬","博美","雪納瑞",
                     "可卡犬","鬆獅犬","西施犬","沙皮狗","惡霸犬","比特犬","米克斯狗","台灣土狗",
                     "大丹犬","大麥町","迷你杜賓","大白熊","棉花面紗犬","藏獒","羅威納","聖伯納犬",
                     "古代牧羊犬","巴哥","喜樂蒂","蝴蝶犬","阿富汗獵犬","剛毛獵狐㹴","英國鬥牛犬",
                     "阿拉斯加犬"]
    },
    "cat-health": {
        "title": "貓咪健康",
        "description": "貓咪常見疾病的症狀辨識、治療方式與預防照護指南。",
        "keywords": ["貓蘚","貓血尿","貓癌症","貓愛滋","貓拉肚子","腎貓","貓腹膜炎","貓口炎",
                     "貓吐","貓粉刺","貓打噴嚏","貓的壽命","貓毛過敏"]
    },
    "dog-health": {
        "title": "狗狗健康",
        "description": "狗狗常見疾病與健康問題的完整照護指南。",
        "keywords": ["狗狗心臟病","狗狗皮膚病","狗狗濕疹","狗狗前庭症候群","狗皮膚黴菌",
                     "狗狗退化性關節炎","狗狗吐","狗狗拉肚子","狗狗身上的蟲","老狗臨終前症狀"]
    },
    "cat-care": {
        "title": "貓咪照護",
        "description": "日常貓咪照護技巧，包含清潔、結紮、環境管理等實用指南。",
        "keywords": ["貓洗澡","貓剪指甲","貓砂多久換一次","公貓結紮","母貓結紮","養貓須知",
                     "養貓一個月花費","新舊貓磨合要多久","母貓會照顧小貓到什麼時候","貓年齡換算"]
    },
    "dog-care": {
        "title": "狗狗照護",
        "description": "狗狗日常照護知識，從洗澡、遛狗到幼犬飼養的實用教學。",
        "keywords": ["狗狗洗澡","遛狗","小狗","狗年齡換算","肛門腺"]
    },
    "cat-nutrition": {
        "title": "貓咪飲食",
        "description": "貓咪飲食安全與營養指南，包含飼料推薦與食物禁忌。",
        "keywords": ["貓可以喝牛奶嗎","貓吃魚","貓草","貓薄荷","木天蓼","貓飼料推薦"]
    },
    "dog-nutrition": {
        "title": "狗狗飲食",
        "description": "狗狗飲食安全指南，收錄禁忌食物清單與飼料推薦。",
        "keywords": ["狗不能吃什麼","狗狗不能吃的水果","狗吃巧克力","狗飼料推薦"]
    },
    "cat-behavior": {
        "title": "貓咪行為",
        "description": "解讀貓咪行為語言與叫聲含義，幫助飼主理解毛孩。",
        "keywords": ["貓一直凹嗚","幼貓一直叫","貓叫聲","貓抓老鼠","貓舌頭","貓怕什麼味道"]
    },
    "dog-behavior": {
        "title": "狗狗行為",
        "description": "解讀狗狗肢體語言、叫聲與行為背後的含義。",
        "keywords": ["狗尾巴","狗狗一直嚶嚶叫","狗叫聲","最聰明的狗"]
    },
    "small-pets": {
        "title": "小型寵物",
        "description": "兔子、倉鼠、天竺鼠等小型寵物的飼養指南與照護知識。",
        "keywords": ["蜜袋鼯","天竺鼠","無毛天竺鼠","龍貓","倉鼠","狐獴","浣熊","兔子",
                     "侏儒兔","安哥拉兔","獅子兔","睡鼠","老公公鼠","黃金鼠","麝香豬",
                     "垂耳兔","刺蝟","豪豬","寵物雞"]
    },
    "reptiles-aquatic": {
        "title": "爬蟲與水族",
        "description": "爬蟲類、水族與兩棲類寵物的品種介紹與飼養教學。",
        "keywords": ["巴西龜","斑龜","球蟒","玉米蛇","鬆獅蜥","豹紋守宮","肥尾守宮",
                     "蘇卡達象龜","鬥魚","孔雀魚","小丑魚","斑馬魚"]
    },
    "birds": {
        "title": "鳥類",
        "description": "鳥類寵物的品種特徵、飼養方式與照護重點。",
        "keywords": ["玄鳳鸚鵡","貓頭鷹"]
    },
    "special-topics": {
        "title": "特殊主題",
        "description": "寵物節日、跨物種知識與其他特殊主題文章。",
        "keywords": ["弓漿蟲","國際小狗日","國際狗狗日"]
    }
}

def slugify(text):
    """Create a URL-friendly slug from Chinese text by using the URL path."""
    return text.strip()

def get_category(keyword):
    """Map a keyword to its category."""
    for cat_id, cat_info in CATEGORY_MAP.items():
        if keyword in cat_info["keywords"]:
            return cat_id
    return "other"

def extract_slug_from_url(url):
    """Extract the slug from a daypets.tw URL."""
    if not url or "daypets.tw/blog/" not in url:
        return None
    parts = url.rstrip("/").split("/")
    return parts[-1] if parts[-1] else None

def write_file(path, content):
    """Write content to a file, creating directories as needed."""
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

# --- Parse CSV ---
articles = []
with open(CSV_PATH, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        keyword = row.get("核心關鍵字", "").strip()
        title = row.get("文章名稱", "").strip()
        url = row.get("上架url（公式往下拉自動組合）", "").strip()
        date = row.get("上架日期", "").strip()
        
        if not keyword or not title or not url or url == "https://daypets.tw/blog/":
            continue
        
        slug = extract_slug_from_url(url)
        if not slug:
            continue
            
        category = get_category(keyword)
        
        # Parse date
        timestamp = NOW
        if date:
            try:
                parts = date.split("/")
                if len(parts) == 3:
                    timestamp = f"{parts[0]}-{int(parts[1]):02d}-{int(parts[2]):02d}T00:00:00+08:00"
            except:
                pass
        
        articles.append({
            "keyword": keyword,
            "title": title,
            "url": url,
            "slug": slug,
            "category": category,
            "timestamp": timestamp
        })

print(f"Parsed {len(articles)} articles")

# --- Group by category ---
by_category = defaultdict(list)
for a in articles:
    by_category[a["category"]].append(a)

for cat, arts in sorted(by_category.items()):
    print(f"  {cat}: {len(arts)} articles")

# --- Generate bundle ---

# 1. Root index.md
root_index = """# 早安毛健康（DayPets）知識庫

* [about](/about/) - 關於早安毛健康：品牌定位、編輯方針與內容標準
* [topics](/topics/) - 內容主題分類：貓咪、狗狗、小型寵物、爬蟲水族等知識領域
* [articles](/articles/) - 完整文章庫：所有已發布的寵物知識文章索引
* [references](/references/) - 參考來源：內容引用的權威獸醫學與營養學資源
"""
write_file(f"{BUNDLE_DIR}/index.md", root_index)

# 2. about/
write_file(f"{BUNDLE_DIR}/about/index.md", """# 關於早安毛健康

* [site-overview](/about/site-overview.md) - 早安毛健康的品牌定位與使命
* [editorial-standards](/about/editorial-standards.md) - 內容製作流程與品質標準
""")

write_file(f"{BUNDLE_DIR}/about/site-overview.md", """---
type: About
title: 早安毛健康（DayPets）
description: 台灣寵物健康知識媒體，用易懂的語言傳遞專業寵物照護知識。
resource: https://daypets.tw
tags: [品牌, 寵物健康, 台灣]
timestamp: 2026-06-23T00:00:00+08:00
---

# 早安毛健康

早安毛健康（DayPets）是台灣的寵物健康知識媒體平台，專注於將專業的寵物照護知識轉化為一般飼主能輕鬆理解的內容。

## 核心使命

為 25-45 歲的台灣飼主（準飼主與現任飼主）提供可信賴的寵物健康資訊，涵蓋品種介紹、疾病照護、營養飲食、行為解讀等面向。

## 內容範疇

- **貓咪**：品種指南、健康照護、飲食營養、行為解讀
- **狗狗**：品種指南、健康照護、飲食營養、行為解讀
- **小型寵物**：兔子、倉鼠、天竺鼠等小動物飼養知識
- **爬蟲與水族**：烏龜、蛇類、守宮、觀賞魚等飼養教學
- **鳥類**：鸚鵡等鳥類寵物照護

## 網站資訊

- 網域：[daypets.tw](https://daypets.tw)
- 語言：繁體中文（台灣）
- 定位：知識媒體，非電商平台
""")

write_file(f"{BUNDLE_DIR}/about/editorial-standards.md", """---
type: Editorial Policy
title: 編輯方針與品質標準
description: 早安毛健康的內容製作流程、事實查核與品質管理標準。
tags: [編輯, 品質, E-E-A-T]
timestamp: 2026-06-23T00:00:00+08:00
---

# 編輯方針與品質標準

## 內容製作流程

早安毛健康的每篇文章經過系統化的製作流程：

1. **主題研究**：分析搜尋意圖、競品內容與讀者需求
2. **架構規劃**：依據研究結果設計文章結構與涵蓋面向
3. **專業撰寫**：基於獸醫學文獻與權威來源撰寫內容
4. **品質審核**：事實查核、數據驗證與可讀性檢查
5. **持續更新**：定期檢視並更新過時資訊

## 引用標準

- 優先引用獸醫學教科書、期刊論文與官方機構資料
- 疾病相關內容參考 WSAVA、AAHA 等國際獸醫組織指引
- 營養相關內容參考 AAFCO、NRC 等標準
- 所有統計數據與醫學聲明須有可追溯的來源

## 內容原則

- 以科學證據為基礎，避免未經驗證的偏方或謠言
- 明確區分「已有共識的知識」與「仍有爭議的觀點」
- 涉及疾病症狀時，建議飼主諮詢專業獸醫
""")

# 3. topics/
topics_index_items = []
for cat_id, cat_info in sorted(CATEGORY_MAP.items()):
    count = len(by_category.get(cat_id, []))
    topics_index_items.append(f"* [{cat_info['title']}](/topics/{cat_id}.md) - {cat_info['description']}（{count} 篇文章）")

write_file(f"{BUNDLE_DIR}/topics/index.md", "# 內容主題分類\n\n" + "\n".join(topics_index_items) + "\n")

for cat_id, cat_info in CATEGORY_MAP.items():
    cat_articles = by_category.get(cat_id, [])
    article_links = "\n".join([
        f"- [{a['title']}](/articles/{cat_id}/{a['slug']}.md)" 
        for a in sorted(cat_articles, key=lambda x: x['keyword'])
    ])
    
    # Determine parent topic tags
    if cat_id.startswith("cat-"):
        parent_tag = "貓咪"
    elif cat_id.startswith("dog-"):
        parent_tag = "狗狗"
    elif cat_id in ["small-pets"]:
        parent_tag = "小型寵物"
    elif cat_id in ["reptiles-aquatic"]:
        parent_tag = "爬蟲水族"
    elif cat_id == "birds":
        parent_tag = "鳥類"
    else:
        parent_tag = "特殊主題"
    
    content = f"""---
type: Topic
title: {cat_info['title']}
description: {cat_info['description']}
resource: https://daypets.tw
tags: [{parent_tag}, {cat_info['title']}]
timestamp: {NOW}
---

# {cat_info['title']}

{cat_info['description']}

## 收錄文章（{len(cat_articles)} 篇）

{article_links}
"""
    write_file(f"{BUNDLE_DIR}/topics/{cat_id}.md", content)

# 4. articles/
articles_index_items = []
for cat_id in sorted(by_category.keys()):
    cat_info = CATEGORY_MAP.get(cat_id, {"title": "其他", "description": ""})
    count = len(by_category[cat_id])
    articles_index_items.append(f"* [{cat_info['title']}](/articles/{cat_id}/) - {count} 篇文章")

write_file(f"{BUNDLE_DIR}/articles/index.md", "# 文章庫\n\n" + "\n".join(articles_index_items) + "\n")

# Per-category article indexes and individual article files
for cat_id, cat_articles in by_category.items():
    cat_info = CATEGORY_MAP.get(cat_id, {"title": "其他", "description": ""})
    
    # Category index
    cat_index_items = []
    for a in sorted(cat_articles, key=lambda x: x['keyword']):
        cat_index_items.append(f"* [{a['title']}]({a['slug']}.md) - 核心關鍵字：{a['keyword']}")
    
    write_file(f"{BUNDLE_DIR}/articles/{cat_id}/index.md",
        f"# {cat_info['title']}文章\n\n" + "\n".join(cat_index_items) + "\n")
    
    # Individual article concepts
    for a in cat_articles:
        # Find related articles in same category
        related = [r for r in cat_articles if r['slug'] != a['slug']][:5]
        related_links = "\n".join([
            f"- [{r['title']}]({r['slug']}.md)" for r in related
        ]) if related else "（暫無）"
        
        # Cross-link to topic
        topic_link = f"[{cat_info['title']}](/topics/{cat_id}.md)"
        
        article_content = f"""---
type: Article
title: "{a['title']}"
description: 早安毛健康關於「{a['keyword']}」的完整指南。
resource: {a['url']}
tags: [{cat_info['title']}, {a['keyword']}]
timestamp: {a['timestamp']}
---

# {a['title']}

主題分類：{topic_link}

## 相關文章

{related_links}
"""
        write_file(f"{BUNDLE_DIR}/articles/{cat_id}/{a['slug']}.md", article_content)

# 5. references/
write_file(f"{BUNDLE_DIR}/references/index.md", """# 參考來源

* [editorial-methodology](/references/editorial-methodology.md) - 內容製作方法論與引用標準
* [veterinary-organizations](/references/veterinary-organizations.md) - 引用的國際獸醫學組織
* [nutrition-standards](/references/nutrition-standards.md) - 寵物營養學參考標準
""")

write_file(f"{BUNDLE_DIR}/references/editorial-methodology.md", """---
type: Reference
title: 內容製作方法論
description: 早安毛健康文章的研究、撰寫與品質管理方法論。
tags: [方法論, 品質管理]
timestamp: 2026-06-23T00:00:00+08:00
---

# 內容製作方法論

## 研究方法

每篇文章的製作始於系統化的研究流程：

1. **搜尋意圖分析**：分析目標關鍵字的搜尋者意圖與資訊需求
2. **文獻回顧**：查閱相關獸醫學文獻、教科書與官方指引
3. **競品分析**：評估現有中文內容的覆蓋面與不足之處
4. **專家諮詢**：必要時諮詢執業獸醫師確認醫學內容

## 品質標準

- 所有醫學聲明須有文獻支持
- 統計數據須標註來源
- 區分「已有共識」與「尚有爭議」的觀點
- 疾病相關內容一律建議諮詢獸醫

## 更新機制

- 定期檢視已發布文章的時效性
- 追蹤獸醫學領域新研究與新指引
- 讀者回饋驅動的內容修正
""")

write_file(f"{BUNDLE_DIR}/references/veterinary-organizations.md", """---
type: Reference
title: 國際獸醫學組織
description: 早安毛健康內容引用的權威獸醫學組織與機構。
tags: [獸醫學, 權威來源]
timestamp: 2026-06-23T00:00:00+08:00
---

# 國際獸醫學組織

早安毛健康的內容製作參考以下國際權威組織的指引與研究：

## 獸醫臨床

- **WSAVA**（World Small Animal Veterinary Association）— 小動物獸醫學全球指引
- **AAHA**（American Animal Hospital Association）— 美國動物醫院協會照護標準
- **ISFM**（International Society of Feline Medicine）— 國際貓科醫學會

## 寵物營養

- **AAFCO**（Association of American Feed Control Officials）— 美國飼料管理協會
- **NRC**（National Research Council）— 美國國家研究委員會動物營養標準
- **FEDIAF**（European Pet Food Industry Federation）— 歐洲寵物食品工業聯盟

## 疾病防治

- **ABCD**（European Advisory Board on Cat Diseases）— 歐洲貓科疾病顧問委員會
- **CAPC**（Companion Animal Parasite Council）— 伴侶動物寄生蟲委員會

## 台灣機構

- **農業部動物保護資訊網** — 台灣動物保護法規與資源
- **台灣獸醫內科醫學會** — 本地獸醫學術交流
""")

write_file(f"{BUNDLE_DIR}/references/nutrition-standards.md", """---
type: Reference
title: 寵物營養學標準
description: 早安毛健康飲食相關內容所依據的營養學標準與指引。
tags: [營養學, AAFCO, NRC]
timestamp: 2026-06-23T00:00:00+08:00
---

# 寵物營養學標準

## AAFCO 飼料標準

AAFCO（Association of American Feed Control Officials）制定的寵物食品營養標準是早安毛健康評估飼料品質的主要依據：

- 成犬/成貓維持期營養需求
- 幼犬/幼貓成長期營養需求
- 懷孕/哺乳期營養需求
- 原料定義與標示規範

## NRC 營養需求

NRC（National Research Council）發布的《犬貓營養需求》提供更細緻的科學數據，作為進階營養討論的參考。

## 引用原則

- 飼料推薦文章以 AAFCO 標準為基礎評估
- 特殊飲食需求（如腎病飲食）參考 WSAVA 營養指引
- 食物安全性資訊參考 ASPCA Animal Poison Control 資料庫
""")

# --- Summary ---
total_files = 0
for root, dirs, files in os.walk(BUNDLE_DIR):
    total_files += len(files)

print(f"\n=== Bundle generated ===")
print(f"Total files: {total_files}")
print(f"Total articles: {len(articles)}")
print(f"Categories: {len(by_category)}")
print(f"Bundle location: {BUNDLE_DIR}")
