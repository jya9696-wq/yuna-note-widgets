"""header_banner_v2.html 틀에 학생 이름을 넣어 PNG로 저장.
사용: python3 render_banner_v2.py 이름 출력.png"""
import sys, asyncio, pathlib
from playwright.async_api import async_playwright
name, out = sys.argv[1:3]
tpl = pathlib.Path(__file__).with_name('header_banner_v2.html').read_text(encoding='utf-8')
html = tpl.replace('{{NAME}}', name)
async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={'width': 760, 'height': 180}, device_scale_factor=4)
        await pg.set_content(html, wait_until='networkidle')
        await pg.locator('#banner').screenshot(path=out, omit_background=True)
        await b.close()
asyncio.run(main())
