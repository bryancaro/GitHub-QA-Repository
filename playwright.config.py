from playwright.sync_api import Playwright, sync_playwright

def run(playwright: Playwright) -> None:
    # Configuración global de Playwright
    browser = playwright.chromium.launch(
        headless=True,
        args=['--no-sandbox']
    )
    
    context = browser.new_context(
        viewport={'width': 1280, 'height': 720},
        record_video_dir='videos/',
        record_video_size={'width': 1280, 'height': 720}
    )
    
    # Cerrar el navegador al finalizar
    browser.close()

with sync_playwright() as playwright:
    run(playwright) 