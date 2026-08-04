import os

def build_svg(is_dark):
    bg_color = "#050505" if is_dark else "#fafafa"
    text_main = "#ffffff" if is_dark else "#111111"
    text_muted = "#737373" if is_dark else "#737373"
    accent = "#ffffff" if is_dark else "#000000"
    accent_dim = "#ffffff22" if is_dark else "#00000022"
    grid_color = "#ffffff0c" if is_dark else "#0000000c"
    panel_bg = "#ffffff05" if is_dark else "#00000005"
    
    # Generate random heights for the static CPU graph
    import random
    bars = ""
    for i in range(25):
        height = random.randint(5, 30)
        bars += f'<rect x="{i*8}" y="0" width="4" height="{height}" fill="{accent}" />\n'

    # The Braille Art
    art_lines = [
        "⠀⠀⠀⠀⠀⠀⠀⠀⢸⡏⠀⢠⡀⢳⡀⠀⣀⠀⠈⡆⠳⣄⠘⡄⢢⡀⠳⣽⡄⠀⠀⠁⣰⡁⠀⠀⠀⡆⠀⠀⣠⠎⠁⠀⠀⢀⡟⢰⣣⡏⠀⠀⠀⡴⠃⠀⠈⠀⣾",
        "⠀⠀⠀⠀⠀⠀⠀⠀⢾⠁⠀⠀⠄⡄⠹⣶⡏⠀⠀⡇⠀⠘⣷⣽⠀⢿⡄⠘⣇⣴⠀⠀⢩⡇⠀⠀⠀⠓⠦⠞⠁⠀⠀⠀⢀⠞⣹⠋⢁⡆⠀⠀⠀⠇⠰⠀⢀⣴⠃",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠀⠀⠀⠸⡄⡸⢻⡀⠀⡇⠀⠀⢸⡘⡆⠈⡇⠀⣿⢻⠀⢀⡟⠀⠀⠀⠀⠀⠀⠀⠀⣠⠆⡴⠁⣰⠇⢀⡟⠀⠀⡖⠀⠞⡰⢠⣿⠁",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⣈⣷⡀⠀⠀⢷⡇⠀⠻⣼⠀⠀⠀⡾⣷⡀⠀⢸⡄⡇⠘⣶⡼⠀⠀⠀⠀⠀⠀⣰⣦⠞⠁⢰⠁⢰⣯⣺⢏⠏⢀⣼⠃⢀⡼⢁⣬⡿",
        "⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⡇⠀⠀⣌⣇⠀⠀⠉⠘⣆⡴⠇⠀⢣⠀⠀⠻⡀⠀⠘⣇⠀⠀⠀⠀⣠⣾⣥⠟⠀⢀⣾⡄⢸⠃⢠⣞⣴⠋⣼⠠⣯⢊⠏⣾⣁",
        "⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⠹⣿⠀⠀⠹⣾⡄⠀⠀⠀⠈⢷⠀⠠⡈⢷⡀⠀⢳⡀⠀⠀⣆⠀⣠⢾⢟⡿⡁⢀⡴⣻⣿⠁⣟⣀⡽⢫⢏⡜⢁⣰⠏⡜⠀⢻⡟",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⡄⠈⢧⠀⢠⠘⢷⢸⠳⡄⠀⠀⢧⡀⢹⣶⡄⠀⢸⣿⠀⠀⣿⠟⢡⠏⣾⣼⡷⠋⣴⡏⣮⣾⢿⡇⢡⣯⢏⣠⣾⣁⣴⢃⣴⠋",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢳⡄⠈⣇⣿⠀⢰⡻⢧⣹⣄⠀⠀⠳⣄⢷⠈⢧⠘⢏⡆⣸⣁⣰⢏⡼⣿⡟⢠⠞⠟⡷⣿⣿⢀⡷⠚⢉⣿⡿⠚⣻⣱⠟⠁",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢿⣶⣆⣹⡠⣄⠳⡀⣹⢻⣿⣧⣀⣦⡙⡆⢻⠀⡼⣽⡿⢁⣯⡞⣀⣾⠟⠁⠀⠀⠀⣾⡟⣸⠁⣰⠿⡿⣣⣾⡽⢟⡟⠁",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣻⡷⣬⠲⡄⠿⢸⣿⢻⣿⣿⣿⣿⣾⣧⣁⢻⠃⣼⣼⡾⢻⣿⠀⠀⠀⠀⠀⢻⢇⣧⣴⠃⣼⡟⡝⡽⣿⡟",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢻⣋⠹⣌⣢⣿⠂⢸⣿⢸⣿⣿⣿⣿⣯⠙⢿⣾⣴⡿⠉⠀⠘⣿⡀⠀⠀⠀⠀⢸⣿⣩⣇⢠⣾⢸⡇⢘⣽⠛",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢷⣄⢹⣿⣄⠀⢻⣿⣿⣿⣿⣿⠟⠀⠀⠙⠃⠀⠀⣠⠒⢿⣷⡀⠀⠀⢀⣸⣿⡟⢻⣿⠃⣼⣵⠛⠁",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣮⣻⡿⢗⢦⣻⣿⣿⣿⣿⠆⠀⠀⢰⠇⠀⢰⠟⢀⡾⢹⣇⣠⣴⣿⣿⠋⠀⢿⠶⢋⣾⠙⠛⠳⠶⠦⢤⣄⣀⣀⡀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⠾⠻⣿⣿⢷⣜⠻⢿⣿⡿⠀⠀⠀⣼⠀⢀⡏⢀⣼⣧⣼⣯⠟⢋⣽⡏⠀⢀⣬⠴⣿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠛⠓⠶⢤⣀⡀",
        "⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⠾⣋⠁⠀⠀⢳⡹⣆⠉⠛⣦⣝⢧⡀⢠⡆⡧⡄⣈⡵⢋⣬⠶⠋⠀⣤⠿⠛⠀⠀⡼⠁⡄⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉",
        "⠀⠀⣠⣤⠄⠀⠠⠴⠶⠤⣴⠞⠋⠀⠀⠀⠀⠀⠀⠈⢧⣿⡗⢶⣤⣈⣳⣽⣦⡿⡇⣷⡿⢚⣿⣶⣶⣶⣿⠃⠀⠀⠀⢠⠇⠀⠃⠀⠙⡆",
        "⠈⠉⠀⠀⠀⠀⠀⢀⡴⠚⠁⠀⠀⠀⠀⠀⠀⠀⣠⣴⣿⣿⡇⠀⣿⣿⣿⣿⠙⠟⠁⠀⠀⠈⠀⢻⣿⣿⠃⠀⠀⠀⠀⣾⠀⠀⠀⠀⠀⠀⢀",
        "⠀⢀⣠⣴⣾⣿⡿⠋⠀⠀⠀⠀⠀⢀⡠⣴⣾⣿⣿⣿⣿⣿⡹⠀⣿⣿⣿⡃⣰⡆⠀⠀⠀⠀⠀⣿⡇⢸⠀⠀⠀⠀⢸⡿⠀⠀⠀⠀⢀⡴⣿⠛⣖⡀",
        "⣠⣿⣿⡿⠿⠋⠀⠀⠀⠀⠀⠀⣺⣽⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⢿⣏⢸⣏⡋⠀⠀⠀⠀⠀⠀⢿⡇⠘⠀⠀⠀⣠⣟⠀⠀⠀⠀⢀⣾⣵⣷⣬⣭⣽⠟⠓",
        "⠉⠁⠀⠀⠀⠀⠀⠀⣠⠤⢲⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡝⣾⣯⠈⢿⣝⢦⣠⣶⡀⠀⠀⠙⢷⠀⠀⢀⣴⣿⠙⠀⢠⠆⠀⣸⣿⣿⣿⣿⡏",
        "⣾⣿⣷⡄⠀⠀⠀⡀⠉⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠘⣿⡄⠈⢿⣿⠾⠾⠷⣖⡒⠂⢸⠀⣰⣿⣿⠏⠀⢀⡏⠀⢠⣿⣿⣿⣿⣿⣿⣦⡀",
        "⣿⣿⣿⠃⠀⠀⠀⣧⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢻⣿⣄⠀⢬⣉⣉⠉⠉⠉⠀⣼⣾⣿⣿⡟⠀⣠⡿⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣦⣄",
        "⣿⠟⣁⣤⣴⣿⣿⣿⣶⣤⡈⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡞⣿⣿⣦⡀⠀⠀⠀⠀⣠⣼⣿⣿⣿⠏⠀⣰⢿⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉",
        "⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣹⡼⣿⣿⣷⣄⣀⣀⣴⡿⡿⢻⣽⠋⠀⣰⠏⠘⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠛⠋",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣒⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⡻⣿⣿⠋⠀⠀⢀⡅⠀⢠⣿⠀⠀⠘⠻⠿⢿⣿⠿⠛⠋⠉⠀⢀⡀",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠉⠙⠻⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡽⣿⠀⠀⢠⡞⠀⢠⣿⡿⣦⣀⣤⣄⣀⣤⣤⣶⣶⣾⠿⠟⠉",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣶⣦⣤⣄⡀⠀⠈⠙⠿⣿⣿⣷⣾⣿⣿⣿⣿⡈⣇⣴⠏⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠞⠛⠙⠛⠛⠛⢿⣿⣿⣿⠟⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⢀",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⡏⣠⣾⣿⣿⣿⣿⣿⣿⣿⡿⢋⡴⠋⠀⠀⠀⠀⠀⠈",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣯⣥⣤⣤⣤⣤⣤⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⠏",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠏⠂",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⠏",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀"
    ]
    
    art_svg = ""
    for idx, line in enumerate(art_lines):
        art_svg += f'<tspan x="400" y="{20 + idx*12}">{line}</tspan>\n'

    svg = f"""<?xml version='1.0' encoding='utf-8'?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 880 420" width="100%" height="100%">
<defs>
  <style>
    @font-face {{
        src: local('Consolas'), local('Consolas Bold');
        font-family: 'ConsolasFallback';
        font-display: swap;
    }}
    .bg {{ fill: {bg_color}; }}
    .text-main {{ fill: {text_main}; font-family: ConsolasFallback, Consolas, monospace; font-size: 13px; font-weight: bold; }}
    .text-muted {{ fill: {text_muted}; font-family: ConsolasFallback, Consolas, monospace; font-size: 12px; }}
    .text-accent {{ fill: {accent}; font-family: ConsolasFallback, Consolas, monospace; font-size: 13px; font-weight: bold; }}
    .micro-text {{ fill: {text_muted}; font-family: ConsolasFallback, Consolas, monospace; font-size: 10px; letter-spacing: 2px; }}
    
    @keyframes pulseGlow {{
      0%, 100% {{ opacity: 0.6; filter: drop-shadow(0 0 4px {accent}); }}
      50% {{ opacity: 1; filter: drop-shadow(0 0 8px {accent}); }}
    }}
    @keyframes scanline {{
      0% {{ transform: translateY(-50px); }}
      100% {{ transform: translateY(450px); }}
    }}
    @keyframes blink {{
      0%, 49% {{ opacity: 1; }}
      50%, 100% {{ opacity: 0; }}
    }}
    
    .art {{
        fill: {text_main};
        font-family: ConsolasFallback, Consolas, monospace;
        font-size: 12px;
        white-space: pre;
    }}
    
    /* The hologram effect applies an intense red glow to the Braille art */
    .hologram {{
        fill: {accent};
        animation: pulseGlow 4s infinite ease-in-out;
        opacity: 0.85;
    }}
    
    .cursor {{ animation: blink 1s infinite; fill: {accent}; }}
    .scan {{ animation: scanline 8s linear infinite; fill: url(#scan-grad); pointer-events: none; opacity: 0.15; }}
  </style>
  
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M 20 0 L 20 40 M 0 20 L 40 20" stroke="{grid_color}" stroke-width="1" stroke-dasharray="2 2" />
    <circle cx="20" cy="20" r="1.5" fill="{accent_dim}" />
  </pattern>
  
  <linearGradient id="scan-grad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="{accent}" stop-opacity="0" />
    <stop offset="50%" stop-color="{accent}" stop-opacity="1" />
    <stop offset="100%" stop-color="{accent}" stop-opacity="0" />
  </linearGradient>
  
  <linearGradient id="art-fade" x1="100%" y1="0%" x2="0%" y2="0%">
    <stop offset="0%" stop-color="{accent}" stop-opacity="1" />
    <stop offset="70%" stop-color="{accent}" stop-opacity="0.3" />
    <stop offset="100%" stop-color="{accent}" stop-opacity="0" />
  </linearGradient>
</defs>

<!-- Background -->
<rect width="100%" height="100%" class="bg" />
<rect width="100%" height="100%" fill="url(#grid)" />

<!-- HUD Frame -->
<path d="M 20 10 L 860 10 L 870 20 L 870 400 L 860 410 L 20 410 L 10 400 L 10 20 Z" fill="none" stroke="{accent}" stroke-width="1.5" opacity="0.5" />
<path d="M 10 40 L 10 80 M 870 40 L 870 80 M 10 340 L 10 380 M 870 340 L 870 380" stroke="{accent}" stroke-width="4" />

<!-- Corner Micro-text -->
<text x="25" y="25" class="micro-text">SYS.INIT // CORE_V2.4</text>
<text x="710" y="25" class="micro-text">ENCRYPTED_CONNECTION_SECURE</text>

<!-- Holographic Art (Right side) -->
<g class="hologram">
  <text class="art">
{art_svg}
  </text>
</g>
<!-- Mask art on the left side to keep text readable -->
<rect x="10" y="10" width="450" height="400" class="bg" opacity="0.85" />
<rect x="10" y="10" width="450" height="400" fill="url(#grid)" opacity="0.3" />

<!-- HUD Info Panels (Left side) -->
<!-- Main Identity Box -->
<rect x="40" y="50" width="380" height="60" fill="{panel_bg}" stroke="{accent_dim}" stroke-width="1" />
<rect x="40" y="50" width="4" height="60" fill="{accent}" />
<text x="55" y="70" class="text-accent">[+] TARGET_IDENTITY</text>
<text x="55" y="95" class="text-main" font-size="20px" letter-spacing="1px">securitygeek15@system<tspan class="cursor">_</tspan></text>

<!-- Hardware Specs -->
<text x="40" y="140" class="text-accent">[+] SYSTEM_SPECS</text>
<path d="M 40 148 L 400 148" stroke="{text_muted}" stroke-width="1" stroke-dasharray="2 4" />
<text x="40" y="170" class="text-muted">OS</text><text x="140" y="170" class="text-main">Arch Linux</text>
<text x="40" y="195" class="text-muted">UPTIME</text><text x="140" y="195" class="text-main" id="uptime_data">17 years, 5 months</text>
<text x="40" y="220" class="text-muted">KERNEL</text><text x="140" y="220" class="text-main">Security &amp; Pentesting</text>
<text x="40" y="245" class="text-muted">IDE</text><text x="140" y="245" class="text-main">VSCode</text>

<!-- Skill Matrix -->
<text x="40" y="290" class="text-accent">[+] SKILL_MATRIX</text>
<path d="M 40 298 L 400 298" stroke="{text_muted}" stroke-width="1" stroke-dasharray="2 4" />
<text x="40" y="320" class="text-muted">LANGS</text><text x="140" y="320" class="text-main">Python, JS, Java, Go, Bash</text>
<text x="40" y="345" class="text-muted">SECTOR</text><text x="140" y="345" class="text-main">Bug Bounty, CTF, Automation</text>
<text x="40" y="370" class="text-muted">CONTACT</text><text x="140" y="370" class="text-main">goofyaapa@gmail.com</text>

<!-- Data Visualizer (Bottom Right) -->
<g transform="translate(640, 360)">
  <rect x="-10" y="-30" width="220" height="70" fill="{bg_color}" opacity="0.9" />
  <text x="0" y="-15" class="micro-text">CPU_LOAD_STREAM</text>
  {bars}
  <rect x="0" y="2" width="196" height="1" fill="{accent}" />
</g>

<!-- Top Right Stats -->
<rect x="660" y="40" width="180" height="90" fill="{bg_color}" stroke="{accent_dim}" stroke-width="1" />
<rect x="660" y="40" width="180" height="90" fill="{panel_bg}" />
<rect x="836" y="40" width="4" height="90" fill="{accent}" />
<text x="670" y="60" class="text-accent">[+] DATABANK</text>
<text x="670" y="80" class="text-muted">REPOS : <tspan class="text-main" id="repo_data">20</tspan></text>
<text x="670" y="100" class="text-muted">STARS : <tspan class="text-main" id="star_data">22</tspan></text>
<text x="670" y="120" class="text-muted">COMMITS: <tspan class="text-main" id="commit_data">122</tspan></text>
<text x="760" y="80" class="text-muted">PR: <tspan class="text-main" id="contrib_data">20</tspan></text>
<text x="760" y="100" class="text-muted">FL: <tspan class="text-main" id="follower_data">4</tspan></text>

<!-- Full scanline overlay -->
<rect width="100%" height="20" class="scan" />

</svg>
"""
    
    filename = "dark_mode.svg" if is_dark else "light_mode.svg"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)

build_svg(True)
build_svg(False)
