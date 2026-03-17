# test_web_ui.py
from playwright.sync_api import sync_playwright

def test_registration_ui():
    with sync_playwright() as p:
        # 1. 開啟瀏覽器 (headless=False 讓你可以在螢幕上看到它動)
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()

        # 2. 前往你的 Flask 網頁
        page.goto("http://127.0.0.1:5000")

        # 3. 填寫帳號與密碼 (使用 HTML 的 name 屬性定位)
        page.fill('input[name="username"]', "AutomationTester")
        page.fill('input[name="password"]', "SuperSecret123")

        # 4. 點擊「立即註冊」按鈕
        page.click('input[type="submit"]')

        # 5. 驗證結果頁面是否包含 "Success" 字樣
        # 我們預期會看到 "註冊結果：Success"
        assert "Success" in page.content()

        print("\nUI 測試成功：瀏覽器已成功完成自動註冊！")
        
        # 關閉瀏覽器
        browser.close()

if __name__ == "__main__":
    test_registration_ui()