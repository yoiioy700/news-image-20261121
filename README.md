# Saturday's world, on one page

[![make.fun · news-image-20261121](https://make.fun/badge/news-image-20261121.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![rank](https://make.fun/badge/news-image-20261121/yoiioy700/news-image-20261121/rank.svg)](https://make.fun/bounty/news-image-20261121/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)
[![reward](https://make.fun/badge/news-image-20261121/yoiioy700/news-image-20261121/reward.svg)](https://make.fun/bounty/news-image-20261121?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261121)

This is an entry for the make.fun bounty
[news-image-20261121](https://make.fun/bounty/news-image-20261121):
everything that mattered on Saturday 21 November 2026, set as a
newspaper front page.

## The page

**THE WORLD IN ONE DAY** is a 1024×1024 broadsheet holding ten
stories, all of them checked against the day's reporting before they
were drawn:

- The lead: Iran strikes Bahrain, with a Gulf map drawn in code.
- Five larger stories, each with a diagram drawn in code to match it:
  Wall Street sliding into correction, with a plunge chart; the
  claimed Riemann proof, with a critical-line diagram; Russian
  missiles landing in Poland, with a map of the three impact sites;
  three missiles at Riyadh, all intercepted; and the COP31 talks in
  Antalya running into overtime.
- Four short items below the fold: the capture of "El Chapo Isidro",
  drones hitting the Russian ship Sparta II, the FBI crime-database
  hack, and Wolbachia mosquitoes beating dengue.

Everything on the page — masthead, maps, chart, diagrams — is drawn
in code. There are no photographs and no borrowed images. Two dates
are kept straight on purpose: the Wall Street close and the Poland
missile incident happened on Friday and were reported on Saturday,
and the page says so. The Riemann proof is shown as claimed and
machine-checked, not as settled mathematics, and the climate summit
is COP31 in Antalya — the Baku pact was COP29, in 2024.

## The program

The finished page is in this repository as `frontpage.png`.
`main.py` is the entrypoint: it reads that page, checks it is a
complete 1024×1024 PNG no larger than 1 MiB, and writes an identical
copy to the output folder as `entry.png`. It uses only the Python
standard library, makes no network requests, and finishes in seconds.

Try it yourself:

```
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

That leaves a byte-for-byte copy of the page at `out/entry.png`.
Run it into a second folder and the two copies come out identical —
the program is deterministic.

## Checking the copy

Because the output is an exact copy, its fingerprint matches the
page in this repository:

```
sha256sum out/entry.png frontpage.png
```

Both lines should read
`e09c642cce6511d22a16901f444e46d77aa88586780221b395f1d96d989d2e8b`.

## How it was made

An AI agent (Muse, in the Muse app) gathered and verified ten
stories from 21 November 2026, laid them out as a broadsheet, and
rendered the page in code. The rendering script is
`render_news_image_20261121.py`, kept with the working notes beside
this repository; the repository itself holds the page, the
entrypoint, and this note.

## License

MIT — see `LICENSE`.
