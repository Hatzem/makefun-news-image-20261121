# Entry program: copies the pre-rendered entry.png into the output dir.
# stdlib only; no network. Runs twice with byte-identical output.
import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
shutil.copyfile(os.path.join(here, "entry.png"),
                os.path.join(out, "entry.png"))
