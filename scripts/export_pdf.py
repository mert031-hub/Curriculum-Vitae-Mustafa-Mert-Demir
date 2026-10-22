"""Generate the Turkish and English A4 PDFs from their HTML with Chromium."""
from pathlib import Path
from functools import partial
from http.server import SimpleHTTPRequestHandler, ThreadingHTTPServer
from threading import Thread
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parents[1]


def main():
    destination = ROOT / "downloads"
    destination.mkdir(exist_ok=True)
    server = ThreadingHTTPServer(("127.0.0.1", 0), partial(SimpleHTTPRequestHandler, directory=str(ROOT)))
    Thread(target=server.serve_forever, daemon=True).start()
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(executable_path="/usr/bin/chromium", args=["--no-sandbox"])
            for source, locale, variants in [
                ("index.html", "tr-TR", [
                    (False, "Mustafa-Mert-Demir-CV.pdf"),
                    (True, "Mustafa-Mert-Demir-CV-Referansli.pdf"),
                ]),
                ("cv-en.html", "en-GB", [
                    (None, "Mustafa-Mert-Demir-CV-European-EN.pdf"),
                ]),
            ]:
                page = browser.new_page(viewport={"width": 1200, "height": 1400}, locale=locale)
                page.goto(f"http://127.0.0.1:{server.server_port}/{source}")
                page.evaluate("document.fonts.ready")
                for include, filename in variants:
                    if include is not None:
                        page.locator("#include-references").set_checked(include)
                    page.pdf(path=str(destination / filename), format="A4", print_background=True,
                             prefer_css_page_size=True, display_header_footer=False)
                    print(destination / filename)
                page.close()
            browser.close()
    finally:
        server.shutdown()
        server.server_close()


if __name__ == "__main__":
    main()
