# Publishing and repository setup

Repository: **https://github.com/latifkedi/useful-sites**
Live: **https://latifkedi.github.io/useful-sites/**

The site is already published. What follows is the setup that got it there,
plus the settings that still need to be right for the automation to work.

---

## Done

| # | Step | |
|---|---|---|
| 1 | Empty repository created on GitHub | done |
| 2 | Branch renamed `master` → `main` | done |
| 3 | `origin` set to the HTTPS address | done |
| 4 | `REPO` constant in `index.html` pointed at the real repository | done |
| 5 | Pushed | done |
| 6 | Pages enabled | done |

**Why HTTPS and not SSH:** there is an `~/.ssh/id_ed25519.pub` key on the
machine, but it is not registered with the GitHub account — connecting returned
`Permission denied (publickey)`. To switch later, add the key at
[github.com/settings/keys](https://github.com/settings/keys) and change the
remote back.

---

## Settings that must be right

### Actions write permission

Settings → Actions → General → **Workflow permissions** →
`Read and write permissions`.

Two workflows need this. Without it the weekly scan cannot write
`data/verified.json` back, so the "last verified" dates on the site freeze and
dead entries never get marked; and the approval workflow cannot push a branch.

### Labels

The automation keys off four labels. GitHub creates them on first use, but
making them up front means the filters work immediately:

| Label | Used by |
|---|---|
| `new-link` | the "Suggest a link" issue template |
| `broken-entry` | the "Report a broken entry" template |
| `approved` | **you**, to turn a submission into a pull request |
| `link-check` | the weekly maintenance issue |

### About box

Settings sidebar → **About** gear:

- **Description:** `An annotated directory of links on software, AI and security`
- **Website:** `https://latifkedi.github.io/useful-sites/`
- **Topics:** `bookmarks`, `awesome-list`, `directory`, `turkish`, `developer-tools`

Topics measurably help discovery through GitHub search.

---

## The two workflows

### Weekly health check

`.github/workflows/link-check.yml` runs every Monday at 04:17 UTC, and can be
triggered by hand from the Actions tab.

It scans every link, audits the linked GitHub repositories for archival and
staleness, writes fresh verification dates back to `data/verified.json`, and
files the result as a single issue. Later weeks update that same issue rather
than opening a new one.

### Approved submission → pull request

`.github/workflows/approve-link.yml` fires when you add the `approved` label to
an issue that already carries `new-link`.

It reads the issue form, writes the record into `data/part_new.py`, rebuilds,
and opens a pull request. It does not merge. The generated description still
needs a pass — the submitter wrote one language in one voice, so both language
fields start out carrying the same text, and there is a marker comment in the
diff saying so.

If the issue cannot be used — malformed URL, empty required field, or a link
already in the directory — the workflow comments on the issue explaining why
and removes the `approved` label.

---

## Adding a link by hand

1. Write the note into one of `data/part_*.py`
2. Run `python data/build.py`
3. `git add -A && git commit -m "..." && git push`

Pages updates within a minute or two. Details in
[data/README.md](data/README.md).

`build.py` regenerates `links.js`, `links.en.js`, `feed.xml`, `sitemap.xml`,
`robots.txt` and the static pages under `k/`. All of them are committed, so
what is served always matches what was built.

---

## If something goes wrong

| Symptom | Cause and fix |
|---|---|
| Push opens a browser, closes, asks again | Delete the `git:https://github.com` entry from Windows Credential Manager and retry |
| `Permission denied (publickey)` | The remote reverted to SSH. `git remote set-url origin https://github.com/latifkedi/useful-sites.git` |
| Push rejected, `fetch first` | The remote has commits you do not. `git pull --rebase origin main`, then push |
| Pages returns 404 | Wrong branch/folder in the Pages settings, or the deploy has not finished — give it two minutes |
| Site loads but is empty | `links.js` was not pushed. Check with `git status` |
| A workflow is red | Almost always the Actions write permission above |
| Approval workflow does nothing | The issue needs both `new-link` and `approved`. The `new-link` label comes from the template; if the issue was opened without it, add it first |
