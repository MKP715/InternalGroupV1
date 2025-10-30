import asyncio
from playwright.async_api import async_playwright
import os

async def main():
    async with async_playwright() as p:
        # On some systems, browsers need to be installed first.
        # This can be done by running `playwright install`
        try:
            browser = await p.chromium.launch()
        except Exception:
            print("Chromium browser not found. Installing...")
            os.system("playwright install chromium")
            browser = await p.chromium.launch()

        page = await browser.new_page()

        # Construct the file path for index.html
        # The file is in the root of the repo.
        file_path = "file://" + os.path.abspath("index.html")
        await page.goto(file_path)

        # We need to navigate to the "Photo Gallery" section first
        # The navigation is handled by a function called `goToSection`
        await page.evaluate("goToSection('gallery-section')")

        # Path to the test image
        # Let's create a dummy image for testing purposes if it doesn't exist
        image_path = os.path.abspath("jules-scratch/verification/test_image.png")
        if not os.path.exists(image_path):
            os.makedirs(os.path.dirname(image_path), exist_ok=True)
            with open(image_path, "w") as f:
                f.write("dummy image content")

        # Set the file for the input element
        # Using the locator to find the element by its ID
        await page.locator("#photo-upload").set_input_files(image_path)

        # Manually dispatch the 'change' event as a fallback
        await page.dispatch_event("#photo-upload", "change")

        # Give a moment for the event to propagate, just in case
        await page.wait_for_timeout(100)

        # Check if the button is enabled
        is_enabled = await page.is_enabled("#upload-btn")

        if is_enabled:
            print("VERIFICATION SUCCESS: Upload button is enabled after selecting a file.")
        else:
            print("VERIFICATION FAILURE: Upload button is still disabled after selecting a file.")

        await browser.close()

if __name__ == "__main__":
    asyncio.run(main())
