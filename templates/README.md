# 이미지 틀 (노션에 그림으로 넣는 것)

## header_banner_v2 — 학생 페이지 머리 배너
- 틀: `header_banner_v2.html` (`{{NAME}}` 자리에 학생 이름)
- 만들기: `python3 render_banner_v2.py 학생이름 출력.png` → 2960×624 PNG (4배 해상도)
- 노션: 학생 페이지 맨 위 이미지 블록. 학생마다 처음 한 번만 만들면 됨.
- 글꼴: Inter Display Black Italic, Noto Sans CJK KR (렌더링 환경에 설치돼 있어야 같은 모양)

## star_white.png
- 배경 없는 흰 반짝이 별 (256px). 카드 위젯 아이콘과 같은 모양.

# 웹 위젯 (노션 임베드)
- `../cards.html?nu=최근노트ID&cu=수업정리ID` — 07 바로가기 · QUICK LINKS (B안 띠). 노션 블록 높이 약 90px (휴대폰 약 70px).
