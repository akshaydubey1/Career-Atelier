---
name: akshay-dubey-resume-tailor
description: Resume Tailor by Akshay Dubey. Use when someone shares a job description or job link to check their fit, reuse or tailor their resume, and get resume and cover letter PDFs, or when they ask to see their saved job list.
license: MIT
metadata:
  author: Akshay Dubey
  homepage: https://github.com/akshaydubey1
  version: "1.0.0"
---

# Resume Tailor

Created by **Akshay Dubey** · github.com/akshaydubey1 · MIT License

This skill helps any job seeker apply smarter, in any AI tool that supports Agent Skills. It scores a job against the user's existing resumes and then takes the cheapest path that works:

| Best match | What happens |
| --- | --- |
| 85% or more | Reuse that resume as is. No tailoring. Write the cover letter only. |
| 75–84% | Tailor the best resume up to 85% or more, then write the cover letter. |
| Below 75% | Stop with a blunt verdict. Nothing else. |

Spend as little effort as possible. Never redo work that already exists. Never invent experience.

## 0. Check what this tool can do (silently, once per session)

Pick the mode from the abilities you actually have. Don't ask the user about it.

| Mode | When | What you deliver |
| --- | --- | --- |
| **Full** | You can read and write files and run Python | PDFs with exact formatting and a saved library |
| **Files only** | You can read and create files, but not run code | A tailored .docx or PDF made with whatever document tools you have, plus a saved library if possible |
| **Chat only** | No file or code access | The score and verdict, plus the tailored resume text and cover letter text, ready to paste |

In **Chat only** mode, say once in a single line that the user needs a tool with file and code access for exact formatting and PDFs. Then continue.

**Where the library lives**, in order of preference:
1. A folder on the user's computer you can reach (directly, or through the tool's computer or file connection). Default: `~/Documents/Resumes/`.
2. The tool's project or workspace storage.
3. Nowhere (Chat only mode). Ask the user to paste their saved resumes when needed.

## 1. First-run setup (once per user)

If `settings.json` isn't in the library yet, ask these in **one** message and save the answers:

1. **Base resume:** "Attach your current resume as a .docx." A PDF or pasted text works for scoring, but keeping exact formatting needs a .docx.
2. **Library folder:** default `~/Documents/Resumes/`. Accept any path.
3. **Years of experience to state in the summary:** default is what the resume shows. Use the user's figure only if the resume supports it.

Read the user's full name from the resume header. Don't ask for it.

`settings.json` holds: `fullName`, `personCode` (section 9), `folder`, `yearsOfExperience`, `created`.

## 2. The resume library

- `Base_Resume.docx`: the master. **Never edit it.**
- Each tailored resume as a `.docx` and `.pdf` pair, named per section 9.
- `index.json`: one entry per resume with `file`, `company`, `role`, `date`, `keywords` (the skills and tools that resume proves) and `jdKeywords` (the job's terms it was made for).
- `jobs.csv`: the private job list (section 10).
- `settings.json`
- **Cover letters are never stored.** Each one is created, handed to the user, and then deleted.

## 3. Read the job

Use the pasted job description, or fetch the link if you can browse. If you can't, ask the user to paste the text.

Extract the company, role, location, salary or rate, sponsorship terms and work terms (W2/C2C, onsite days).

Build a requirement list and tag each item:
- **must-have**: required, minimum, "strong hands-on", "proficiency in"
- **nice-to-have**: preferred, "a plus", bonus

## 4. Score against the library (cheap first)

1. **Pre-screen with `index.json` only.** Don't open resume files yet. Match the requirement list against each entry's `keywords` and pick the top 1–2 candidates. The base resume is always one of them.
2. If the same company and role is already indexed, show it and ask whether to reuse it or redo it.
3. **Fully score only the top candidate(s).** Read the resume text and score each requirement:
   - 1.0 = shown in real work, with a concrete bullet
   - 0.5 = adjacent or partial (a similar tool, or evidence only from a certification, course or personal project)
   - 0 = not there

**Match % = (sum of must-have scores × 2 + sum of nice-to-have scores) ÷ (must-have count × 2 + nice-to-have count) × 100**, rounded to a whole number.

Check the arithmetic. Score strictly: when unsure, take the lower score.

## 5. Decide the path

### Below 75%: hard stop
Do not tailor, write a cover letter, draft messages, add to the job list, or suggest courses or projects. Reply with only:

1. `Match: NN% — skip this one.`
2. The 2–3 dealbreakers, one line each: the requirement and the plain fact that it's missing.
3. One blunt sentence on why applying is a poor use of their time.

Be honest and direct, under ~80 words, with no softening. If the user says "proceed anyway" or confirms experience that isn't on the resume, rescore with it.

### 85% or more: reuse, no tailoring
Copy that resume to the new file name (section 9) without changing its content. Run section 11 on the copy. Add an `index.json` entry. Go to step 7.

### 75–84%: tailor (step 6)

## 6. Tailor to 85% or more

Start from a copy of the best-scoring resume's .docx. Never edit the base.

- Raise the score only by surfacing real experience:
  - move the relevant bullets up
  - use the job's exact terms where the experience truly matches ("GKE" vs "Kubernetes", "CI/CD" vs "pipelines")
  - turn under-described experience into explicit bullets
  - add skills the user has actually used
- Write the summary with the years of experience from settings and the role's top three must-haves the user meets.
- **Never invent** employers, titles, dates, degrees, metrics, tools or certifications, even to reach 85%. Keep certifications, courses and personal projects in their own sections, never presented as work experience.
- Rescore. If an honest score can't reach 85%, deliver the best honest version and list the requirements holding it back, one line each.
- Keep the same page count as the source resume.

**Preserve formatting (non-negotiable).** Edit the copied .docx in place with python-docx: change the text inside existing runs and paragraphs, and keep fonts, sizes, bold and italic, spacing, margins, bullet styles and section order. To add a bullet, copy an existing bullet paragraph's XML and replace its text. Never rebuild the document or change fonts.

Then run `scripts/finalize.py` (section 11) to make the PDF. Check page 1 and the page count. Save the .docx and .pdf to the library and add the `index.json` entry.

## 7. Cover letter (75% or more only)

- About 250–330 words in 3–4 paragraphs, written in the user's first person.
- Use the resume's font family and the same name and contact header, and sign it with the user's full name.
- Name the company and role, and make one specific, verified point about the company.
- Give 2–3 concrete proof points tied to the top must-haves, and close with a simple, low-key ask.
- Build it as a .docx in a temporary location (never the library) and run `scripts/finalize.py <file> "<Full Name>" cover`. Hand over the PDF, then **delete both the .docx and the PDF from the temporary location**.

## 8. Output (75% or more only)

- Hand over exactly two PDFs: the resume and the cover letter. Use the tool's normal way of giving files to the user, or save them to the library folder and give the paths.
- Reply in 3–4 lines: the path taken (reused or tailored), the match % before → after, any remaining gaps, and the two file names.
- Don't mention the job list.

## 9. File names (exact)

**Person code + company code + document code**, with no spaces, underscores or dates.

- **Person code:** first name + last-name initial. Akshay Dubey → `AkshayD`, Maria Lopez → `MariaL`.
- **Company code:** 2 uppercase letters.
  - One word: its first and last letters. Perfect → `PT`, Google → `GE`, Vanguard → `VD`.
  - Two or more words: the first letters of the first two words. Capital One → `CO`, Bank of America → `BO`.
  - Ignore Inc, LLC, Corp and Technologies.
- **Document code:** `R` for the resume, `CL` for the cover letter.

Example: Akshay Dubey applying to Perfect gets `AkshayDPTR.pdf` and `AkshayDPTCL.pdf`.

If a resume name already exists for a different role at the same company, add a hyphen and the role's first letter (`AkshayDPTR-S.pdf`).

## 10. Private job list

**Only jobs that scored 75% or more are added.**

After step 8, silently add one row to `jobs.csv` (create it with a header row if it's missing). Don't announce it or show it.

| Column | What goes in it |
| --- | --- |
| Company | As posted (the end client if the posting names one) |
| Position | Job title as posted |
| Location | City, state and work mode, e.g. `Plano, TX — hybrid, 3 days onsite` or `Remote (US)` |
| Salary | As posted, or `Not mentioned` |
| Sponsorship | `Yes`, `No`, or `Not mentioned` |
| Comment | One line: match % before → after, reused or tailored, resume file name, date added, and key terms (e.g. `W2 only`) |

- Sponsorship comes only from the posting text. Never guess. "W2 only" alone isn't a `No`.
- If the same company and position already exists, update that row instead of adding a new one.
- **Show the list only when asked** ("show my jobs", "job list"). Display it as a table, newest first. Hand over the CSV only if the user asks for the file.
- In Chat only mode there's no file to keep the list in, so skip this section.

## 11. The user's name only, no tool trace

Everything produced belongs to the user and carries only their name.

- **Run `scripts/finalize.py <file.docx> "<Full Name>" <resume|cover>` on every document.** It:
  - sets the .docx author and last-modified-by to the user's name, and sets the title
  - converts to PDF with LibreOffice, or with Microsoft Word through docx2pdf if LibreOffice isn't installed
  - replaces all PDF metadata, including the XMP block, with only the user's name and the title
- The script installs `python-docx`, `pikepdf` and `docx2pdf` itself if they're missing. If neither LibreOffice nor Word is installed, tell the user in one line to install LibreOffice (it's free).
- Without Python (Files only mode), set the author and title with whatever document tools you have, and remove any other author or producer fields.
- **Content:** no mention of AI, assistants, "generated" or any tool name anywhere. That includes file names, headers, footers, hidden text, and the CSV and JSON files.
- **Voice:** plain and direct, with varied sentence length. Avoid "delve", "leverage" as a verb, "passionate about", "in today's fast-paced", "I am excited to", "proven track record", "seamless", stacked adjectives and heavy em-dash use.
- **Honesty is not optional.** Removing tool traces never means adding claims. Every line must stay true to the user's real experience.
