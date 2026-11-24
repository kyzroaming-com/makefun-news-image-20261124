#!/usr/bin/env python3
"""Draw the 24 Nov 2026 world-news front page, 1024x1024 PNG.

Headlines verified against Just Security Early Edition, The Global Eye,
CWEB, Daily Summary and Medium briefs for 24 Nov 2026 (all accessed
24 Nov 2026). No network at run time; output is deterministic.
"""
from PIL import Image, ImageDraw, ImageFont
import textwrap

W = H = 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def font(path, size):
    return ImageFont.truetype(path, size)

img = Image.new("RGB", (W, H), "white")
d = ImageDraw.Draw(img)

# Outer border
d.rectangle([6, 6, W - 7, H - 7], outline="black", width=4)

# Masthead
d.text((512, 52), "THE WORLD TODAY", font=font(BOLD, 74),
       fill="black", anchor="ma")
d.text((512, 128), "TUESDAY  24  NOVEMBER  2026", font=font(BOLD, 34),
       fill="#b00000", anchor="ma")
d.line([(40, 178), (984, 178)], fill="black", width=4)
d.line([(40, 186), (984, 186)], fill="#b00000", width=2)
d.text((512, 196), "Six stories that defined the day  •  Reported 24 November 2026",
       font=font(REG, 22), fill="#333333", anchor="ma")

stories = [
    ("NVIDIA  •  TECH",
     "Huang returns as Nvidia CEO",
     "Board reinstates Jensen Huang after Trump push; shares jump about 30%."),
    ("UKRAINE  •  WAR AT SEA",
     "Ukraine sinks Russian warship in Libya",
     "Naval drones hit a Russian corvette at Benghazi port, Kyiv says."),
    ("IRAN  •  STRAIT OF HORMUZ",
     "Tankers hit mines; Iran refuses talks",
     "Iran says tankers were mined in the strait and it will not negotiate."),
    ("GAZA  •  ISRAEL-HAMAS WAR",
     "Strike kills Hamas security chief",
     "Israeli airstrike kills Naeem Abu Nahel, head of Hamas internal security."),
    ("UKRAINE  •  RUSSIA STRIKE",
     "Zaporizhzhia strike kills 2, wounds 40",
     "Overnight Russian attack hits flats; four children among the wounded."),
    ("CLIMATE  •  COP31",
     "COP31 collapses with no fossil-fuel deal",
     "Climate talks end without agreement on phasing out fossil fuels."),
]

# 2 columns x 3 rows; cards end at 930, footer strip starts at 946
x0s = [40, 532]
y0s = [236, 472, 708]
cw, ch = 452, 222
for i, (kicker, headline, summary) in enumerate(stories):
    x0 = x0s[i % 2]
    y0 = y0s[i // 2]
    # Card
    d.rectangle([x0, y0, x0 + cw, y0 + ch], outline="#999999", width=2)
    d.rectangle([x0, y0, x0 + cw, y0 + 34], fill="#111111")
    d.text((x0 + 12, y0 + 17), kicker, font=font(BOLD, 19),
           fill="white", anchor="lm")
    # Headline, wrapped to fit
    lines = []
    for raw in textwrap.wrap(headline, width=22):
        lines.append(raw)
    y = y0 + 46
    for ln in lines[:3]:
        d.text((x0 + 12, y), ln, font=font(BOLD, 28), fill="black")
        y += 34
    # Summary, wrapped
    y += 2
    for ln in textwrap.wrap(summary, width=36)[:3]:
        d.text((x0 + 12, y), ln, font=font(REG, 20), fill="#222222")
        y += 26

# Footer strip
d.rectangle([40, 946, 984, 1006], fill="#b00000")
d.text((512, 976),
       "ALSO: ICJ finds Myanmar guilty of Rohingya genocide",
       font=font(BOLD, 20), fill="white", anchor="mm")

img.save("entry.png", "PNG", optimize=True)
print("saved entry.png", img.size)
