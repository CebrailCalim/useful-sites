# About

## The problem this addresses

A link's name and URL do not tell you what it is. A line reading
`regex101.com` says nothing until the site is opened. Whereas the following
lets a reader decide in seconds whether it is worth opening:

> Explains a regular expression token by token, and its debugger shows exactly
> where a match falls apart.

Every entry in this directory carries that: **what the resource does** and
**where it parts ways with its neighbours.** The second is the substantive
half. Choosing among several tools that address the same problem does not call
for a feature list; it calls for the line along which they differ.

## Attribution

The links were selected and curated by hand. The descriptions, the category
scheme, the tag vocabulary and the site itself were produced with AI assistance
and reviewed before publication.

This matters because of what the directory claims. Each entry carries a
comparative judgement — "lighter than", "unlike", "in exchange for" — and those
judgements are machine-generated and human-reviewed rather than
human-authored. They are grounded in the projects' own documentation and in
metadata retrieved from the sites themselves, not invented, but they remain
judgements. Read them as a starting point rather than a verdict, and file a
correction as an issue where one is wrong.

## Selection

The directory draws on a curated bookmark archive and on several published
compilations. Entries excluded during curation:

- Account-gated dashboards, which are of no use to a reader
- Search engine result URLs
- Personal file shares
- Links that failed a liveness check

Every entry records which source surfaced it, and that source is exposed as a
filter on the site. The distinction is deliberate: entries taken from external
compilations were verified and described here, but they were not held to the
same standard as those reviewed individually, and presenting them as equal
would misrepresent the directory.

## Scope

This is not a "best tools" list. Two or three entries per category are marked
as starting points, which means "begin here if the area is new to you", not
"this is the best available".

## Maintenance

Link directories share a common failure: they rot. After a period, a
significant fraction stops resolving and the collection loses its value.

Three mechanisms work against that.

A weekly scan checks every link and collects failures into a single issue.
Linked GitHub repositories receive a second, separate audit, because a
repository can cease to be maintained without ever returning a 404 — one entry
here is exactly that case: a 76,000-star compilation whose pages still load,
archived in November 2025. A link check cannot detect this; a repository audit
can.

Anything the scan finds dead is marked on the site itself, so a visitor is
warned before following the link rather than after.

Every entry additionally carries a Wayback Machine link, so an entry retains
some value once its target is gone permanently.

## Contributing

The **Submit a Link** control on the site accepts a single entry through a
form, or reads a bookmark export (`.html`, `.json`, `.csv`) and filters out
everything already present, leaving only what is new. The file is parsed in the
browser and uploaded nowhere; there is no server to upload it to.

Submissions open as GitHub issues. Nothing reaches the site automatically: an
issue is read, a description is written, and the entry is included in the next
build if it fits the scope.

The submission form requires a "how does it differ" field. If the answer is not
known, saying so is acceptable and it will be researched — but left empty, the
entry does not carry what the directory exists to provide.

---

*Build scripts, data layout and the procedure for adding an entry:
[data/README.md](data/README.md).*
