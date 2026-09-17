#!/usr/bin/env python3
import json
import os
import subprocess
import time
import urllib.request
from pathlib import Path
from websocket import create_connection

PORT = 9222
ROOT = Path(__file__).resolve().parents[1]


def cdp(ws, method, params=None, ident=[0]):
    ident[0] += 1
    ws.send(json.dumps({"id": ident[0], "method": method, "params": params or {}}))
    while True:
        msg = json.loads(ws.recv())
        if msg.get("id") == ident[0]:
            return msg


def measure(url, width, height):
    browser = subprocess.Popen([
        "chromium", "--headless", "--no-sandbox", "--disable-gpu",
        "--disable-background-networking", "--disable-component-update",
        "--remote-debugging-port=%d" % PORT, "--remote-allow-origins=*", "--window-size=%d,%d" % (width, height),
        "--user-data-dir=/tmp/ts-cls-%d" % width,
    ], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    try:
        for _ in range(40):
            try:
                targets = json.load(urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json/list"))
                target = next(t for t in targets if t.get("type") == "page")
                break
            except Exception:
                time.sleep(0.1)
        ws = create_connection(target["webSocketDebuggerUrl"], suppress_origin=True)
        cdp(ws, "Page.enable")
        cdp(ws, "Runtime.enable")
        cdp(ws, "Emulation.setDeviceMetricsOverride", {"width": width, "height": height, "deviceScaleFactor": 1, "mobile": width < 768})
        cdp(ws, "Page.addScriptToEvaluateOnNewDocument", {"source": "window.__cls=[]; new PerformanceObserver(list=>{for(const e of list.getEntries()){if(!e.hadRecentInput){window.__cls.push({v:e.value,t:e.startTime,s:e.sources?.map(x=>x.node?.tagName+'.'+x.node?.className).slice(0,5)})}}}).observe({type:'layout-shift',buffered:true});"})
        cdp(ws, "Page.navigate", {"url": url})
        time.sleep(4)
        # Scroll through the page to exercise lazy rendering and content-visibility without user input.
        for y in range(0, 12000, 800):
            cdp(ws, "Runtime.evaluate", {"expression": f"scrollTo(0,{y})"})
            time.sleep(0.12)
        time.sleep(0.5)
        result = cdp(ws, "Runtime.evaluate", {"expression": "JSON.stringify({cls:__cls.reduce((a,e)=>a+e.v,0), entries:__cls})", "returnByValue": True})
        payload = json.loads(result["result"]["result"]["value"])
        print(json.dumps({"url": url, "viewport": [width, height], **payload}, separators=(",", ":")))
        ws.close()
    finally:
        browser.terminate()
        browser.wait(timeout=5)


if __name__ == "__main__":
    base = os.environ.get("CLS_BASE_URL", "http://127.0.0.1:8000").rstrip("/")
    for viewport in ((1365, 900), (390, 844)):
        for route in ("/", "/one-piece-tcg.html", "/one-piece-tcg-cards.html"):
            measure(base + route, *viewport)
