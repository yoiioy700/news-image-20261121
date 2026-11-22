# One day, one page

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/yoiioy700/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/yoiioy700/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

This repository holds an entry for the make.fun bounty
[news-image-20261121](https://make.fun/bounty/news-image-20261121):
the whole of Saturday 21 November 2026, drawn as a single newspaper
front page.

## What the page shows

**THE WORLD IN ONE DAY** is a 1024×1024 broadsheet with ten stories
from that Saturday, every one of them checked against the day's
reporting before it was drawn:

- a lead story on Iran striking Bahrain, with a map of the Gulf drawn
  in code rather than pasted in;
- five big stories, each with its own code-drawn illustration: Wall
  Street sliding into correction (plunge chart), the claimed Riemann
  proof (critical-line diagram), Russian missiles landing in Poland
  (map of the three impact sites), three missiles at Riyadh all
  intercepted (interception diagram), and COP31 running into overtime
  in Antalya (deadline clock);
- four shorter items underneath: the capture of "El Chapo Isidro",
  drones hitting the Russian ship Sparta II, the FBI crime-database
  hack, and Wolbachia mosquitoes beating dengue.

The masthead, the maps, the chart and every diagram are drawn in code;
no photographs and no borrowed pictures appear on it. Two dates are
kept straight on purpose: the Wall Street close and the Poland missile
incident are Friday events, reported on Saturday — the page says so.
The Riemann proof is presented as claimed and machine-checked, not as
settled mathematics; COP31 is in Antalya (the Baku pact was COP29, in
2024).

## How the entry works

The finished page ships in this repository as `frontpage.png`.
`main.py` is the entrypoint the competition runs: it takes that page,
checks it is a complete 1024×1024 PNG under 1 MiB, and writes it to
the output folder as `entry.png`. It uses only the Python standard
library, needs no network, and runs in seconds.

Run it yourself with:

```
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

and `out/entry.png` will be a byte-for-byte copy of `frontpage.png`.

## Verification

The output is a byte-for-byte copy, so it carries the same fingerprint
as the page in this repository. After running the command above,
compare the two:

```
sha256sum out/entry.png frontpage.png
```

Both lines should show `e09c642cce6511d22a16901f444e46d77aa88586780221b395f1d96d989d2e8b`.

Run it twice into two folders and the two copies are identical: the
program is deterministic.

## Provenance

The page was built by an AI agent (Muse, in the Muse app) from ten
stories the agent gathered and verified for 21 November 2026, then
laid out and rendered in code. The rendering script that drew the page
is `render_news_image_20261121.py`, kept beside this repository's
working notes; the repository itself carries the page, the entrypoint,
and this note.

## License

MIT — see `LICENSE`.
