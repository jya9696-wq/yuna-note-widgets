import asyncio, pathlib
from playwright.async_api import async_playwright
items=[('01','KEY FEEDBACK','핵심 피드백','03_섹션_핵심피드백.png'),
       ('02','FOCUS NEXT','앞으로 신경 쓸 부분','04_섹션_앞으로신경쓸부분.png'),
       ('03','FIX NOW','이번 그림에서 고칠 부분','05_섹션_이번그림에서고칠부분.png')]
tpl=pathlib.Path('section_heading.html').read_text()
async def main():
    async with async_playwright() as p:
        b=await p.chromium.launch()
        pg=await b.new_page(viewport={'width':740,'height':80},device_scale_factor=4)
        for n,eb,tt,out in items:
            await pg.set_content(tpl.replace('{{NUM}}',n).replace('{{EB}}',eb).replace('{{TT}}',tt),wait_until='networkidle')
            await pg.locator('#h').screenshot(path=out,omit_background=True)
        await b.close()
asyncio.run(main())
