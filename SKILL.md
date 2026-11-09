---
name: perfect-cv
description: Tailor a person's own CV to a specific job ad, keeping their layout and voice, improving only what makes it match the role. On first use, ask the person to upload their current CV so the look is theirs. Use whenever someone wants a CV or cover letter adapted to a job posting.
---

# Perfect CV

Adapt a person's **own** CV to a specific job, then produce a clean one-page PDF (plus a
matching cover letter if they want one). The layout and voice stay theirs. Only the
content changes, and only to make a genuine, truthful match with the ad. No templated
look forced on them, no invented experience, no robotic phrasing.

## First message: get their CV

If no CV layout has been captured yet in this conversation, the first thing to do is ask
the person to **upload their current CV** (PDF or Word), so the result keeps their design:

> "Upload your current CV (PDF or Word) and I'll use your own layout. Then paste the job
> ad you're aiming for."

Only if they have no CV at all, offer to start from the neutral default in
`templates/` and build one with them.

## Capture their layout (once)

When the CV arrives, read it (use the PDF/Word reading tools) and rebuild it as clean,
self-contained HTML that **mirrors their design**: the same section order, headings,
fonts where reproducible, spacing and overall feel. Pull their real content into it
verbatim. Render it once and show it back:

> "Here's your CV rebuilt so I can tailor it. Does this match your layout?"

Fix anything off, then save this HTML as their working template for the rest of the chat.
This captured layout, not any bundled theme, is what every tailored version is built on.

## Per job: tailor, don't rewrite the person

For each job ad:

1. Read the ad. Note the role, the must-have requirements, and the words it repeats.
2. In their captured layout, adjust content to match:
   - Reframe the summary toward this role.
   - Surface the skills and bullet points the ad cares about; de-emphasize the rest.
   - Mirror the ad's vocabulary where it honestly fits what they've done.
   - Keep every real company, role, date and location exactly as in their CV.
3. Render to PDF and check it is one page (or matches their CV's length). Show the preview.
4. If they want a cover letter, write 3-4 short paragraphs in their voice: a hook, the
   relevant experience, the practical fit (availability, location), a warm close.

## The two rules that matter

- **No lies.** Never add experience, tools, certificates, degrees or dates they don't
  have. Tailoring is reordering, reframing and emphasis, not invention. If the ad hard-
  requires something they lack, tell them plainly instead of faking it; help them make
  the honest best case. If a posting looks like a scam or could expose them to harm,
  flag it rather than help them apply.
- **No robotic writing.** Plain, human sentences in their own register. No em-dashes, no
  "I am excited to leverage", no filler. If their CV has a voice, keep it.

## Rendering

```
python scripts/render.py embed photo.jpg          # photo -> data: URI, if their CV has one
python scripts/render.py build cv.html  Name_CV.pdf   # HTML -> verified one-page PDF + preview
```

Name delivered files by the general role family (e.g. `Name_Reception_CV.pdf`) so one
tailored CV can be reused for similar ads. For a new ad in the same family, keep the CV
and only redo the cover letter.

## Dependencies

```
pip install weasyprint pdfplumber pdf2image
```
WeasyPrint needs Pango/Cairo; the preview needs Poppler. The page-count and preview
steps are optional; rendering works without them.

## Files

- `scripts/render.py` — embed a photo as a data URI; build HTML into a verified PDF + preview.
- `templates/default_resume.html`, `templates/default_cover.html` — a neutral fallback
  design, only for someone who has no CV to upload. The real layout comes from their file.
