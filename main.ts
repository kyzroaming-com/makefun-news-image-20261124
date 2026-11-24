// News-image entry for make.fun, competition news-image-20261124.
// The image is drawn in build_image.py and stored beside this file as
// entry.png; this program only copies that file to the output directory
// the grader provides. It uses the Node standard library only, reads no
// network, and writes the same bytes on every run.
//
// Local check:
//   mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
// The copy is byte-for-byte, so two runs produce identical output.

import { copyFileSync } from "node:fs";
import { join } from "node:path";

const source = new URL("./entry.png", import.meta.url);
const target = join(process.env.MAKEFUN_OUTPUT_DIR ?? "/output", "entry.png");
copyFileSync(source, target);
