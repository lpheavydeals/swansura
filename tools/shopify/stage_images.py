"""Staged uploads for product images through the Shopify connector (no API keys needed).

1) python3 tools/shopify/stage_images.py input FILE.webp ...
     -> prints the stagedUploadsCreate `input` JSON (resource IMAGE, POST); file names must be unique,
        e.g. <product-handle>-01.webp (they become the Shopify file names).
2) run stagedUploadsCreate with that input (Shopify connector; ask for url resourceUrl parameters{name value}).
3) python3 tools/shopify/stage_images.py post FILE.webp ...
     -> finds the stagedUploadsCreate result for those file names in any session transcript under
        ~/.claude/projects/-home-user-swansura (main session or helper agents), POSTs each file and prints
        [{"file": path, "resourceUrl": url, "code": http}] for productCreateMedia(originalSource: resourceUrl).
"""
import json, os, subprocess, sys, glob

PROJ = os.path.expanduser("~/.claude/projects/-home-user-swansura")


def staged_input(files):
    return [{"resource": "IMAGE", "filename": os.path.basename(f), "mimeType": "image/webp",
             "httpMethod": "POST", "fileSize": str(os.path.getsize(f))} for f in files]


def walk(o):
    if isinstance(o, str):
        if '"stagedUploadsCreate"' in o and o.lstrip().startswith("{"):
            try:
                yield json.loads(o)
            except Exception:
                pass
    elif isinstance(o, dict):
        for v in o.values():
            yield from walk(v)
    elif isinstance(o, list):
        for v in o:
            yield from walk(v)


def find_targets(names):
    want, found = set(names), {}
    paths = sorted(glob.glob(PROJ + "/**/*.jsonl", recursive=True) + glob.glob(PROJ + "/**/tool-results/*.txt", recursive=True),
                   key=os.path.getmtime)
    for p in paths:
        if p.endswith(".txt"):                 # large tool results saved to a file (whole file = the response)
            try:
                txt = open(p, errors="ignore").read()
            except Exception:
                continue
            if "stagedUploadsCreate" in txt and any(n in txt for n in want):
                try:
                    d = json.loads(txt)
                except Exception:
                    d = None
                for dd in ([d] if isinstance(d, dict) else []) + list(walk(d)):
                    sc = (dd.get("data", dd) if isinstance(dd, dict) else {}).get("stagedUploadsCreate", {})
                    for tg in (sc.get("stagedTargets") or []) if isinstance(sc, dict) else []:
                        n = tg["resourceUrl"].rsplit("/", 1)[1]
                        if n in want:
                            found[n] = tg
            continue
        try:
            lines = open(p, errors="ignore").readlines()
        except Exception:
            continue
        for line in lines:
            if "stagedUploadsCreate" not in line or "x-goog-signature" not in line:
                continue
            if not any(n in line for n in want):
                continue
            try:
                obj = json.loads(line)
            except Exception:
                continue
            for d in walk(obj):
                for tg in d.get("data", {}).get("stagedUploadsCreate", {}).get("stagedTargets", []) or []:
                    n = tg["resourceUrl"].rsplit("/", 1)[1]
                    if n in want:
                        found[n] = tg          # later transcripts / lines win (newest)
    return found


def post(files):
    tg = find_targets([os.path.basename(f) for f in files])
    out = []
    for f in files:
        t = tg.get(os.path.basename(f))
        if not t:
            out.append({"file": f, "error": "no staged target found"})
            continue
        args = ["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}", t["url"]]
        for p in t["parameters"]:
            args += ["-F", f"{p['name']}={p['value']}"]
        args += ["-F", f"file=@{f};type=image/webp"]
        code = subprocess.run(args, capture_output=True, text=True).stdout
        out.append({"file": f, "resourceUrl": t["resourceUrl"], "code": code})
    print(json.dumps(out, indent=1))


if __name__ == "__main__":
    if sys.argv[1] == "input":
        print(json.dumps(staged_input(sys.argv[2:])))
    else:
        post(sys.argv[2:])
