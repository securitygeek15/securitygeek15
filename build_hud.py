import os
import random

def build_svg(is_dark):
    bg_color = "#000000" if is_dark else "#ffffff"
    text_main = "#ffffff" if is_dark else "#000000"
    text_muted = "#777777" if is_dark else "#888888"
    border_color = "#ffffff" if is_dark else "#000000"
    border_dim = "#333333" if is_dark else "#dddddd"
    grid_color = "#ffffff0a" if is_dark else "#0000000a"
    
    # Pure ASCII CPU load stream bars
    random.seed(1337)
    cpu_bars = ""
    for i in range(30):
        h = random.randint(4, 24)
        x_pos = i * 6
        cpu_bars += f'<rect x="{x_pos}" y="{26 - h}" width="3" height="{h}" fill="{text_main}" opacity="0.85" />\n'

    # Gojo "Nah, I'd win" Braille Art
    art_lines = [
        "⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⣾⡳⣼⣆⠀⠀⢹⡄⠹⣷⣄⢠⠇⠻⣷⣶⢀⣸⣿⡾⡏⠀⠰⣿⣰⠏⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⣀⣀⣀⡹⣟⡪⢟⣷⠦⠬⣿⣦⣌⡙⠿⡆⠻⡌⠿⣦⣿⣿⣿⣿⣦⣿⡿⠟⠚⠉⠀⠉⠳⣄⡀⠀⠀⠁⠀",
        "⠀⠀⠀⠀⠀⠀⠀⡀⢀⣼⣟⠛⠛⠙⠛⠉⠻⢶⣮⢿⣯⡙⢶⡌⠲⢤⡑⠀⠈⠛⠟⢿⣿⠛⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣆⠀⠀⠀",
        "⠀⠀⠀⠀⠀⡸⠯⣙⠛⢉⣉⣙⣿⣿⡳⢶⣦⣝⢿⣆⠉⠻⣄⠈⢆⢵⡈⠀⠀⢰⡆⠀⣼⠓⠀⠀⠀          Nah    ⠀⠀⠈⣷⠀⠀",
        "⠀⠀⠀⠖⠉⠻⣟⡿⣿⣭⢽⣽⣶⣈⢛⣾⣿⣧⠀⠙⠓⠀⠑⢦⡀⠹⣧⢂⠀⣿⡇⢀⣿⠺⠇⠀          ⠀I'd⠀          ⠀⣿⠀⠀",
        "⠀⠀⠀⠀⠐⠈⠉⢛⣿⣿⣶⣤⣈⠉⣰⣗⡈⢛⣇⠀⣵⡀⠀⠘⣿⡄⢻⣤⠀⢻⡇⣼⣧⣿⡄⠀⠀         Win⠀      ⠀⠀⡿⠀⠀",
        "⠀⠀⠀⠀⠀⣠⣾⣿⢍⡉⠛⠻⣷⡆⠨⣿⣭⣤⣍⠀⢹⣷⡀⠀⠹⣿⡄⠈⠀⢿⠁⣿⣿⠏⠀⠀⠀                        ⠀⠀⠀⣇⠀⠀",
        "⠀⣿⣇⣠⣾⣿⣛⣲⣿⠛⠀⠀⢀⣸⣿⣿⣟⣮⡻⣷⣤⡙⢟⡀⠀⠙⢧⠀⠀⠎⠀⠉⠁⠰⣿⠀⠀                         ⠀⢀⡿⠀⠀",
        "⠀⠈⢻⣿⣿⣽⣿⣿⣿⣴⡏⠚⢛⣈⣍⠛⠛⠿⢦⣌⢙⠻⡆⠁⠀⠀⠀⣴⣦⠀⠀⠀⠐⢳⢻⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠮⠀⠀⠀",
        "⠀⠀⠈⠙⣿⣧⣶⣿⠿⣧⣴⣿⢻⡉⠀⢀⣠⣴⣾⡟⠿⠃⠁⣠⣤⡶⣾⡟⠅⠀⣀⡄⠀⣾⢸⣿⣏⢻⢶⣦⣤⣤⣄⢶⣾⣿⣡⣤⡄⠀",
        "⠀⠀⣠⣞⣋⣿⣿⣾⣿⡿⡛⣹⡟⣤⢰⡿⠟⠉⣀⣀⣤⣤⡠⠙⢁⣾⡿⠂⠀⣿⠟⣁⠀⣹⠀⣹⣿⡟⣼⣿⣿⣌⣿⣞⣿⣿⠁⠀⠀⠀",
        "⠀⢠⡿⢛⢟⣿⣿⣿⣿⣿⣿⡟⣼⣿⣟⢓⠛⣿⣏⣿⣵⣗⣵⣴⣿⢟⡵⣣⣼⣿⢟⣵⣶⢻⣶⣿⠀⠀⣈⢻⣿⣿⣿⢿⣾⢿⣧⠀⠀⠀",
        "⠀⠘⠃⢸⣿⡾⣿⣿⣿⣿⣯⣿⣿⣿⣶⣿⣿⣟⣾⡿⣫⣿⣿⣿⣽⣿⣿⣿⣿⢫⣾⣿⣿⣿⣿⣿⣴⡆⣻⣿⡏⣿⢻⣧⣿⡿⣿⡆⠀⠀",
        "⠀⠀⠀⠜⣿⣾⢿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣭⣿⣖⣿⢿⣿⡿⣿⣿⣿⡿⢡⢯⣿⣿⣿⣿⣿⣿⣿⣧⡿⣾⣷⣿⣿⢿⣿⡇⠉⠁⠀⠀",
        "⠀⠀⠀⠀⣿⣥⣾⣿⣿⣿⣿⣿⣿⣿⡇⣭⣿⣿⣿⣿⠃⠞⠟⣸⣿⠏⣸⣧⣀⠿⢿⣿⣿⣟⣿⣿⣿⣿⣽⣿⢿⣿⣿⣿⣿⠁⠀⠀⠀⠀",
        "⠀⠀⠀⠈⠛⣹⣿⣿⣿⣿⢿⣿⣿⣿⣿⣿⣟⣿⣿⡿⢶⣦⣄⣿⠏⠀⣿⣟⣿⣶⠾⣿⣟ Russian⣿⣟⣋⣛⣿⣿⣿⣿⡇⣻⣿⣿⣿⡏⠀⠀⠀⠀⠀".replace("Russian", ""),
        "⠀⠀⠀⠀⠟⠛⠫⣿⣿⣿⣿⣿⡿⣧⠛⣿⠛⣿⣿⣿⣷⡌⠹⡟⠀⠀⠉⡟⠋⢠⣾⣿⣿⣿⡟⣿⣿⣿⣿⢀⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠘⠋⣾⣷⣿⣿⣧⠙⠀⠙⢣⠝⠛⠋⣽⣷⢦⠇⠀⠀⠘⠁⣤⣾⣿⠝⠛⠉⠘⢻⣿⣿⢿⣼⣷⡟⢻⣷⠉⠀⡀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠐⠟⢻⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠈⠛⠀⠀⠀⠀⠀⣾⠟⠀⢸⣷⣿⡇⠀⠛⠀⠀⠁⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠛⠁⠀⢹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣿⡧⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠆⠀⠀⠀⠀⠀⠀⠈⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣾⢻⡿⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣇⠀⠀⠀⠀⠀⠀⠀⠀⠲⣄⠀⡄⠆⠀⠀⠀⠀⠀⠀⠀⠀⣼⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⣷⡀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⣀⠀⠀⣠⣾⣿⠁⠀⠀⠀⠀⠀⣀⡄⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⢻⣆⠀⠛⠁⠶⣶⣶⣶⣶⣶⣶⡶⠆⠘⠋⣠⡾⢫⣾⡟⠀⠀⠀⠀⠀⠐⠉⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠛⠀⠙⣷⡀⠀⠀⠙⠛⠛⠛⠛⠋⠁⠀⢀⣴⠋⠀⣾⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣿⣰⣦⡀⠸⣿⣦⡀⠀⠀⠀⠀⠀⠀⢀⣴⡟⠁⠀⠐⢻⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⡄⢺⣿⡄⠹⣿⠻⢦⣤⣤⣤⣤⣶⣿⡟⢀⣀⠀⠀⢸⣿⣦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⠀⠀⠀⠀⢀⣠⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣮⣿⣿⡀⠹⡷⣦⣀⡀⡀⢸⣿⠏⢠⣾⣿⠀⠀⣾⣿⣿⣿⣿⣶⣄⣀⠀⠀⠀⠀⠀⠀⠀⠀",
        "⣀⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⧉⠀⠘⣷⣻⡟⠀⡼⠁⣴⣿⣿⣯⣥⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⠀⠀⠀",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣯⣿⣤⣤⣤⣬⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣄",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿"
    ]

    art_svg = ""
    for idx, line in enumerate(art_lines):
        art_svg += f'<tspan x="448" y="{170 + idx * 7.4}">{line}</tspan>\n'

    svg = f"""<?xml version='1.0' encoding='utf-8'?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 420" width="100%" height="100%">
<defs>
  <style>
    @font-face {{
        font-family: 'ConsolasFallback';
        src: local('Consolas'), local('Fira Code'), local('Cascadia Code'), local('Courier New'), monospace;
        font-display: swap;
    }}
    .bg {{ fill: {bg_color}; }}
    .text-main {{ fill: {text_main}; font-family: 'ConsolasFallback', Consolas, monospace; font-size: 13px; font-weight: bold; }}
    .text-muted {{ fill: {text_muted}; font-family: 'ConsolasFallback', Consolas, monospace; font-size: 11px; }}
    .text-title {{ fill: {text_main}; font-family: 'ConsolasFallback', Consolas, monospace; font-size: 18px; font-weight: bold; letter-spacing: 1px; }}
    .text-header {{ fill: {text_main}; font-family: 'ConsolasFallback', Consolas, monospace; font-size: 12px; font-weight: bold; letter-spacing: 1px; }}
    .micro-text {{ fill: {text_muted}; font-family: 'ConsolasFallback', Consolas, monospace; font-size: 10px; letter-spacing: 1px; }}
    
    @keyframes blink {{
      0%, 49% {{ opacity: 1; }}
      50%, 100% {{ opacity: 0; }}
    }}
    @keyframes scanline {{
      0% {{ transform: translateY(-40px); }}
      100% {{ transform: translateY(430px); }}
    }}
    
    .art {{
        fill: {text_main};
        font-family: 'ConsolasFallback', Consolas, monospace;
        font-size: 6.8px;
        white-space: pre;
        opacity: 0.95;
    }}
    
    .cursor {{ animation: blink 1s infinite; fill: {text_main}; }}
    .scan {{ animation: scanline 8s linear infinite; fill: url(#scan-grad); pointer-events: none; opacity: 0.1; }}
  </style>
  
  <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
    <line x1="0" y1="0" x2="20" y2="0" stroke="{grid_color}" stroke-width="0.5" />
    <line x1="0" y1="0" x2="0" y2="20" stroke="{grid_color}" stroke-width="0.5" />
  </pattern>
  
  <linearGradient id="scan-grad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="{text_main}" stop-opacity="0" />
    <stop offset="50%" stop-color="{text_main}" stop-opacity="0.6" />
    <stop offset="100%" stop-color="{text_main}" stop-opacity="0" />
  </linearGradient>
</defs>

<!-- Background -->
<rect width="100%" height="100%" class="bg" />
<rect width="100%" height="100%" fill="url(#grid)" />

<!-- Outer Minimal ASCII Border -->
<rect x="10" y="10" width="860" height="400" fill="none" stroke="{border_color}" stroke-width="1.5" />
<path d="M 10 18 L 18 10 M 862 10 L 870 18 M 10 402 L 18 410 M 862 410 L 870 402" stroke="{border_color}" stroke-width="1.5" />

<!-- Top Header Info -->
<text x="25" y="26" class="micro-text">SYS.INIT // NAH_ID_WIN // MONOCHROME_ASCII</text>
<text x="700" y="26" class="micro-text">STATUS: ACTIVE // SEC_NODE</text>
<line x1="10" y1="35" x2="870" y2="35" stroke="{border_color}" stroke-width="1" />

<!-- LEFT COLUMN: Identity, Specs, Skill Matrix -->

<!-- 1. IDENTITY BOX -->
<g transform="translate(25, 48)">
  <rect width="395" height="58" fill="none" stroke="{border_color}" stroke-width="1" />
  <text x="12" y="16" class="text-header">[ IDENTITY ]</text>
  <line x1="0" y1="24" x2="395" y2="24" stroke="{border_color}" stroke-width="0.8" stroke-dasharray="2 2" />
  <text x="12" y="44" class="text-title">securitygeek15@system<tspan class="cursor">_</tspan></text>
</g>

<!-- 2. SYSTEM SPECS BOX -->
<g transform="translate(25, 118)">
  <rect width="395" height="126" fill="none" stroke="{border_color}" stroke-width="1" />
  <text x="12" y="16" class="text-header">[ SYSTEM_SPECS ]</text>
  <line x1="0" y1="24" x2="395" y2="24" stroke="{border_color}" stroke-width="0.8" stroke-dasharray="2 2" />
  
  <text x="12" y="42" class="text-muted">OS      :</text><text x="90" y="42" class="text-main">Arch Linux (x86_64)</text>
  <text x="12" y="62" class="text-muted">UPTIME  :</text><text x="90" y="62" class="text-main" id="uptime_data">17 years, 6 months</text>
  <text x="12" y="82" class="text-muted">KERNEL  :</text><text x="90" y="82" class="text-main">Security &amp; Pentesting</text>
  <text x="12" y="102" class="text-muted">SHELL   :</text><text x="90" y="102" class="text-main">Zsh / Bash</text>
  <text x="240" y="82" class="text-muted">IDE   :</text><text x="285" y="82" class="text-main">Neovim</text>
  <text x="240" y="102" class="text-muted">SECTOR:</text><text x="285" y="102" class="text-main">Red Team</text>
</g>

<!-- 3. SKILL MATRIX BOX -->
<g transform="translate(25, 256)">
  <rect width="395" height="142" fill="none" stroke="{border_color}" stroke-width="1" />
  <text x="12" y="16" class="text-header">[ SKILL_MATRIX ]</text>
  <line x1="0" y1="24" x2="395" y2="24" stroke="{border_color}" stroke-width="0.8" stroke-dasharray="2 2" />
  
  <text x="12" y="42" class="text-muted">LANGS   :</text><text x="90" y="42" class="text-main">Python, Go, Bash, Java, JS, C/C++</text>
  <text x="12" y="62" class="text-muted">DOMAINS :</text><text x="90" y="62" class="text-main">Web Pentesting, CTF, Automation</text>
  <text x="12" y="82" class="text-muted">TOOLS   :</text><text x="90" y="82" class="text-main">Burp Suite, Metasploit, Wireshark</text>
  
  <!-- ASCII Progress Bars -->
  <text x="12" y="106" class="text-muted">OFFENSIVE SEC :</text>
  <text x="130" y="106" class="text-main">[==================  ] 90%</text>

  <text x="12" y="126" class="text-muted">AUTOMATION    :</text>
  <text x="130" y="126" class="text-main">[====================] 95%</text>
</g>

<!-- RIGHT COLUMN: Databank Stats & Braille Art -->

<!-- 1. DATABANK STATS BOX -->
<g transform="translate(435, 48)">
  <rect width="420" height="92" fill="none" stroke="{border_color}" stroke-width="1" />
  <text x="12" y="16" class="text-header">[ DATABANK ]</text>
  <line x1="0" y1="24" x2="420" y2="24" stroke="{border_color}" stroke-width="0.8" stroke-dasharray="2 2" />
  
  <!-- Row 1 -->
  <text x="12" y="46" class="text-muted">REPOS   :</text><text x="90" y="46" class="text-main" id="repo_data">20</text>
  <text x="150" y="46" class="text-muted">STARS   :</text><text x="220" y="46" class="text-main" id="star_data">24</text>
  <text x="290" y="46" class="text-muted">COMMITS :</text><text x="365" y="46" class="text-main" id="commit_data">127</text>

  <!-- Row 2 -->
  <text x="12" y="72" class="text-muted">CONTRIB :</text><text x="90" y="72" class="text-main" id="contrib_data">20</text>
  <text x="150" y="72" class="text-muted">FOLLOW  :</text><text x="220" y="72" class="text-main" id="follower_data">5</text>
  <text x="290" y="72" class="text-muted">RANK    :</text><text x="365" y="72" class="text-main">S+ TIER</text>
</g>

<!-- 2. BRAILLE ARTWORK STREAM BOX -->
<g transform="translate(435, 150)">
  <rect width="420" height="248" fill="none" stroke="{border_color}" stroke-width="1" />
  <text x="12" y="16" class="text-header">[ ARTWORK_STREAM ]</text>
  <line x1="0" y1="24" x2="420" y2="24" stroke="{border_color}" stroke-width="0.8" stroke-dasharray="2 2" />
  
  <g class="art">
{art_svg}
  </g>

  <!-- Bottom ASCII CPU Visualizer -->
  <g transform="translate(12, 212)">
    <line x1="0" y1="0" x2="396" y2="0" stroke="{border_dim}" stroke-width="0.8" stroke-dasharray="2 2" />
    <text x="0" y="18" class="micro-text">CPU_LOAD_STREAM :</text>
    <g transform="translate(130, 2)">
      {cpu_bars}
    </g>
    <text x="325" y="18" class="text-main" font-size="10px">99.8% UP</text>
  </g>
</g>

<!-- Scanline Overlay -->
<rect width="100%" height="20" class="scan" />

</svg>
"""

    filename = "dark_mode.svg" if is_dark else "light_mode.svg"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == '__main__':
    build_svg(True)
    build_svg(False)
    print("Gojo 'Nah, I'd win' ASCII HUD SVGs generated successfully!")
