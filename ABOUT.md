# About

This directory came out of a browser bookmark archive that had been growing for
years.

There were a little over two thousand bookmarks in it. Most had never been
opened twice, a fair number were already dead, and working out what any of them
was meant opening it. The folder names did not help either: thirty links under
"Tools" tells you nothing about which tool does what.

The real problem was not that the bookmarks were untidy. It was that **a link's
name and URL do not tell you what it is.** A line reading `regex101.com` says
nothing until you open the site. Whereas if you knew this, you could decide in
a second whether it was worth opening:

> Explains a regular expression token by token, and its debugger shows you
> exactly where a match falls apart.

Every entry here carries that. Two things: **what it does** and **where it
parts ways with its neighbours.** The second is the real one. Choosing between
five tools that do the same job does not call for a feature list, it calls for
the line where they diverge.

## Who wrote what

The archive is the owner's, collected by hand over years. The links, the taste
behind them, and the decision about what belongs in a public directory are his.

The descriptions, the categories, the tag vocabulary and the site were written
by an AI working from that archive and from each project's own documentation.
He reviewed the output; he did not write seven hundred descriptions by hand.

This is worth stating plainly because of what the directory claims to be. Every
entry carries a comparative judgement — "lighter than", "unlike", "in exchange
for" — and those judgements are a machine's, checked by a person rather than
formed by one. They are grounded in the projects' own documentation and in
metadata fetched from the sites themselves, not invented, but they are still
judgements. Read them as a starting point, not a verdict.

If one is wrong, say so in an issue. That correction is worth more here than
anywhere else.

## How it was narrowed down

Of the 2294 bookmarks in the raw archive, 634 were technology-related. From
those:

- Account-gated dashboards were removed — an AWS console link helps nobody
- Google search queries were removed
- Personal file shares were removed
- Dead links were scanned for and dropped

An external compilation was then added on top. Those entries are marked
separately, because they are not held to the same standard: the ones from the
personal archive were gone through individually, and the same cannot be claimed
for the imported ones.

## What it does not claim

This is not a "best tools" list. Two or three entries per category are marked
as starting points, but that means "look here first if you are new to this
area", not "this is the best one".

## Against rot

Link lists share a fate: they rot. After a while half of them stop opening and
the list loses its point.

Three things push back on that.

A weekly scan checks every link and collects the failures in a single issue.
GitHub repositories get a second, separate audit — because a repository can die
without ever returning a 404. One entry here is exactly that case: a 76k-star
compilation whose page still loads fine, archived in November 2025. A link scan
cannot see that; a repository audit can.

Anything the scan finds dead is marked on the site itself, so a visitor is
warned before clicking rather than after.

And every entry carries an archive link to the Wayback Machine. When a site
finally goes for good, the entry does not lose all of its value.

## Contributing

The **Submit a Link** button on the site does two things: sends a single link
through a form, or reads a bookmark export (`.html`, `.json`, `.csv`) and
filters out everything already in the directory, leaving only what is new. The
file never leaves your browser — there is no server to upload it to.

What you send opens as a GitHub issue. It does not appear on the site by
itself. It gets read first, a description gets written, and it goes in on the
next build if it fits.

The submission form has a required "how does it differ" field. If you do not
know, write that you do not know and it will be looked into — but left empty,
the entry does not carry what the directory exists for.

---

*Build scripts, the data layout and how to add a link:
[data/README.md](data/README.md).*
