from pathlib import Path

exts = {".png", ".jpg", ".jpeg", ".webp"}

imgs = sorted(
    [p.name for p in Path(".").iterdir() if p.suffix.lower() in exts]
)

with open("README.md", "w") as f:
    f.write("# Wallpapers\n\n")
    f.write("<p align=\"center\">\n")

    for img in imgs:
        f.write(f'  <img src="{img}" width="30%" alt="{img}">\n')

    f.write("</p>\n")
