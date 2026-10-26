"""Helper for pushing theme files through Shopify staged uploads (connector session use).

1) python3 tools/theme/stage_upload.py input FILE...   -> prints the stagedUploadsCreate `input` JSON
2) run stagedUploadsCreate with that input (Shopify connector)
3) python3 tools/theme/stage_upload.py post TRANSCRIPT.jsonl
   -> finds the latest stagedUploadsCreate result in the session transcript, POSTs each file
      (paths relative to theme/), prints themeFilesUpsert `files` JSON (body type URL)
4) run themeFilesUpsert with those files; check checksums (sections with schema errors fail
   silently in URL mode, so re-send a failing file as TEXT to see the error).
"""
import json
import os
import subprocess
import sys

THEME = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "theme")


def staged_input(files):
    return [{"resource": "FILE", "filename": f.replace("/", "__") + ".txt", "mimeType": "text/plain",
             "httpMethod": "POST", "fileSize": str(os.path.getsize(os.path.join(THEME, f)))} for f in files]


def latest_targets(transcript):
    found = None
    for line in open(transcript):
        if '\\"stagedUploadsCreate\\"' in line and "x-goog-signature" in line and '"tool_result"' in line:
            found = json.loads(line)

    def walk(o):
        if isinstance(o, str):
            if o.lstrip().startswith('{"data":{"stagedUploadsCreate"'):
                yield o
        elif isinstance(o, dict):
            for v in o.values():
                yield from walk(v)
        elif isinstance(o, list):
            for v in o:
                yield from walk(v)

    return json.loads(next(walk(found)))["data"]["stagedUploadsCreate"]["stagedTargets"]


def post(transcript):
    out = []
    for tg in latest_targets(transcript):
        fn = tg["resourceUrl"].rsplit("/", 1)[1][:-4].replace("__", "/")
        args = ["curl", "-sS", "-o", "/dev/null", "-w", "%{http_code}", tg["url"]]
        for p in tg["parameters"]:
            args += ["-F", f"{p['name']}={p['value']}"]
        args += ["-F", f"file=@{os.path.join(THEME, fn)};type=text/plain"]
        code = subprocess.run(args, capture_output=True, text=True).stdout
        print(code, fn, file=sys.stderr)
        out.append({"filename": fn, "body": {"type": "URL", "value": tg["resourceUrl"]}})
    print(json.dumps(out))


if __name__ == "__main__":
    if sys.argv[1] == "input":
        print(json.dumps(staged_input(sys.argv[2:])))
    else:
        post(sys.argv[2])
