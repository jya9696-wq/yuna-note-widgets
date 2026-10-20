"""A 기반 이미지형 커버 (글씨는 얇은 외곽선 질감으로만)"""
import sys, random, math
sys.path.insert(0, "/home/claude/yuna")
from make_covers import svg, star, grad, grid, Wd, H, CX, CY, BL
from make_v2 import tp, B, Y, W, N
L2 = "#4FAAFB"

def _unused(): pass
def ostar(cx, cy, r, c, sw=3, op=1):
    k = r * 0.16
    return (f'<path d="M{cx} {cy-r} Q{cx+k} {cy-k} {cx+r} {cy} Q{cx+k} {cy+k} {cx} {cy+r} '
            f'Q{cx-k} {cy+k} {cx-r} {cy} Q{cx-k} {cy-k} {cx} {cy-r}Z" fill="none" stroke="{c}" stroke-width="{sw}" opacity="{op}"/>')

def sparkles(seed, n, c, rmin, rmax, op=(.5, .8, 1)):
    random.seed(seed); return "".join(star(random.uniform(60, Wd-60), random.uniform(80, H-80), random.uniform(rmin, rmax), c, random.choice(op)) for _ in range(n))

def wlines(seed, n, c="#FFFFFF"):
    random.seed(seed); o = ""
    for _ in range(n):
        y = random.uniform(120, H - 120); x = random.uniform(-300, 2200); ln = random.uniform(500, 1500)
        o += f'<rect x="{x}" y="{y}" width="{ln}" height="{random.choice([3,4,6])}" fill="url(#wl)" opacity="{random.choice([.35,.6,.9])}"/>'
    return o

defs = grad("wl", "#FFFFFF", 1, 0)
V = {}
# A1 외곽선 대형 글자 2줄 + 속도선 + 반짝이
V["A1"] = svg("".join([f'<rect width="{Wd}" height="{H}" fill="{B}"/>', grid(120, BL, .3),
    tp("FEEDBACK", "numI", 560, CX, 590, stroke=BL, sw=3, anchor="middle"),
    tp("NOTE  NOTE", "numI", 560, CX + 300, 1130, stroke=BL, sw=3, anchor="middle"),
    wlines(7, 9), sparkles(2, 9, W, 14, 46),
    f'<rect x="2260" y="520" width="40" height="40" fill="{Y}"/>', f'<rect x="700" y="760" width="26" height="26" fill="{Y}"/>']), defs)

# A2 HUD 원·조준선 + 모눈 + 반짝이
rings = "".join(f'<circle cx="{CX}" cy="{CY}" r="{r}" fill="none" stroke="{BL}" stroke-width="{w}" opacity="{o}"/>'
                for r, w, o in [(180, 4, .9), (300, 2.5, .6), (460, 2, .45), (680, 2, .3), (960, 2, .2)])
ticks = "".join(f'<path d="M{CX+math.cos(a)*300} {CY+math.sin(a)*300} L{CX+math.cos(a)*340} {CY+math.sin(a)*340}" stroke="{W}" stroke-width="4"/>'
                for a in [i * math.pi / 12 for i in range(24)])
V["A2"] = svg("".join([f'<rect width="{Wd}" height="{H}" fill="{B}"/>', grid(120, BL, .25), rings, ticks,
    f'<path d="M0 {CY}H{Wd} M{CX} 0V{H}" stroke="{W}" stroke-width="2" opacity=".35"/>',
    star(CX, CY, 90, W), ostar(CX, CY, 150, W, 3),
    star(CX + 300, CY - 260, 46, W), sparkles(4, 10, W, 10, 34),
    f'<rect x="{CX-460-20}" y="{CY-20}" width="40" height="40" fill="{Y}"/>']), defs)

# A3 대각 줄무늬 질감 + 큰 외곽선 반짝이 별들
diag = "".join(f'<path d="M{x} 0 L{x-H} {H}" stroke="{BL}" stroke-width="2" opacity=".25"/>' for x in range(0, Wd + H, 40))
V["A3"] = svg("".join([f'<rect width="{Wd}" height="{H}" fill="{B}"/>', diag,
    ostar(CX, CY, 360, W, 5), ostar(CX - 520, CY + 120, 170, BL, 4), ostar(CX + 560, CY - 140, 210, BL, 4),
    ostar(CX + 980, CY + 260, 120, BL, 3, .7), ostar(CX - 1050, CY - 250, 110, BL, 3, .7),
    star(CX, CY, 70, W), sparkles(9, 12, W, 8, 26),
    f'<rect x="{CX+200}" y="{CY+240}" width="34" height="34" fill="{Y}"/>']), "")

# A4 반복 외곽선 YUNA 질감 + 흰 블록 줄 + 반짝이
rows = "".join(tp("FEEDBACK  NOTE  FEEDBACK", "numI", 300, -200 + (i % 2) * 400, 260 + i * 300, stroke=L2, sw=2.5) for i in range(4))
V["A4"] = svg("".join([f'<rect width="{Wd}" height="{H}" fill="{B}"/>', rows, grid(150, BL, .18),
    f'<rect x="0" y="{CY-3}" width="{Wd}" height="6" fill="url(#wl)" transform="translate({Wd} 0) scale(-1 1)"/>',
    "".join(f'<rect x="{CX-150+i*80}" y="{CY+60}" width="60" height="18" fill="{c}"/>' for i, c in enumerate([W, W, Y, W])),
    star(CX - 220, CY - 120, 60, W), sparkles(13, 10, W, 10, 30)]), defs)

for k, s in V.items():
    open(f"covers/cover_{k}.svg", "w").write(s)
    open(f"covers/cover_{k}_mono.svg", "w").write(s.replace(Y, W))
print("ok")
