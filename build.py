#!/usr/bin/env python3
"""seolmyung-aio-deck — base64 image inliner."""
import base64
import pathlib

ROOT = pathlib.Path(__file__).parent
IMAGES = {
    "{{IMG_ACTIVITY}}": "ga4-activity.png",
    "{{IMG_CHANNELS}}": "ga4-channels.png",
    "{{IMG_EVENTS}}": "ga4-events.png",
}

def b64(name: str) -> str:
    return base64.b64encode((ROOT / name).read_bytes()).decode("ascii")

tpl = (ROOT / "deck.template.html").read_text(encoding="utf-8")
for token, fname in IMAGES.items():
    tpl = tpl.replace(token, b64(fname))
(ROOT / "deck.html").write_text(tpl, encoding="utf-8")
print("built deck.html")
