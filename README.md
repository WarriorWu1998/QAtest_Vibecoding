🚀 Python 自動化測試與網頁註冊系統示範
這是一個專為初學者設計的教學專案，結合了 Flask 網頁開發與 Playwright/Pytest 自動化測試。
透過此專案，你可以學習從底層邏輯驗證（單元測試）到前端畫面自動化（UI 測試）的完整流程。

🛠 功能特點
後端邏輯：使用 Python 撰寫使用者註冊邏輯（包含帳號長度與重複性檢查）。

網頁介面：使用 Flask 框架搭建簡易的註冊頁面。

自動化測試：

單元測試 (Unit Test)：驗證核心邏輯是否正確。

UI 測試 (E2E Test)：使用 Playwright 模擬真實瀏覽器操作。

📦 環境建置步驟
1. 複製專案與建立虛擬環境
複製專案 (請將網址換成你自己的 GitHub 倉庫網址)
git clone https://github.com/WarriorWu1998/QAtest_VibeCoding.git
cd QAtest_VibeCoding

建立並啟動虛擬環境 (Windows)
python -m venv .venv
.venv\Scripts\activate

2. 安裝必要套件
pip install -r requirements.txt
playwright install

🚀 如何執行程式
步驟 A：啟動網頁伺服器
python app.py
啟動後，請在瀏覽器開啟：http://127.0.0.1:5000

步驟 B：執行自動化測試
注意：執行測試前，請確保上面的網頁伺服器 (app.py) 正在執行中。請開啟另一個終端機視窗執行：

執行所有測試案例 (pytest)
pytest

觀察 UI 自動化過程 (會自動彈出瀏覽器畫面)
python test_web_ui.py

📂 檔案結構說明
app.py: Flask 網頁伺服器主程式。

user_system.py: 使用者註冊的核心邏輯（被測試對象）。

test_user_system.py: 針對邏輯的單元測試腳本。

test_web_ui.py: 針對網頁畫面的 UI 自動化測試腳本。

templates/: 存放 HTML 網頁範本。

requirements.txt: 專案所需的套件版本清單。

.gitignore: 設定 Git 忽略上傳的檔案（如 .venv）。

⚠️ 測試重點說明
邊界值範例：在 user_system.py 中，帳號長度限制為 > 3。因此測試案例中的 "Bob" 會觸發錯誤，這是教學中刻意設計的報錯點，用來練習如何讀取測試報告。

環境隔離：本專案使用 pytest fixture 確保每個測試案例都在乾淨的狀態下執行。

完成貼上並存檔後，記得回到終端機執行最後的上傳指令：

git add README.md

git commit -m "docs: 建立完整的專案說明文件"

git push origin main