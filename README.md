# GPT-4o Proxy Translator

## 這啥?

一個最小可行 Flask API Proxy，使用 OpenAI API 進行字幕翻譯。

## Features
- 使用 Flask 架設本地 RESTful API
- 透過 .env 讀取 API 金鑰，避免金鑰外洩
- 封裝 GPT-4o 自然語言翻譯，支援自訂 prompt
- 對接Tampermonkey

## 怎麼用?

1. 先到 OpenAI 申請 API Key，把它放到 key.env

2. 安裝套件（flask、.env、openai）

3. 啟動 proxy

## 為什麼做這個？

簡易自動化/筆記用。  
可以拿來跟瀏覽器外掛、Tampermonkey、任何自動化腳本串起來，大概。

---

## 注意事項

- key.env **勿上傳 github**，寫在 .gitignore 裡。
- 用於學習和測試用途，沒有任何商業包裝。

---

## 隨筆
- 想說趁著美金便宜用用看openai的API，結果手續費超貴，白癡


