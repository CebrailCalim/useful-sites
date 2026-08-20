# Build scripts

Nothing in this folder is needed to serve the site. `index.html`, `links.js` and
`links.en.js` are the whole site; everything here exists to produce them.

## Adding a link

Write a note in one of the `part_*.py` files:

```python
add('https://example.com/', 'Example', ['open-source', 'python'],
    'Ne yaptigi ve komsularindan nerede ayrildigi.',
    'What it does and where it parts ways with its neighbours.',
    'araclar')
```

Then run `python build.py`.

Tags are drawn from the 63 canonical tags in `tags.py`. A tag that does not match
one of them is looked up in the `ALIAS` table and mapped to a canonical
equivalent; if it maps to nothing, it is dropped.

To mark an entry as a starting point for its category, add its URL to `picks.py`.

`links.js` can be edited directly for a quick fix, but the next build overwrites
it.

## What each script does

| Script | Job |
|---|---|
| `extract.py` | Pulls technology links out of a browser bookmark file and prunes them |
| `check.py` | Checks whether links are alive |
| `fetchmeta.py` | Fetches title/description metadata per site (GitHub API where possible) |
| `notes.py` + `part_*.py` | Curator notes — the actual content |
| `tags.py` | Collapses 357 free-form tags into 63 canonical ones |
| `picks.py` | Entries marked as starting points, a few per category |
| `sources.py` | Where each record came from (own archive / external list) |
| `intros.py` | Category introduction texts |
| `verified.json` | Last-verified date per record; refreshed weekly by CI |
| `build.py` | Merges all of the above into `links.js` and `links.en.js` |
| `ci_check.py` | Link scan and report, for GitHub Actions |
| `ci_github.py` | Archive/staleness audit for linked GitHub repositories |

`meta.json` and `ext_meta.json` are raw fetch output and are not committed. They
are only needed to rebuild from scratch; the published `links.js` is tracked.

## Weekly check

`.github/workflows/link-check.yml` runs every Monday. It opens a single issue
and updates that same issue in later weeks rather than filing a new one.

The report separates four cases:

| Heading | Meaning |
|---|---|
| Dead | 404/410 or no response — replace or remove |
| Suspect | 403/429/503 — likely bot blocking, may open fine in a browser |
| Archived | GitHub repository is read-only; the page returns 200 but maintenance has stopped |
| Stale | No pushes in two years or more |

The last two come from a separate audit (`ci_github.py`). A source can die
without ever returning 404: the `Best-websites-a-programmer-should-visit`
repository, 76k stars, was archived on 1 November 2025, and a link scan cannot
see that.

Run either by hand with `python ci_check.py` or `python ci_github.py`.
