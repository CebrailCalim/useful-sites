Closes #ISSUENO

Written by `data/from_issue.py` from the submitted issue form.

**Before merging, the description needs a pass.** The submitter wrote one
language in one voice, so the Turkish and English fields currently carry the
same text, and the "how does it differ" half may need sharpening. There is a
marker comment above the new entry in `data/part_new.py`.

Check the category and tags as well: the category comes from the form's
dropdown, and any tag that did not match the canonical table in `data/tags.py`
was dropped rather than guessed at.
