# A P Annie Nimisha — Personal Portfolio & Curriculum Vitae 🚀

A modern, responsive, high-performance personal portfolio website built with semantic **HTML5**, modern **CSS3**, and vanilla **JavaScript**. Designed specifically for software developer placements, internships, hackathon presentations, and recruiter evaluations.

---

## 📁 Project Structure

```text
portfolio/
│
├── index.html                   # Main semantic HTML structure & portfolio content
├── style.css                    # Modern dark theme styles, animations & responsive queries
├── script.js                    # Typing effect, mobile nav, resume page switcher, modals, toast
├── generate_resume.py           # Automated Python script to generate official 2-page resume PDF
│
├── assets/
│   ├── images/
│   │   ├── favicon.svg          # Modern glowing monogram browser icon
│   │   └── profile-placeholder.svg # High-res developer vector avatar
│   │
│   └── resume/
│       ├── resume.pdf           # Official 2-page curriculum vitae PDF
│       ├── resume_page_1.png    # High-resolution image preview of Page 1
│       ├── resume_page_2.png    # High-resolution image preview of Page 2
│       └── README.txt           # Resume status and re-generation guide
│
└── README.md                    # Complete setup, customization, and deployment guide
```

---

## ⚡ How to Run the Website Locally in VS Code

1. **Open VS Code**:
   - Launch VS Code and click **File > Open Folder...**
   - Select your project folder: `d:\Documents\portfolio`
2. **Install the "Live Server" Extension** (Recommended):
   - Click the Extensions icon on the left sidebar (or press `Ctrl + Shift + X`).
   - Search for **Live Server** (by *Ritwick Dey*) and click **Install**.
3. **Launch the Website**:
   - Right-click `index.html` in the explorer and select **Open with Live Server** (or click **Go Live** at the bottom-right status bar).
   - Your default browser will automatically open: `http://127.0.0.1:5500/index.html`.
4. Any changes you make to `index.html`, `style.css`, or `script.js` will instantly reload in your browser.

---

## 📄 Official Resume Integration

The portfolio comes with Annie's official 2-page resume integrated across multiple touchpoints:
1. **Interactive Resume Showcase Section** (`#resume`): Visitors can toggle between Page 1 and Page 2 right on the website.
2. **1-Click Download Buttons**: Nav bar, Hero, and Resume showcase download `assets/resume/resume.pdf` (`A_P_Annie_Nimisha_Resume.pdf`).
3. **Automated Generator**: Run `python generate_resume.py` to regenerate both `resume.pdf` and the high-resolution preview images from source code.

---

## 🛠️ How to Add New Content

### 1. How to Add a New Project
Open `index.html`, scroll to the `<section id="projects">` section, and paste this card template inside `<div class="projects-grid">`:

```html
<article class="project-card card-glass">
  <div class="project-header">
    <div class="project-icon-box">
      <i class="fa-solid fa-code"></i>
    </div>
    <div class="project-badges">
      <span class="badge badge-accent">Web App</span>
      <span class="badge badge-subtle">Full Stack</span>
    </div>
  </div>

  <div class="project-body">
    <h3 class="project-title">Your Project Name</h3>
    <p class="project-description">
      A concise 2-sentence description of what problem this project solves and the audience it serves.
    </p>

    <div class="project-features">
      <h4 class="features-heading"><i class="fa-solid fa-star"></i> Key Features:</h4>
      <ul class="features-list">
        <li><i class="fa-solid fa-check"></i> Feature 1 description</li>
        <li><i class="fa-solid fa-check"></i> Feature 2 description</li>
        <li><i class="fa-solid fa-check"></i> Feature 3 description</li>
      </ul>
    </div>

    <div class="project-tech-tags">
      <span class="tech-tag">React</span>
      <span class="tech-tag">Node.js</span>
      <span class="tech-tag">MongoDB</span>
    </div>
  </div>

  <div class="project-footer">
    <a href="https://github.com/Annie-Nimisha/your-repo" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-outline">
      <i class="fa-brands fa-github"></i> GitHub Repo
    </a>
    <a href="https://your-demo-url.vercel.app" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-primary">
      <i class="fa-solid fa-arrow-up-right-from-square"></i> Live Demo
    </a>
  </div>
</article>
```

### 2. How to Add a New Skill
Open `index.html`, locate the relevant category in `<section id="skills">`, and paste a new `.skill-pill` item:

```html
<div class="skill-pill">
  <i class="fa-brands fa-react skill-icon" style="color: #61dafb;"></i>
  <div class="skill-meta">
    <span class="skill-name">React.js</span>
    <span class="skill-level">Component Architecture & Hooks</span>
  </div>
</div>
```

### 3. How to Add a New Certification
Open `index.html`, locate `<section id="certifications">`, and duplicate the `<div class="cert-card card-glass">` container:

```html
<div class="cert-card card-glass">
  <div class="cert-header">
    <div class="cert-icon-wrapper">
      <i class="fa-solid fa-certificate"></i>
    </div>
    <div class="cert-status-badge badge-accent">
      <i class="fa-solid fa-check"></i>
      <span>Completed</span>
    </div>
  </div>

  <div class="cert-body">
    <span class="cert-issuer">AWS / Coursera / HackerRank</span>
    <h3 class="cert-title">Certificate Name Here</h3>
    <p class="cert-description">
      Key competencies gained and practical problems solved during this coursework.
    </p>
  </div>

  <div class="cert-footer">
    <a href="https://credential-link.com" target="_blank" rel="noopener noreferrer" class="btn btn-sm btn-primary">
      <i class="fa-solid fa-shield-halved"></i> Verify Credential
    </a>
  </div>
</div>
```

---

## 🎨 How to Change Colors and Fonts

All visual design tokens are defined at the top of `style.css` in `:root`:

```css
:root {
  /* Change the dark background tint */
  --bg-primary: #07090e;

  /* Change the accent gradient colors */
  --accent-cyan: #38bdf8;
  --accent-indigo: #6366f1;
  --accent-purple: #a855f7;
  --accent-pink: #ec4899;

  /* Change the font family */
  --font-main: 'Plus Jakarta Sans', sans-serif;
  --font-mono: 'JetBrains Mono', monospace;
}
```
Modifying any variable instantly cascades across the entire website.

---

## 📬 Connecting the Contact Form to Receive Live Emails

The contact form includes complete front-end client-side validation. To have messages sent straight to your email (`annienimisha2006@gmail.com`) for free without any backend coding:

1. Go to [https://formspree.io/](https://formspree.io/) and create a free account.
2. Click **New Form**, name it "Portfolio Contact", and set your recipient email to `annienimisha2006@gmail.com`.
3. Copy your unique Formspree endpoint (e.g. `https://formspree.io/f/xbjvonpk`).
4. In `index.html`, update `<form class="contact-form" id="contactForm">`:
   ```html
   <form class="contact-form" id="contactForm" action="https://formspree.io/f/YOUR_ENDPOINT_ID" method="POST">
   ```

---

## 🚀 How to Push to GitHub & Host with GitHub Pages

### Step 1: Initialize Git and Commit
Open a terminal in VS Code (`Ctrl + ~`) in the `portfolio` folder:
```powershell
git init
git add .
git commit -m "Initial commit: A.P. Annie Nimisha modern portfolio"
```

### Step 2: Create a Repository on GitHub
1. Log in to [GitHub](https://github.com/Annie-Nimisha).
2. Click the **+** (plus icon) in the top-right and select **New repository**.
3. Name it: `portfolio` (or `Annie-Nimisha.github.io`).
4. Set visibility to **Public**.
5. Do **not** check "Add a README" (we already created one).
6. Click **Create repository**.

### Step 3: Push Your Code
Copy the commands shown on GitHub and run them in your VS Code terminal:
```powershell
git branch -M main
git remote add origin https://github.com/Annie-Nimisha/portfolio.git
git push -u origin main
```

### Step 4: Enable Free Hosting via GitHub Pages
1. Go to your GitHub repository page: `https://github.com/Annie-Nimisha/portfolio`
2. Click **Settings** (tab at the top).
3. In the left menu, click **Pages**.
4. Under **Build and deployment > Branch**:
   - Select `main` from the dropdown.
   - Leave the folder as `/(root)`.
   - Click **Save**.
5. Wait ~60 seconds. Refresh the page.
6. GitHub will display:
   > **Your site is live at https://annie-nimisha.github.io/portfolio/**

---

## 💡 Recommended Refinement Strategy

When extending your portfolio in future cycles, give concise, targeted prompts such as:
- *"Add a new Project card for my Expense Tracker without changing the existing styling."*
- *"Add my CS50 certificate link and badge in the Certifications section without modifying any other part."*

This preserves the high-polish design system while letting your portfolio grow smoothly alongside your achievements!
