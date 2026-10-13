# Application Autofill

**By Akshay Dubey** · [github.com/akshaydubey1](https://github.com/akshaydubey1)

Stop retyping your résumé into every careers site. Open the application form, ask your AI tool to fill it, and review everything before you submit.

## What it does

- **Reads the form on your screen**, page by page, from Workday, Greenhouse, Lever, iCIMS, Ashby, LinkedIn Easy Apply or any careers site.
- **Fills it from your profile and tailored résumé.** It uploads the résumé that [Resume Tailor](../akshay-dubey-resume-tailor/) made for this exact job, and fixes anything the site's résumé parser got wrong.
- **Drafts short answers** to "Why this role?" style questions from your real experience, for you to check.
- **Stops for your review.** You see every answer, every blank field and every consent box before anything is submitted. You say "submit", or nothing goes out.
- **Logs it.** It marks the job as applied in your private job list.

## What it never does

- Submit without your yes
- Type passwords, codes, government ID numbers, or bank or card details
- Create accounts, sign in for you, or solve CAPTCHAs
- Answer voluntary self-ID questions (gender, ethnicity, veteran, disability) for you
- Save screen recordings or screenshots

## Works in

Any tool that supports the open [Agent Skills](https://agentskills.io) format and can see your screen or browser. It works best with a browser tool that reads the page (Claude in Chrome, the Claude desktop app's built-in browser, or similar). Without one, it uses screenshots and clicks, or gives you a copy-paste answer sheet.

## Setup

On first use it builds `applicant-profile.json` from your résumé and asks a few questions once: work authorization, sponsorship, relocation, start date and salary expectation. The template is in `references/profile-template.json`.

## License

MIT © 2026 Akshay Dubey. Free to use, share and adapt with credit.
