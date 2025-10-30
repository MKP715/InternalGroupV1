import asyncio
from playwright.async_api import async_playwright, expect
import os

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        file_path = os.path.abspath('index.html')
        await page.goto(f'file://{file_path}')

        # Get initial image count
        gallery = page.locator('#gallery')
        initial_image_count = await gallery.locator('img').count()

        # Upload a file
        await page.locator('#photo-upload').set_input_files('test-image.jpg')

        # Click the upload button
        await page.get_by_role("button", name="Upload Photos").click()

        # Wait for the success toast message
        await expect(page.locator('.toast.success')).to_be_visible(timeout=10000)
        await expect(page.locator('.toast.success')).to_have_text("1 photo(s) uploaded successfully!")

        # Wait for the gallery to have one more image.
        await expect(gallery.locator('img')).to_have_count(initial_image_count + 1, timeout=10000)

        # Take a screenshot
        await page.screenshot(path='jules-scratch/verification/verification.png')

        await browser.close()

if __name__ == '__main__':
    asyncio.run(main())
