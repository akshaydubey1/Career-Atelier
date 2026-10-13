# Resume Tailor

**By Akshay Dubey** · [github.com/akshaydubey1](https://github.com/akshaydubey1)

Stop sending résumés to jobs you won't get, and stop rewriting the same résumé from scratch.

Paste a job description. Resume Tailor scores it against your existing résumés and does only the work that's needed:

| Your best match | What you get |
| --- | --- |
| **85% or more** | Your existing résumé, reused as is, plus a new cover letter |
| **75–84%** | A résumé tailored to 85% or more, plus a cover letter |
| **Below 75%** | A blunt "skip this one" and the reasons why. No wasted effort. |

## Why it's different

- **Honest scoring.** It uses a fixed formula where must-haves count double, and it scores strictly.
- **Never invents experience.** It only rewords and reorders what you've actually done. Courses and certifications are never passed off as work experience.
- **Keeps your formatting.** It edits a copy of your own Word file, so your fonts, spacing and layout stay the same.
- **Reuses past work.** Every tailored résumé is saved and checked first next time, which saves time and effort.
- **Clean files.** The PDFs carry only your name in their properties, with names like `AkshayDPTR.pdf` (résumé) and `AkshayDPTCL.pdf` (cover letter).
- **Private job list.** Every job you qualify for (75% or more) is logged quietly with company, position, location, salary, sponsorship and a comment. Ask "show my jobs" to see it.
- **Cover letters aren't stored.** You download them and they're deleted.

## Works in any Agent Skills tool

Resume Tailor uses the open [Agent Skills](https://agentskills.io) format. It runs in Claude, Claude Code, ChatGPT and Codex, Cursor, GitHub Copilot and VS Code, Gemini CLI, and [many more](https://agentskills.io/home).

It adapts to what your tool can do:

| Your tool can… | You get |
| --- | --- |
| Read and write files and run code | Formatted PDFs, a saved résumé library and the job list |
| Create files but not run code | Tailored documents, with basic formatting |
| Only chat | The score and verdict, plus the résumé and cover letter text to paste |

## Install

1. Download this folder, or the zip from Releases.
2. Add it to your tool's skills. Each tool has its own steps:
   - **Claude app:** upload the zip as a custom skill ([how skills work](https://support.claude.com/en/articles/12512176-what-are-skills)).
   - **Claude Code:** copy the folder to `~/.claude/skills/`.
   - **Other tools:** see your tool's skills page, linked from the [Agent Skills client list](https://agentskills.io/home).
3. Paste a job description. On first use it asks for your résumé (.docx) and where to keep your files.

**For formatted PDFs:** Python 3 plus LibreOffice (free) or Microsoft Word. The bundled `scripts/finalize.py` installs the Python packages it needs.

## File naming

**First name + last-name initial + company code + R or CL**

- One-word company: first and last letter. Perfect → `PT`
- Two or more words: first letters of the first two words. Capital One → `CO`

So Akshay Dubey applying to Perfect gets `AkshayDPTR.pdf` and `AkshayDPTCL.pdf`.

## License

MIT © 2026 Akshay Dubey. Free to use, share and adapt with credit.
