import os
import random

def build_svg(is_dark):
    # Palette definition
    if is_dark:
        bg_color = "#080c14"
        bg_gradient_start = "#0f172a"
        bg_gradient_end = "#080c14"
        panel_bg = "#0f172a"
        panel_bg_opacity = "0.6"
        panel_border = "#00f0ff"
        panel_border_dim = "#00f0ff33"
        text_main = "#f8fafc"
        text_muted = "#94a3b8"
        accent_primary = "#00f0ff"      # Neon Cyan
        accent_secondary = "#00ff9d"    # Neon Green
        accent_tertiary = "#b026ff"     # Neon Magenta
        grid_color = "#00f0ff0d"
        card_bg = "#1e293b"
        card_bg_opacity = "0.5"
        bar_fill = "#00f0ff"
        glow_color = "#00f0ff"
    else:
        bg_color = "#f8fafc"
        bg_gradient_start = "#ffffff"
        bg_gradient_end = "#f1f5f9"
        panel_bg = "#ffffff"
        panel_bg_opacity = "0.85"
        panel_border = "#2563eb"
        panel_border_dim = "#2563eb33"
        text_main = "#0f172a"
        text_muted = "#64748b"
        accent_primary = "#2563eb"      # Electric Blue
        accent_secondary = "#059669"    # Emerald Green
        accent_tertiary = "#7c3aed"     # Deep Violet
        grid_color = "#2563eb0d"
        card_bg = "#f1f5f9"
        card_bg_opacity = "0.7"
        bar_fill = "#2563eb"
        glow_color = "#2563eb"

    # Dynamic CPU Load stream bars
    random.seed(42) # Deterministic yet organic bars
    cpu_bars = ""
    for i in range(28):
        h = random.randint(6, 32)
        x_pos = i * 7
        color = accent_primary if i % 4 != 0 else accent_secondary
        cpu_bars += f'<rect x="{x_pos}" y="{35 - h}" width="4" height="{h}" fill="{color}" rx="1" opacity="0.85" />\n'

    # Cyber Braille Art
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
        "⣿⣿⣿⠃⠀⠀⠀⣧⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣇⢻⣿⣄⠀⢬⣉⣉⠉⠉⠉⠀⣼⣾⣿⣿⡟⠀⣠⡿⠀⢀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣶⣶⣶⣶⣦⣄",
        "⣿⠟⣁⣤⣴⣿⣿⣿⣶⣤⡈⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡞⣿⣿⣦⡀⠀⠀⠀⠀⣠⣼⣿⣿⣿⠏⠀⣰⢿⠁⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⠉",
        "⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡀⠀⠙⣿⣿⣿⣿⣿⣿⣿⣿⣿⣟⣹⡼⣿⣿⣷⣄⣀⣀⣴⡿⡿⢻⣽⠋⠀⣰⠏⠘⣦⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠛⠛⠛⠛⠛⠋",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣛⣒⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⣿⡻⣿⣿⠋⠀⠀⢀⡅⠀⢠⣿⠀⠀⠘⠻⠿⢿⣿⠿⠛⠋⠉⠀⢀⡀",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠋⠉⠉⠙⠻⠿⠿⠿⠿⢿⣿⣿⣿⣿⣿⡇⢸⣿⣿⣿⡽⣿⠀⠀⢠⡞⠀⢠⣿⡿⣦⣀⣤⣄⣀⣤⣤⣶⣶⣾⠿⠟⠉",
        "⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣿⣿⣿⣿⣶⣦⣤⣄⡀⠀⠈⠙⠿⣿⣿⣷⣾⣿⣿⣿⣿⡈⣇⣴⠏⠀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⠁"
    ]

    art_svg = ""
    for idx, line in enumerate(art_lines):
        art_svg += f'<tspan x="475" y="{202 + idx * 9.2}">{line}</tspan>\n'

    svg = f"""<?xml version='1.0' encoding='utf-8'?>
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 920 460" width="100%" height="100%">
<defs>
  <style>
    @font-face {{
        font-family: 'ConsolasFallback';
        src: local('Consolas'), local('Fira Code'), local('Cascadia Code'), local('Courier New'), monospace;
        font-display: swap;
    }}
    .bg {{ fill: url(#bg-grad); }}
    .font-mono {{ font-family: 'ConsolasFallback', Consolas, 'Fira Code', monospace; }}
    
    .text-main {{ fill: {text_main}; font-family: 'ConsolasFallback', Consolas, monospace; font-size: 13px; font-weight: 600; }}
    .text-muted {{ fill: {text_muted}; font-family: 'ConsolasFallback', Consolas, monospace; font-size: 11px; }}
    .text-accent {{ fill: {accent_primary}; font-family: 'ConsolasFallback', Consolas, monospace; font-size: 12px; font-weight: bold; letter-spacing: 0.5px; }}
    .text-title {{ fill: {text_main}; font-family: 'ConsolasFallback', Consolas, monospace; font-size: 21px; font-weight: 800; letter-spacing: 1px; }}
    .text-stat-val {{ fill: {text_main}; font-family: 'ConsolasFallback', Consolas, monospace; font-size: 16px; font-weight: 800; }}
    .text-stat-lbl {{ fill: {text_muted}; font-family: 'ConsolasFallback', Consolas, monospace; font-size: 10px; letter-spacing: 1px; font-weight: 600; }}
    .micro-text {{ fill: {text_muted}; font-family: 'ConsolasFallback', Consolas, monospace; font-size: 10px; letter-spacing: 1.5px; }}
    
    @keyframes pulseGlow {{
      0%, 100% {{ opacity: 0.7; filter: drop-shadow(0 0 3px {glow_color}); }}
      50% {{ opacity: 1; filter: drop-shadow(0 0 9px {glow_color}); }}
    }}
    @keyframes pulseDot {{
      0%, 100% {{ opacity: 1; r: 4; }}
      50% {{ opacity: 0.4; r: 5; }}
    }}
    @keyframes scanline {{
      0% {{ transform: translateY(-40px); }}
      100% {{ transform: translateY(470px); }}
    }}
    @keyframes blink {{
      0%, 49% {{ opacity: 1; }}
      50%, 100% {{ opacity: 0; }}
    }}
    @keyframes radarSpin {{
      0% {{ transform: rotate(0deg); }}
      100% {{ transform: rotate(360deg); }}
    }}
    
    .art {{
        fill: {accent_primary};
        font-family: 'ConsolasFallback', Consolas, monospace;
        font-size: 7.8px;
        white-space: pre;
        opacity: 0.85;
    }}
    
    .hologram {{
        animation: pulseGlow 4s infinite ease-in-out;
    }}
    
    .cursor {{ animation: blink 1s infinite; fill: {accent_primary}; }}
    .status-dot {{ animation: pulseDot 2s infinite ease-in-out; fill: {accent_secondary}; }}
    .scan {{ animation: scanline 7s linear infinite; fill: url(#scan-grad); pointer-events: none; opacity: 0.12; }}
    .radar-line {{ transform-origin: 675px 305px; animation: radarSpin 12s linear infinite; }}
  </style>
  
  <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="{bg_gradient_start}" />
    <stop offset="100%" stop-color="{bg_gradient_end}" />
  </linearGradient>

  <pattern id="grid" width="30" height="30" patternUnits="userSpaceOnUse">
    <path d="M 30 0 L 0 0 0 30" fill="none" stroke="{grid_color}" stroke-width="1" />
    <circle cx="30" cy="30" r="1" fill="{panel_border_dim}" />
  </pattern>
  
  <linearGradient id="scan-grad" x1="0%" y1="0%" x2="0%" y2="100%">
    <stop offset="0%" stop-color="{accent_primary}" stop-opacity="0" />
    <stop offset="50%" stop-color="{accent_primary}" stop-opacity="0.8" />
    <stop offset="100%" stop-color="{accent_primary}" stop-opacity="0" />
  </linearGradient>

  <linearGradient id="panel-grad" x1="0%" y1="0%" x2="100%" y2="100%">
    <stop offset="0%" stop-color="{panel_bg}" stop-opacity="{panel_bg_opacity}" />
    <stop offset="100%" stop-color="{card_bg}" stop-opacity="{card_bg_opacity}" />
  </linearGradient>
  
  <filter id="glow" x="-20%" y="-20%" width="140%" height="140%">
    <feGaussianBlur stdDeviation="3" result="blur" />
    <feComposite in="SourceGraphic" in2="blur" operator="over" />
  </filter>
</defs>

<!-- Background -->
<rect width="100%" height="100%" class="bg" rx="10" />
<rect width="100%" height="100%" fill="url(#grid)" rx="10" />

<!-- Outer HUD Frame Chamfered -->
<path d="M 20 12 L 900 12 L 910 22 L 910 438 L 900 448 L 20 448 L 10 438 L 10 22 Z" 
      fill="none" stroke="{panel_border}" stroke-width="1.2" stroke-opacity="0.4" />

<!-- Outer Corner Tech Accents -->
<path d="M 10 32 L 10 22 L 20 12 M 900 12 L 910 22 L 910 32 M 10 428 L 10 438 L 20 448 M 900 448 L 910 438 L 910 428" 
      fill="none" stroke="{accent_primary}" stroke-width="2.5" />

<!-- Top Header Navigation Bar -->
<rect x="20" y="20" width="880" height="32" fill="{panel_bg}" fill-opacity="0.7" rx="4" stroke="{panel_border_dim}" stroke-width="1" />
<circle cx="36" cy="36" r="4" class="status-dot" />
<text x="48" y="40" class="text-accent" font-size="11px">[● ONLINE]</text>
<text x="135" y="40" class="micro-text">SYS.SECURITY.HUD v3.5 // NODE: securitygeek15</text>
<text x="640" y="40" class="micro-text">ENCRYPTED_SESSION [256-BIT]</text>
<rect x="805" y="27" width="85" height="18" fill="{accent_primary}" fill-opacity="0.15" rx="3" stroke="{accent_primary}" stroke-width="0.8" />
<text x="812" y="40" class="text-accent" font-size="9px">SEC_LEVEL: ALPHA</text>

<!-- LEFT PANEL: Identity, Specs & Arsenal -->

<!-- 1. Identity Card -->
<g transform="translate(24, 62)">
  <rect width="424" height="66" fill="url(#panel-grad)" rx="6" stroke="{panel_border_dim}" stroke-width="1" />
  <rect x="0" y="0" width="4" height="66" fill="{accent_primary}" rx="2" />
  <text x="16" y="22" class="text-accent">[+] TARGET_IDENTITY</text>
  <text x="16" y="48" class="text-title">securitygeek15<tspan class="cursor">_</tspan></text>
  <text x="300" y="22" class="micro-text" font-size="9px">ROLE: SEC_ENG</text>
  <text x="235" y="48" class="text-muted" font-size="11px">Cyber Sec &amp; Pentester</text>
</g>

<!-- 2. System Diagnostics Card -->
<g transform="translate(24, 138)">
  <rect width="424" height="126" fill="url(#panel-grad)" rx="6" stroke="{panel_border_dim}" stroke-width="1" />
  <text x="16" y="20" class="text-accent">[+] SYSTEM_DIAGNOSTICS</text>
  <line x1="16" y1="28" x2="408" y2="28" stroke="{panel_border_dim}" stroke-width="1" stroke-dasharray="3 3" />
  
  <!-- Column 1 -->
  <text x="16" y="48" class="text-muted">OS</text>
  <text x="80" y="48" class="text-main">Arch Linux (x86_64)</text>
  
  <text x="16" y="72" class="text-muted">KERNEL</text>
  <text x="80" y="72" class="text-main">Security &amp; Hardened</text>
  
  <text x="16" y="96" class="text-muted">SHELL</text>
  <text x="80" y="96" class="text-main">Zsh / Bash</text>

  <text x="16" y="116" class="text-muted">IDE</text>
  <text x="80" y="116" class="text-main">Neovim / VS Code</text>

  <!-- Column 2 -->
  <text x="230" y="48" class="text-muted">UPTIME</text>
  <text x="290" y="48" class="text-main" id="uptime_data">17 years, 6 months</text>

  <text x="230" y="72" class="text-muted">STATUS</text>
  <text x="290" y="72" class="text-main">🟢 Active / Hunting</text>

  <text x="230" y="96" class="text-muted">SECTOR</text>
  <text x="290" y="96" class="text-main">Red Team / CTF</text>

  <text x="230" y="116" class="text-muted">CONTACT</text>
  <text x="290" y="116" class="text-main" font-size="11px">goofyaapa@gmail.com</text>
</g>

<!-- 3. Skill Arsenal & Progress Matrix -->
<g transform="translate(24, 274)">
  <rect width="424" height="166" fill="url(#panel-grad)" rx="6" stroke="{panel_border_dim}" stroke-width="1" />
  <text x="16" y="20" class="text-accent">[+] SECURITY &amp; TECH ARSENAL</text>
  <line x1="16" y1="28" x2="408" y2="28" stroke="{panel_border_dim}" stroke-width="1" stroke-dasharray="3 3" />
  
  <!-- Skill Category Badges -->
  <text x="16" y="46" class="text-muted">LANGS</text>
  <g transform="translate(75, 34)">
    <rect x="0" y="0" width="52" height="18" fill="{card_bg}" fill-opacity="{card_bg_opacity}" rx="3" stroke="{panel_border_dim}" stroke-width="0.8" />
    <text x="26" y="13" class="text-main" font-size="10px" text-anchor="middle">Python</text>
    
    <rect x="58" y="0" width="40" height="18" fill="{card_bg}" fill-opacity="{card_bg_opacity}" rx="3" stroke="{panel_border_dim}" stroke-width="0.8" />
    <text x="78" y="13" class="text-main" font-size="10px" text-anchor="middle">Go</text>
    
    <rect x="104" y="0" width="44" height="18" fill="{card_bg}" fill-opacity="{card_bg_opacity}" rx="3" stroke="{panel_border_dim}" stroke-width="0.8" />
    <text x="126" y="13" class="text-main" font-size="10px" text-anchor="middle">Bash</text>
    
    <rect x="154" y="0" width="42" height="18" fill="{card_bg}" fill-opacity="{card_bg_opacity}" rx="3" stroke="{panel_border_dim}" stroke-width="0.8" />
    <text x="175" y="13" class="text-main" font-size="10px" text-anchor="middle">Java</text>
    
    <rect x="202" y="0" width="34" height="18" fill="{card_bg}" fill-opacity="{card_bg_opacity}" rx="3" stroke="{panel_border_dim}" stroke-width="0.8" />
    <text x="219" y="13" class="text-main" font-size="10px" text-anchor="middle">JS</text>

    <rect x="242" y="0" width="44" height="18" fill="{card_bg}" fill-opacity="{card_bg_opacity}" rx="3" stroke="{panel_border_dim}" stroke-width="0.8" />
    <text x="264" y="13" class="text-main" font-size="10px" text-anchor="middle">C/C++</text>
  </g>

  <text x="16" y="74" class="text-muted">DOMAINS</text>
  <g transform="translate(75, 62)">
    <rect x="0" y="0" width="90" height="18" fill="{card_bg}" fill-opacity="{card_bg_opacity}" rx="3" stroke="{panel_border_dim}" stroke-width="0.8" />
    <text x="45" y="13" class="text-main" font-size="10px" text-anchor="middle">Web Pentesting</text>
    
    <rect x="96" y="0" width="70" height="18" fill="{card_bg}" fill-opacity="{card_bg_opacity}" rx="3" stroke="{panel_border_dim}" stroke-width="0.8" />
    <text x="131" y="13" class="text-main" font-size="10px" text-anchor="middle">Bug Bounty</text>
    
    <rect x="172" y="0" width="42" height="18" fill="{card_bg}" fill-opacity="{card_bg_opacity}" rx="3" stroke="{panel_border_dim}" stroke-width="0.8" />
    <text x="193" y="13" class="text-main" font-size="10px" text-anchor="middle">CTF</text>
    
    <rect x="220" y="0" width="72" height="18" fill="{card_bg}" fill-opacity="{card_bg_opacity}" rx="3" stroke="{panel_border_dim}" stroke-width="0.8" />
    <text x="256" y="13" class="text-main" font-size="10px" text-anchor="middle">Automation</text>
  </g>

  <!-- Skill Progress Fills -->
  <g transform="translate(16, 96)">
    <text x="0" y="12" class="text-muted" font-size="10px">OFFENSIVE SEC</text>
    <rect x="110" y="3" width="220" height="10" fill="{card_bg}" rx="3" />
    <rect x="110" y="3" width="206" height="10" fill="{accent_primary}" rx="3" opacity="0.9" />
    <text x="340" y="12" class="text-accent" font-size="10px">94%</text>

    <text x="0" y="32" class="text-muted" font-size="10px">AUTOMATION &amp; BOT</text>
    <rect x="110" y="23" width="220" height="10" fill="{card_bg}" rx="3" />
    <rect x="110" y="23" width="198" height="10" fill="{accent_secondary}" rx="3" opacity="0.9" />
    <text x="340" y="32" class="text-accent" font-size="10px">90%</text>

    <text x="0" y="52" class="text-muted" font-size="10px">REVERSE ENG &amp; CTF</text>
    <rect x="110" y="43" width="220" height="10" fill="{card_bg}" rx="3" />
    <rect x="110" y="43" width="187" height="10" fill="{accent_tertiary}" rx="3" opacity="0.9" />
    <text x="340" y="52" class="text-accent" font-size="10px">85%</text>
  </g>
</g>

<!-- RIGHT PANEL: Databank Grid & Holographic Visualizer -->

<!-- 1. Databank 6-Card Grid (x: 464, y: 62, w: 432, h: 110) -->
<g transform="translate(464, 62)">
  <!-- Card 1: Repos -->
  <g transform="translate(0, 0)">
    <rect width="136" height="50" fill="url(#panel-grad)" rx="5" stroke="{panel_border_dim}" stroke-width="1" />
    <rect x="0" y="0" width="3" height="50" fill="{accent_primary}" rx="1" />
    <text x="12" y="18" class="text-stat-lbl">REPOSITORIES</text>
    <text x="12" y="40" class="text-stat-val" id="repo_data">20</text>
    <text x="105" y="38" font-size="16px">📦</text>
  </g>
  
  <!-- Card 2: Stars -->
  <g transform="translate(148, 0)">
    <rect width="136" height="50" fill="url(#panel-grad)" rx="5" stroke="{panel_border_dim}" stroke-width="1" />
    <rect x="0" y="0" width="3" height="50" fill="{accent_secondary}" rx="1" />
    <text x="12" y="18" class="text-stat-lbl">TOTAL STARS</text>
    <text x="12" y="40" class="text-stat-val" id="star_data">24</text>
    <text x="105" y="38" font-size="16px">⭐</text>
  </g>

  <!-- Card 3: Commits -->
  <g transform="translate(296, 0)">
    <rect width="136" height="50" fill="url(#panel-grad)" rx="5" stroke="{panel_border_dim}" stroke-width="1" />
    <rect x="0" y="0" width="3" height="50" fill="{accent_tertiary}" rx="1" />
    <text x="12" y="18" class="text-stat-lbl">COMMITS</text>
    <text x="12" y="40" class="text-stat-val" id="commit_data">127</text>
    <text x="105" y="38" font-size="16px">⚡</text>
  </g>

  <!-- Card 4: Contributions -->
  <g transform="translate(0, 58)">
    <rect width="136" height="50" fill="url(#panel-grad)" rx="5" stroke="{panel_border_dim}" stroke-width="1" />
    <rect x="0" y="0" width="3" height="50" fill="{accent_secondary}" rx="1" />
    <text x="12" y="18" class="text-stat-lbl">CONTRIBS / PRS</text>
    <text x="12" y="40" class="text-stat-val" id="contrib_data">20</text>
    <text x="105" y="38" font-size="16px">🔀</text>
  </g>

  <!-- Card 5: Followers -->
  <g transform="translate(148, 58)">
    <rect width="136" height="50" fill="url(#panel-grad)" rx="5" stroke="{panel_border_dim}" stroke-width="1" />
    <rect x="0" y="0" width="3" height="50" fill="{accent_primary}" rx="1" />
    <text x="12" y="18" class="text-stat-lbl">FOLLOWERS</text>
    <text x="12" y="40" class="text-stat-val" id="follower_data">5</text>
    <text x="105" y="38" font-size="16px">👥</text>
  </g>

  <!-- Card 6: Rank -->
  <g transform="translate(296, 58)">
    <rect width="136" height="50" fill="url(#panel-grad)" rx="5" stroke="{panel_border_dim}" stroke-width="1" />
    <rect x="0" y="0" width="3" height="50" fill="{accent_primary}" rx="1" />
    <text x="12" y="18" class="text-stat-lbl">SECURITY RANK</text>
    <text x="12" y="40" class="text-stat-val" fill="{accent_primary}">S+ TIER</text>
    <text x="105" y="38" font-size="16px">🛡️</text>
  </g>
</g>

<!-- 2. Holographic Braille Art & Radar Stream Card (x: 464, y: 180, w: 432, h: 260) -->
<g transform="translate(464, 180)">
  <rect width="432" height="260" fill="url(#panel-grad)" rx="6" stroke="{panel_border_dim}" stroke-width="1" />
  
  <!-- Header Bar -->
  <text x="16" y="20" class="text-accent">[+] HOLOGRAPHIC_AVATAR // MONITOR</text>
  <text x="320" y="20" class="micro-text" font-size="9px">FEED: LIVE_STREAM</text>
  <line x1="16" y1="26" x2="416" y2="26" stroke="{panel_border_dim}" stroke-width="1" stroke-dasharray="3 3" />

  <!-- Background Tactical Radar Circles -->
  <g transform="translate(216, 135)" opacity="0.25">
    <circle r="80" stroke="{accent_primary}" stroke-width="1" fill="none" stroke-dasharray="4 4" />
    <circle r="55" stroke="{accent_primary}" stroke-width="0.8" fill="none" />
    <circle r="30" stroke="{accent_secondary}" stroke-width="0.8" fill="none" stroke-dasharray="2 2" />
    <line x1="-90" y1="0" x2="90" y2="0" stroke="{accent_primary}" stroke-width="0.8" />
    <line x1="0" y1="-90" x2="0" y2="90" stroke="{accent_primary}" stroke-width="0.8" />
  </g>

  <!-- Braille Hologram Art -->
  <g class="hologram">
    <text class="art">
{art_svg}
    </text>
  </g>

  <!-- Bottom Data Visualizer Stream -->
  <g transform="translate(16, 212)">
    <rect width="400" height="38" fill="{card_bg}" fill-opacity="{card_bg_opacity}" rx="4" stroke="{panel_border_dim}" stroke-width="0.8" />
    <text x="10" y="14" class="micro-text" font-size="8px" fill="{accent_primary}">CPU_LOAD_STREAM // NET_TRAFFIC_MONITOR</text>
    <g transform="translate(10, 20)">
      {cpu_bars}
    </g>
    <text x="345" y="28" class="text-accent" font-size="9px">99.8% UP</text>
  </g>
</g>

<!-- Full SVG Scanline Overlay -->
<rect width="100%" height="24" class="scan" rx="10" />

</svg>
"""
    
    filename = "dark_mode.svg" if is_dark else "light_mode.svg"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(svg)

if __name__ == '__main__':
    build_svg(True)
    build_svg(False)
    print("HUD SVGs generated successfully!")
