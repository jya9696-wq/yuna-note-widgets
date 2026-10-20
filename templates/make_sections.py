"""필기노트 섹션 제목 이미지 (번호 | 영문 라벨 + 한글 제목 + 선) — 시안 E(노랑 포인트) / F(단색 파랑)"""
import os, sys
sys.path.insert(0, "/home/claude/yuna")
from make_v2 import tp, width, B, Y, FONT
from fontTools.ttLib import TTFont
FONT["numI"] = TTFont("/home/claude/yuna/gf/ofl/poppins/Poppins-ExtraBoldItalic.ttf")
G = "#7C828C"
OUT = "/home/claude/yuna/sec"; os.makedirs(OUT, exist_ok=True)

def star(cx, cy, r, c):
    k = r * 0.16  # 오목한 4각 반짝이
    return (f'<path d="M{cx} {cy-r} Q{cx+k} {cy-k} {cx+r} {cy} Q{cx+k} {cy+k} {cx} {cy+r} '
            f'Q{cx-k} {cy+k} {cx-r} {cy} Q{cx-k} {cy-k} {cx} {cy-r}Z" fill="{c}"/>')

GRAD = '<defs><linearGradient id="gl" x1="0" x2="1" y1="0" y2="0"><stop offset="0" stop-color="#1F92F9"/><stop offset="1" stop-color="#1F92F9" stop-opacity="0"/></linearGradient></defs>'

def gline(x0, x1, y, h):
    return f'<rect x="{x0}" y="{y-h/2}" width="{x1-x0}" height="{h}" fill="url(#gl)"/>'

def thick(p, w):
    """같은 색 외곽선을 더해 고딕을 두껍게"""
    c = p.split('fill="')[1].split('"')[0]
    return p.replace('/>', f' stroke="{c}" stroke-width="{w}" stroke-linejoin="round"/>')

def label(en, ko, mono=False):
    """오늘의 한마디 같은 작은 라벨 줄 (별 없이): EN + 한글 + 오른쪽 선"""
    P = B if mono else Y
    Wd, H = 1470, 64
    b = [thick(tp(en, "monoM", 30, 4, 44, B, ls=3), 1.6)]
    ex = 4 + width(en, "monoM", 30, 3) + 22
    b.append(tp(ko, "koB", 27, ex, 44, B))
    lx = ex + width(ko, "koB", 27) + 26
    b.append(gline(lx, Wd - 40, 34, 4))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{Wd}" height="{H}" viewBox="0 0 {Wd} {H}">'
            + GRAD + "".join(b) + "</svg>")

def section(num, en, ko, mono=False):
    """비율: 사용자 레퍼런스(1470x202) 그대로 — 번호 75px, 세로선 x207, 라벨/제목 x259, 가운데 선 y101"""
    P = B if mono else Y
    Wd, H = 1470, 202
    body = []
    if num:
        body.append(tp(num, "numI", 104, 22, 136, B, ls=-2))
        body.append(f'<path d="M207 54V146" stroke="{G}" stroke-width="3"/>')
        tx = 259
    else:
        tx = 29
    body.append(thick(tp(en, "monoM", 33, tx, 66, B, ls=4), 1.8))
    body.append(tp(ko, "ko", 68, tx, 152, B, max_w=Wd - tx - 420))
    kw = min(width(ko, "ko", 68), Wd - tx - 420)
    sx = tx + kw + 10
    body.append(f'<rect x="{sx}" y="133" width="19" height="19" fill="{P}"/>')
    if not num:  # 단골 피드백: 오른쪽 선·블록 없이
        return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{Wd}" height="{H}" viewBox="0 0 {Wd} {H}">'
                + "".join(body) + "</svg>")
    lx = sx + 18 + 56
    body.append(gline(lx, Wd - 40, 101.5, 5))
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{Wd}" height="{H}" viewBox="0 0 {Wd} {H}">'
            + GRAD + "".join(body) + "</svg>")

ITEMS = [("s01", "01", "KEY FEEDBACK", "핵심 피드백"),
         ("s02", "02", "NEXT FOCUS", "앞으로 신경 쓸 부분"),
         ("s03", "03", "FIX LIST", "이번 그림에서 고칠 부분"),
         ("s04", "04", "REFERENCE", "같이 보면 좋은 자료"),
         ("s05", "05", "TODAY'S CLASS", "오늘의 수업 내용"),
         ("srep", None, "REPEAT FEEDBACK", "자주 나오는 단골 피드백")]
open(f"{OUT}/yuna3_today.svg", "w").write(label("TODAY'S POINT", "오늘의 한마디"))
open(f"{OUT}/yuna3f_today.svg", "w").write(label("TODAY'S POINT", "오늘의 한마디", mono=True))
for k, n, e, t in ITEMS:
    open(f"{OUT}/yuna3_{k}.svg", "w").write(section(n, e, t))
    open(f"{OUT}/yuna3f_{k}.svg", "w").write(section(n, e, t, mono=True))
# 미리보기
html = '<body style="margin:0;padding:20px;background:#fff">' + "".join(
    f'<img src="sec/yuna3_{k}.svg" style="width:700px;display:block;margin:8px 0">' for k, *_ in ITEMS+[("today",)]) + \
    '<div style="background:#191919;padding:20px">' + "".join(
    f'<img src="sec/yuna3f_{k}.svg" style="width:700px;display:block;margin:8px 0">' for k, *_ in ITEMS) + '</div>'
open("_sec.html", "w").write(html)
