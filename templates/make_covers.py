"""학생 페이지·필기노트 커버 배너 시안 (3000x1200, 가운데 띠에 핵심 — 넓은 화면/휴대폰에서 잘려도 괜찮게)"""
import sys, random
sys.path.insert(0, "/home/claude/yuna")
from make_v2 import tp, width, B, Y, N, W, FONT
from fontTools.ttLib import TTFont
FONT["numI"] = TTFont("/home/claude/yuna/gf/ofl/poppins/Poppins-ExtraBoldItalic.ttf")
FONT["popB"] = TTFont("/home/claude/yuna/gf/ofl/poppins/Poppins-Bold.ttf")
Wd, H = 3000, 1200
CX, CY = Wd / 2, H / 2
BL = "#7CC1FF"; G = "#7C828C"

def svg(body, defs=""):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{Wd}" height="{H}" viewBox="0 0 {Wd} {H}">'
            f'<defs>{defs}</defs>{body}</svg>')

def star(cx, cy, r, c, op=1):
    k = r * 0.16
    return (f'<path d="M{cx} {cy-r} Q{cx+k} {cy-k} {cx+r} {cy} Q{cx+k} {cy+k} {cx} {cy+r} '
            f'Q{cx-k} {cy+k} {cx-r} {cy} Q{cx-k} {cy-k} {cx} {cy-r}Z" fill="{c}" opacity="{op}"/>')

def grad(id_, c, a0=1, a1=0, x2=1):
    return (f'<linearGradient id="{id_}" x1="0" x2="{x2}" y1="0" y2="0"><stop offset="0" stop-color="{c}" stop-opacity="{a0}"/>'
            f'<stop offset="1" stop-color="{c}" stop-opacity="{a1}"/></linearGradient>')

def grid(step, c, op, sw=1.5):
    d = "".join(f"M{x} 0V{H}" for x in range(0, Wd + 1, step)) + "".join(f"M0 {y}H{Wd}" for y in range(0, H + 1, step))
    return f'<path d="{d}" stroke="{c}" stroke-width="{sw}" opacity="{op}"/>'

def blocks(x, y, cols, w=46, h=16, gap=12):
    return "".join(f'<rect x="{x+i*(w+gap)}" y="{y}" width="{w}" height="{h}" fill="{c}"/>' for i, c in enumerate(cols))

def center_title(main, font, size, y, fill, ls=0):
    return tp(main, font, size, CX, y, fill, anchor="middle", ls=ls)

def stars_scatter(seed, n, c, rmin=8, rmax=26, band=(80, 1120)):
    random.seed(seed); out = ""
    for _ in range(n):
        x = random.uniform(40, Wd - 40); y = random.uniform(*band)
        if 820 < x < 2180 and 440 < y < 760: continue  # 가운데 글자 자리 비움
        out += star(x, y, random.uniform(rmin, rmax), c, random.choice([.5, .75, 1]))
    return out

V = {}
# A. 블루 면 + 모눈 + 외곽선 대형 글자
b = [f'<rect width="{Wd}" height="{H}" fill="{B}"/>', grid(120, BL, .35),
     tp("FEEDBACK NOTE", "numI", 420, CX, 760, stroke=BL, sw=3, anchor="middle"),
     tp("YUNA ACADEMY", "monoM", 54, CX, 520, W, anchor="middle", ls=14),
     center_title("WEEKLY FEEDBACK NOTE", "numI", 150, 700, W),
     f'<rect x="{CX + width("WEEKLY FEEDBACK NOTE","numI",150)/2 + 18}" y="662" width="38" height="38" fill="{Y}"/>',
     star(560, 430, 34, W), star(2470, 780, 26, W, .8), star(2620, 400, 16, W, .6)]
V["A"] = svg("".join(b))

# B. 흰 종이 + 점 모눈 + HUD 꺾쇠
dots = "".join(f'<circle cx="{x}" cy="{y}" r="3" fill="{B}" opacity=".22"/>' for x in range(60, Wd, 60) for y in range(60, H, 60))
L = 70; fx0, fx1, fy0, fy1 = 760, 2240, 420, 780
hud = (f'<path d="M{fx0} {fy0+L}V{fy0}H{fx0+L} M{fx1-L} {fy0}H{fx1}V{fy0+L} M{fx1} {fy1-L}V{fy1}H{fx1-L} M{fx0+L} {fy1}H{fx0}V{fy1-L}" '
       f'fill="none" stroke="{B}" stroke-width="10"/>')
b = [f'<rect width="{Wd}" height="{H}" fill="#FFFFFF"/>', dots, hud,
     tp("[ YUNA ACADEMY / FEEDBACK NOTE ]", "mono", 40, CX, 500, G, anchor="middle", ls=4),
     center_title("이번 주 피드백 노트", "title", 150, 690, B),
     f'<rect x="{CX + width("이번 주 피드백 노트","title",150)/2 + 16}" y="650" width="36" height="36" fill="{Y}"/>',
     f'<rect x="0" y="598" width="{fx0-60}" height="5" fill="url(#gl)"/>',
     f'<rect x="{fx1+60}" y="598" width="{Wd-fx1-60}" height="5" fill="url(#gr)"/>',
     blocks(CX - 108, 728, [B, B, Y, G])]
V["B"] = svg("".join(b), grad("gl", B, 0, 1) + grad("gr", B, 1, 0))

# C. 연한 바탕 + 파랑→투명 속도선 + 반짝이
random.seed(3); lines = ""
for y in range(90, H, 46):
    if 430 < y < 780: continue
    x0 = random.uniform(-200, 600); ln = random.uniform(600, 2200); h = random.choice([3, 4, 6])
    lines += f'<rect x="{x0}" y="{y}" width="{ln}" height="{h}" fill="url(#gl)" opacity="{random.choice([.35,.6,.9])}"/>'
b = [f'<rect width="{Wd}" height="{H}" fill="#F3F8FF"/>', lines,
     tp("YUNA ACADEMY", "numI", 230, CX, 680, B, anchor="middle", ls=-4),
     tp("WEEKLY FEEDBACK NOTE  ·  EVERY WED", "monoM", 40, CX, 760, B, anchor="middle", ls=8),
     star(CX + width("YUNA ACADEMY", "numI", 230, -4) / 2 + 70, 500, 46, B),
     stars_scatter(5, 14, B, 8, 22)]
V["C"] = svg("".join(b), grad("gl", B, 1, 0))

# D. 밤하늘 (남색→파랑) + 반짝이
b = [f'<rect width="{Wd}" height="{H}" fill="url(#sky)"/>', grid(150, "#FFFFFF", .06),
     stars_scatter(11, 70, "#FFFFFF", 5, 20), stars_scatter(12, 18, BL, 10, 30),
     tp("FEEDBACK NOTE", "numI", 210, CX, 670, W, anchor="middle"),
     tp("YUNA ACADEMY  ·  WEEKLY", "monoM", 42, CX, 760, BL, anchor="middle", ls=12),
     f'<rect x="{CX + width("FEEDBACK NOTE","numI",210)/2 + 14}" y="626" width="40" height="40" fill="{Y}"/>']
V["D"] = svg("".join(b), f'<linearGradient id="sky" x1="0" x2="0" y1="0" y2="1"><stop offset="0" stop-color="{N}"/><stop offset="1" stop-color="{B}"/></linearGradient>')

# E. 큰 글자 잘라 쓰기 (블루 위 연파랑 YUNA) + 작은 라벨
b = [f'<rect width="{Wd}" height="{H}" fill="{B}"/>',
     tp("YUNA YUNA YUNA", "numI", 760, CX, 870, "#3DA2FB", anchor="middle", ls=-10),
     f'<rect x="{CX-620}" y="470" width="1240" height="260" fill="{B}"/>',
     f'<path d="M{CX-620} 470H{CX+620} M{CX-620} 730H{CX+620}" stroke="{W}" stroke-width="4"/>',
     tp("WEEKLY FEEDBACK", "numI", 132, CX, 655, W, anchor="middle"),
     tp("YUNA ACADEMY", "monoM", 36, CX - 600, 455, W, ls=8),
     tp("EVERY WED", "monoM", 36, CX + 600, 455, W, anchor="end", ls=8),
     f'<rect x="{CX+560}" y="746" width="40" height="40" fill="{Y}"/>', star(CX - 580, 766, 22, W)]
V["E"] = svg("".join(b))

for k, s in V.items():
    open(f"covers/cover_{k}.svg", "w").write(s)
    open(f"covers/cover_{k}_mono.svg", "w").write(s.replace(Y, W if k in "ADE" else B))
print("ok")
