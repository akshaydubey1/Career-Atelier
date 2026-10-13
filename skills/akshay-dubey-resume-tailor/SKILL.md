---
name: akshay-dubey-resume-tailor
description: Resume Tailor by Akshay Dubey. Use when someone shares a job description or job link to check their fit, reuse or tailor their resume, and get resume and cover letter PDFs, or when they ask to see their saved job list.
license: MIT
metadata:
  author: Akshay Dubey
  homepage: https://github.com/akshaydubey1
  version: "1.2.1"
---

# Resume Tailor

Created by **Akshay Dubey** · github.com/akshaydubey1 · MIT License

This skill helps any job seeker apply smarter, in any AI tool that supports Agent Skills. It scores a job against the user's existing resumes and then takes the cheapest path that works:

| Best match | What happens |
| --- | --- |
| 85% or more, on a resume this skill already tailored | Reuse it as is. Write the cover letter only. |
| 50–84% (or any untailored resume) | Full tailoring: build the strongest honest resume for this job, aiming for 85% or more, then write the cover letter. |
| Below 50% | Stop with a blunt verdict. Nothing else. |

Save effort on scoring and reuse. Spend it on making the tailored resume excellent. Never invent experience.

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

### Below 50%: hard stop
Do not tailor, write a cover letter, draft messages, add to the job list, or suggest courses or projects. Reply with only:

1. `Match: NN% — skip this one.`
2. The 2–3 dealbreakers, one line each: the requirement and the plain fact that it's missing.
3. One blunt sentence on why applying is a poor use of their time.

Be honest and direct, under ~80 words, with no softening. If the user says "proceed anyway" or confirms experience that isn't on the resume, rescore with it.

### 85% or more, and the resume already passed the quality bar: reuse
Use this path only if the resume was made by this skill earlier (it has an `index.json` entry) and was tailored for a role with the same title family. Copy it to the new file name (section 9) without changing its content. Run section 11 on the copy. Add an `index.json` entry. Go to step 7.

The base resume, or any resume not made by this skill, always goes through step 6, even at 85% or more.

### 50–84% (or 85%+ that can't be reused): full tailoring (step 6)

## 6. Tailor: build the strongest honest resume for this job

The goal is a resume a recruiter shortlists in a 10-second scan and an ATS ranks near the top, while every line stays true. The target is 85% or more. Work through all seven stages. Don't skip any for speed.

### 6a. Decode the job
- Write down, for your own use: the role's core problem (what this hire is expected to fix or own), the top 5 must-haves in order of importance, the seniority signals (lead, mentor, strategy, ownership), and the domain (industry, regulated or not, scale).
- Build the **keyword list**: every tool, platform, practice and certification the posting names, with the exact spelling it uses and common variants (`CI/CD` = `pipelines`, `IAM` = `identity and access management`, `EKS` = `Amazon EKS`).

### 6b. Map the evidence
- For each must-have and nice-to-have, find the strongest proof across the source resume, the user's other resumes in the library, and experience the user has confirmed. Strongest means production work, with scope or a number, in the most recent role.
- Mark each requirement: **proven** (strong bullet exists), **buried** (true but weak, vague, or in an old role or the skills list only), or **gap** (no real evidence).
- For each **gap**, look up its equivalents in `references/tech-map.md` (section 2). If the user has an equivalent tool, the requirement is framed through the shared concept (6d), never claimed.
- If a must-have is a gap but the user might have it, ask about it in **one** batched question before writing (e.g. "Have you written AWS IAM policies, used Harness, or worked on migrations?"). If the user isn't present to answer, proceed without it.

### 6c. Rewrite, top to bottom
1. **Title line under the name:** match the posting's title family if it truthfully describes the user's work (`Senior Platform Engineer` for a platform role). Never claim a level the user hasn't held.
2. **Summary (3–4 lines):** years of experience from settings; the role's top 3 must-haves, each with one proof point or number; one line on the kind of impact this role needs (e.g. reliability at scale, secure self-service platforms). No generic adjectives.
3. **Skills:** reorder the categories so the posting's must-haves come first. Use the posting's exact terms where true. Remove skills irrelevant to this job if space is needed. Never add a skill the user hasn't used.
4. **Experience bullets**, for each role:
   - Order bullets by relevance to this job; the most relevant goes first.
   - Each bullet follows **action verb + what was done + tools + measurable result or scope**. Example: "Built least-privilege IAM roles for 200+ EKS environments with Terraform, removing standing admin access."
   - Turn every **buried** requirement into a clear bullet in the most recent role where it's true.
   - Every must-have the user meets appears in **at least one experience bullet**, not only in the skills list, using the posting's term.
   - Cut or merge bullets with no relevance to this job to make room. The most recent role gets 5–7 bullets, older roles 2–4, and roles over 10 years old 1–2.
   - Keep every existing number. Never invent a metric. When there's no number, use scope (environments, users, repositories, teams, traffic).
   - Vary the verbs and don't start two bullets in a row with the same one.
5. **Certifications and education:** put certifications this job values first. Keep labels like "previously held" and "coursework" exactly honest.

### 6d. Technology intelligence (applies to every edit in 6c)
Read `references/tech-map.md` before editing. Every technology you add, move or rename must pass all five tests:

1. **Ecosystem fit:** it belongs to the stack that role actually used. EKS goes with IAM roles, IRSA and CloudFormation; AKS goes with Entra ID and Bicep; GKE goes with Workload Identity. Never mix clouds inside one bullet unless the role truly spanned them, and then say so plainly.
2. **Timeline fit:** it existed during that role. Build a `roles.json` of each role's start year, end year and every technology in its bullets, then run `python scripts/tech_check.py roles.json`. Fix every FAIL. Verify any UNKNOWN yourself. Use the current year as the end of an ongoing role.
3. **Placement:** a technology goes in the role where the user actually used it. Never move a tool into an older or newer role to fill a gap there.
4. **Depth:** where the user's real experience is deep, show the specifics that prove it (tech-map section 3), such as IRSA, permission boundaries or drift detection, not vague labels.
5. **Precision:** use the vendor's correct, current name and spelling (tech-map section 4). Mirror the posting's exact term once where it truly matches. Never use a buzzword the bullet can't back up.

**Gaps through equivalents.** When the posting names a tool the user hasn't used but they've used an equivalent, keep their real tool and describe the shared concept in the posting's words. Example: for a Harness posting, write "Built CI/CD pipelines with staged approvals, automated rollback and canary releases (Jenkins, GitHub Actions)." Never write "Harness" in experience or skills unless the user has used it.

**Make the story add up.** Read the finished experience section as a technical interviewer would. Each role should describe one believable system: its scale, the stack that ran it, how it was deployed, secured and observed. If a bullet reads like a keyword placed for the ATS rather than work someone did, rewrite or remove it.

### 6e. Keep the format and make it ATS-safe
- **Preserve formatting (non-negotiable).** Edit a copy of the source .docx in place with python-docx: change the text inside existing runs and paragraphs, and keep fonts, sizes, bold and italic, spacing, margins, bullet styles and section order. To add a bullet, copy an existing bullet paragraph's XML and replace its text. Never rebuild the document or change fonts.
- Keep the same page count as the source (2 pages at most for 10+ years, 1 page under 5 years).
- Run `scripts/finalize.py` (section 11) to make the PDF.
- **ATS check on the PDF:** extract the text (`pdftotext`) and confirm:
  - the name, email and phone come out as plain text at the top
  - section headings are standard (Summary, Skills, Experience, Education, Certifications)
  - dates read in one consistent format
  - every keyword from 6a that the user truly has is found in the extracted text
  - no text is lost to tables, text boxes, headers or footers

### 6f. Quality review (fresh eyes)
Review the PDF as a demanding recruiter for this exact role would. If you can start a separate reviewer (a sub-agent that hasn't seen your work), give it the job posting and the PDF and ask it to grade. Otherwise, reread it cold yourself.

Grade each item pass or fail:

| Check | Pass when |
| --- | --- |
| 10-second scan | The title line, summary and first bullet of the latest role together show this person fits this job |
| Must-have coverage | Every must-have the user meets appears in an experience bullet using the posting's term |
| Evidence | At least 70% of bullets carry a number or a clear scope |
| Relevance | No bullet in the latest role is irrelevant to this job |
| Honesty | Every claim traces to the source resume or something the user confirmed |
| Tech coherence | All five 6d tests pass, `tech_check.py` shows 0 FAIL, and each role reads as one believable stack |
| Voice | No filler phrases (section 11), no repeated verb openers, no keyword lists inside bullets |
| ATS | Every check in 6e passes |
| Layout | Same fonts, spacing and page count as the source, and nothing overflows |

Fix every fail, then grade again. Don't deliver until all checks pass, except where an honest gap makes a check impossible.

### 6g. Rescore and save
- Rescore with the section 4 formula. If an honest score is still below 85%, deliver the strongest honest version anyway and list the requirements holding it back, one line each.
- Save the .docx and .pdf to the library and add the `index.json` entry.

## 7. Cover letter (50% or more only)

- About 250–330 words in 3–4 paragraphs, written in the user's first person.
- Use the resume's font family and the same name and contact header, and sign it with the user's full name.
- Name the company and role, and make one specific, verified point about the company.
- Give 2–3 concrete proof points tied to the top must-haves.
- If a must-have is a real gap, address it in one honest sentence that points to the closest related experience. Never claim the missing skill.
- Close with a simple, low-key ask.
- Build it as a .docx in a temporary location (never the library) and run `scripts/finalize.py <file> "<Full Name>" cover`. Hand over the PDF, then **delete both the .docx and the PDF from the temporary location**.

## 8. Output (50% or more only)

- Hand over exactly two PDFs, the resume and the cover letter, as **two separate files, each ready to download on its own**. Never zip, bundle or combine them into one file or archive. Use the tool's normal way of giving files to the user (one file card or link per PDF), or save them to the library folder and give both paths.
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

**Only jobs that scored 50% or more are added.**

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
