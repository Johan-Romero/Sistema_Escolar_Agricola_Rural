from playwright.sync_api import sync_playwright, Page, expect

def run(page: Page):
    # Navigate to the welcome page
    page.goto("http://127.0.0.1:8000/")

    # Open the login modal and take a screenshot
    page.get_by_role("button", name="Iniciar Sesión").click()
    expect(page.locator("#loginModal")).to_be_visible()
    page.screenshot(path="jules-scratch/verification/login_modal.png")

    # Close the login modal
    page.get_by_role("button", name="Cerrar").first.click()
    expect(page.locator("#loginModal")).not_to_be_visible()

    # Open the registration modal and take a screenshot
    page.get_by_role("button", name="Registrarse").click()
    expect(page.locator("#registroModal")).to_be_visible()
    page.screenshot(path="jules-scratch/verification/registro_modal.png")

def main():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        run(page)
        browser.close()

if __name__ == "__main__":
    main()
