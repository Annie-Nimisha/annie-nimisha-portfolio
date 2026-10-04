import os
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, HRFlowable, Table, TableStyle, PageBreak
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_RIGHT, TA_JUSTIFY
from reportlab.pdfgen import canvas
import pymupdf

class NumberedCanvas(canvas.Canvas):
    def __init__(self, *args, **kwargs):
        super(NumberedCanvas, self).__init__(*args, **kwargs)
        self._saved_page_states = []

    def showPage(self):
        self._saved_page_states.append(dict(self.__dict__))
        self._startPage()

    def save(self):
        num_pages = len(self._saved_page_states)
        for state in self._saved_page_states:
            self.__dict__.update(state)
            self.draw_page_decorations(num_pages)
            super(NumberedCanvas, self).showPage()
        super(NumberedCanvas, self).save()

    def draw_page_decorations(self, page_count):
        self.saveState()
        # Top gradient-like accent stripe
        self.setFillColor(colors.HexColor("#0284C7"))
        self.rect(0, 787, 612, 5, fill=1, stroke=0)
        self.setFillColor(colors.HexColor("#38BDF8"))
        self.rect(0, 785, 612, 2, fill=1, stroke=0)

        # Footer
        self.setFont("Helvetica", 8.5)
        self.setFillColor(colors.HexColor("#64748B"))
        footer_y = 25
        self.drawString(38, footer_y, "A P Annie Nimisha — Curriculum Vitae")
        page_str = f"Page {self._pageNumber} of {page_count}"
        self.drawRightString(612 - 38, footer_y, page_str)
        
        self.setStrokeColor(colors.HexColor("#CBD5E1"))
        self.setLineWidth(0.6)
        self.line(38, footer_y + 11, 612 - 38, footer_y + 11)
        self.restoreState()

def create_resume(output_path):
    doc = SimpleDocTemplate(
        output_path,
        pagesize=letter,
        leftMargin=38,
        rightMargin=38,
        topMargin=26,
        bottomMargin=36
    )

    styles = getSampleStyleSheet()

    PRIMARY = colors.HexColor("#0F172A")       # Deep Slate
    ACCENT = colors.HexColor("#0369A1")        # Deep Sky Blue
    ACCENT_LIGHT = colors.HexColor("#0284C7")  # Bright Sky Blue
    TEXT_DARK = colors.HexColor("#1E293B")     # Dark Slate Text
    TEXT_MUTED = colors.HexColor("#475569")    # Slate Muted
    BORDER_COLOR = colors.HexColor("#CBD5E1")  # Slate Border
    BG_BOX = colors.HexColor("#F1F5F9")        # Slate Light Box

    name_style = ParagraphStyle(
        'NameStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=19,
        leading=22,
        textColor=PRIMARY,
        spaceAfter=2
    )

    role_sub_style = ParagraphStyle(
        'RoleSubStyle',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=9.5,
        leading=13,
        textColor=ACCENT_LIGHT,
        spaceAfter=2
    )

    contact_style = ParagraphStyle(
        'ContactStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=TEXT_MUTED
    )

    contact_right_style = ParagraphStyle(
        'ContactRightStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=12.5,
        textColor=TEXT_MUTED,
        alignment=TA_RIGHT
    )

    section_heading = ParagraphStyle(
        'SectionHeading',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=10,
        leading=13,
        textColor=ACCENT,
        spaceBefore=5,
        spaceAfter=2,
        keepWithNext=True
    )

    section_heading_p2 = ParagraphStyle(
        'SectionHeadingP2',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=11,
        leading=15,
        textColor=ACCENT,
        spaceBefore=14,
        spaceAfter=6,
        keepWithNext=True
    )

    body_style = ParagraphStyle(
        'BodyStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK,
        alignment=TA_JUSTIFY,
        spaceAfter=2
    )

    body_style_p2 = ParagraphStyle(
        'BodyStyleP2',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.5,
        leading=14,
        textColor=TEXT_DARK,
        spaceAfter=4
    )

    item_title_bold = ParagraphStyle(
        'ItemTitleBold',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.8,
        leading=11.5,
        textColor=PRIMARY
    )

    item_meta_right = ParagraphStyle(
        'ItemMetaRight',
        parent=styles['Normal'],
        fontName='Helvetica-Bold',
        fontSize=8.5,
        leading=11.5,
        textColor=ACCENT,
        alignment=TA_RIGHT
    )

    bullet_style = ParagraphStyle(
        'BulletStyle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=8.5,
        leading=11.5,
        textColor=TEXT_DARK,
        leftIndent=12,
        firstLineIndent=-8,
        spaceAfter=1.5
    )

    bullet_style_p2 = ParagraphStyle(
        'BulletStyleP2',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=9.2,
        leading=13.5,
        textColor=TEXT_DARK,
        leftIndent=14,
        firstLineIndent=-10,
        spaceAfter=6
    )

    story = []

    # =========================================================================
    # PAGE 1: HEADER, SUMMARY, EDUCATION, SKILLS, INTERNSHIPS, PROJECTS
    # =========================================================================

    # Header
    head_left = [
        Paragraph("A P ANNIE NIMISHA", name_style),
        Paragraph("Computer Science &amp; Engineering Student | Full Stack &amp; AI Enthusiast", role_sub_style),
        Paragraph("<font color='#0F172A'><b>Location:</b></font> Kanyakumari, Tamil Nadu, India", contact_style)
    ]
    head_right = [
        Paragraph("<font color='#0F172A'><b>Phone:</b></font> +91 9597515781", contact_right_style),
        Paragraph("<font color='#0F172A'><b>Email:</b></font> <a href='mailto:annienimisha2006@gmail.com' color='#0284C7'><u>annienimisha2006@gmail.com</u></a>", contact_right_style),
        Paragraph("<font color='#0F172A'><b>LinkedIn:</b></font> <a href='https://www.linkedin.com/in/a-p-annie-nimisha-861577336' color='#0284C7'><u>linkedin.com/in/a-p-annie-nimisha-861577336</u></a>", contact_right_style)
    ]
    head_table = Table([[head_left, head_right]], colWidths=[310, 226])
    head_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(head_table)
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=1.2, color=ACCENT_LIGHT, spaceBefore=2, spaceAfter=4))

    # Professional Summary
    story.append(Paragraph("PROFESSIONAL SUMMARY", section_heading))
    summary_text = (
        "Motivated and enthusiastic Computer Science Engineering student with a strong interest in "
        "<b>Full Stack Development</b> and <b>Artificial Intelligence</b>. Currently building expertise in "
        "Python, JavaScript, SQL, HTML, and CSS. Passionate about solving real-world problems through "
        "innovative software solutions, with hands-on experience in academic projects, internships, and "
        "hackathons. A quick learner and problem solver seeking opportunities."
    )
    story.append(Paragraph(summary_text, body_style))
    story.append(HRFlowable(width="100%", thickness=0.4, color=BORDER_COLOR, spaceBefore=3, spaceAfter=4))

    # Education
    story.append(Paragraph("EDUCATION", section_heading))
    edu_rows = [
        [
            Paragraph("<b>B.E. Computer Science and Engineering</b> &bull; <font color='#475569'>DMI Engineering College</font>", item_title_bold),
            Paragraph("<b>2024 – 2028</b> | <font color='#0369A1'><b>CGPA: 9.2</b> (till 4th sem)</font>", item_meta_right)
        ],
        [
            Paragraph("<b>Higher Secondary Certificate (HSC)</b> &bull; <font color='#475569'>Pearl Matriculation Higher Secondary School</font>", item_title_bold),
            Paragraph("<b>2023 – 2024</b> | <font color='#0369A1'><b>85%</b></font>", item_meta_right)
        ],
        [
            Paragraph("<b>Secondary School Leaving Certificate (SSLC)</b> &bull; <font color='#475569'>St. Anne's Matriculation School</font>", item_title_bold),
            Paragraph("<b>2021 – 2022</b> | <font color='#0369A1'><b>94%</b></font>", item_meta_right)
        ]
    ]
    edu_table = Table(edu_rows, colWidths=[330, 206])
    edu_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
    ]))
    story.append(edu_table)
    story.append(HRFlowable(width="100%", thickness=0.4, color=BORDER_COLOR, spaceBefore=3, spaceAfter=4))

    # Technical Skills
    story.append(Paragraph("TECHNICAL SKILLS", section_heading))
    tech_data = [
        [
            Paragraph("<b>Programming Languages:</b>", item_title_bold),
            Paragraph("Python, C, Java (basics)", body_style)
        ],
        [
            Paragraph("<b>Web Technologies:</b>", item_title_bold),
            Paragraph("HTML, CSS, JavaScript", body_style)
        ],
        [
            Paragraph("<b>Database:</b>", item_title_bold),
            Paragraph("MongoDB (basics), SQL", body_style)
        ],
        [
            Paragraph("<b>Core Areas:</b>", item_title_bold),
            Paragraph("Full stack development, web development", body_style)
        ],
    ]
    tech_table = Table(tech_data, colWidths=[150, 386])
    tech_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 1),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1),
    ]))
    story.append(tech_table)

    # Soft Skills
    story.append(Paragraph("SOFT SKILLS", section_heading))
    story.append(Paragraph("Leadership, Communication, Teamwork, Quick Learner, Analytical Thinking", body_style))
    story.append(HRFlowable(width="100%", thickness=0.4, color=BORDER_COLOR, spaceBefore=3, spaceAfter=4))

    # Internship Experience
    story.append(Paragraph("INTERNSHIP EXPERIENCE", section_heading))
    internships = [
        [
            Paragraph("<b>Data Analyst Intern</b> — <font color='#475569'>JCLICK Solutions</font>", item_title_bold),
            Paragraph("<font color='#0369A1'><b>Internship</b></font>", item_meta_right)
        ],
        [
            Paragraph("<b>Python Full Stack Developer Intern</b> — <font color='#475569'>SMARK Solutions</font>", item_title_bold),
            Paragraph("<font color='#0369A1'><b>Internship</b></font>", item_meta_right)
        ],
        [
            Paragraph("<b>Staff Engineer Role (Intern)</b> — <font color='#475569'>Agile Tribers</font>", item_title_bold),
            Paragraph("<font color='#0369A1'><b>1 Month</b></font>", item_meta_right)
        ]
    ]
    intern_table = Table(internships, colWidths=[390, 146])
    intern_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 1.5),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 1.5),
    ]))
    story.append(intern_table)
    story.append(HRFlowable(width="100%", thickness=0.4, color=BORDER_COLOR, spaceBefore=3, spaceAfter=4))

    # Projects
    story.append(Paragraph("PROJECTS", section_heading))
    projects = [
        ("Smart Vehicle Parking System", "IoT and web-enabled automated parking slot management & monitoring system. (Awarded 2nd Prize in Ideathon)"),
        ("Smart Checklist", "Dynamic digital task management and productivity checklist with responsive real-time tracking."),
        ("Expense Tracker", "Personal financial tracking web application for categorizing daily expenses and budget insights."),
        ("Kaivinai AI", "Digital platform for empowering traditional artisans through technology and AI craft promotion."),
        ("Cycora", "AI-powered menstrual health assistant providing personalized cycle predictions, health guidance, and wellness tips."),
        ("Bankora X", "Multi-bank appointment booking and queue management platform streamlining customer branch scheduling.")
    ]

    for p_title, p_desc in projects:
        story.append(Paragraph(f"&bull; <b>{p_title}</b> – <font color='#334155'>{p_desc}</font>", bullet_style))

    # =========================================================================
    # PAGE 2: ACHIEVEMENTS, CERTIFICATIONS, DECLARATION
    # =========================================================================
    story.append(PageBreak())

    # Achievements
    story.append(Paragraph("ACHIEVEMENTS", section_heading_p2))
    achievements = [
        ("2nd Prize - Ideathon (Smart Parking System)", "Secured second place for the innovative IoT and web-based smart parking system prototype."),
        ("3rd Prize - Technical Paper Presentation", "Awarded 3rd place for well-researched technical paper, conceptual clarity, and presentation delivery."),
        ("Winner - Voice of DMI Competition", "First prize winner in the college-wide public speaking and communication competition."),
        ("Participated in Buildathon 2026", "Organised by TechVerse Solutions; rapid software prototyping and engineering under hackathon timelines."),
        ("Participated in NexBuildOn Hack 2026", "Collaborated on problem-solving challenge tracks with a multi-disciplinary developer team."),
        ("Participated in SheBuilds Chennai X CCCL Hack", "Women-in-tech hackathon focusing on collaborative software engineering and social impact solutions.")
    ]
    for ach_title, ach_desc in achievements:
        story.append(Paragraph(f"&bull; <b>{ach_title}</b><br/><font color='#475569'>&nbsp;&nbsp;&nbsp;{ach_desc}</font>", bullet_style_p2))

    story.append(Spacer(1, 6))
    story.append(HRFlowable(width="100%", thickness=0.6, color=BORDER_COLOR, spaceBefore=4, spaceAfter=10))

    # Certifications
    story.append(Paragraph("CERTIFICATIONS", section_heading_p2))
    certs = [
        ("Python Programming", "Swayam NPTEL", "Comprehensive Python programming, data structures, and algorithmic logic."),
        ("Data Analytics (CCP)", "Novi Tech Certificate Course in Python", "Hands-on data analytics, exploratory data processing, and visualization in Python."),
        ("MongoDB Basics for Students", "MongoDB University", "Document model, MongoDB Atlas, schema design, and CRUD operations."),
        ("Python Course", "CSC", "Foundational and object-oriented Python software development."),
        ("CS50's Introduction to Computer Science (CS50x)", "Offered by Harvard University", "Rigorous computer science study covering C, algorithms, memory, Python, SQL, and web technologies (Currently Pursuing).")
    ]
    for c_title, c_issuer, c_detail in certs:
        story.append(Paragraph(f"&bull; <b>{c_title}</b> &bull; <font color='#0369A1'><b>{c_issuer}</b></font><br/><font color='#475569'>&nbsp;&nbsp;&nbsp;{c_detail}</font>", bullet_style_p2))

    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=0.6, color=BORDER_COLOR, spaceBefore=6, spaceAfter=12))

    # Declaration
    story.append(Paragraph("DECLARATION", section_heading_p2))
    declaration_text = (
        "I hereby declare that the details furnished above are true and correct to the best of my knowledge and belief."
    )
    story.append(Paragraph(declaration_text, body_style_p2))
    story.append(Spacer(1, 28))

    decl_data = [
        [
            Paragraph("<b>Place:</b> Kanyakumari<br/><b>Date:</b> 03/10/2026", body_style_p2),
            Paragraph("<b>Signature:</b><br/><br/><font size='12' color='#0F172A'><b><i>A P Annie Nimisha</i></b></font>", ParagraphStyle('Sig', parent=body_style_p2, alignment=TA_RIGHT))
        ]
    ]
    decl_table = Table(decl_data, colWidths=[260, 276])
    decl_table.setStyle(TableStyle([
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('LEFTPADDING', (0, 0), (-1, -1), 0),
        ('RIGHTPADDING', (0, 0), (-1, -1), 0),
        ('TOPPADDING', (0, 0), (-1, -1), 0),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 0),
    ]))
    story.append(decl_table)

    doc.build(story, canvasmaker=NumberedCanvas)

if __name__ == '__main__':
    target = os.path.join(r"d:\Documents\portfolio\assets\resume", "resume.pdf")
    create_resume(target)
    print(f"Generated at: {target}")

    # Generate preview images
    doc_fitz = pymupdf.open(target)
    for i, page in enumerate(doc_fitz):
        pix = page.get_pixmap(dpi=150)
        img_path = f"assets/resume/resume_page_{i+1}.png"
        pix.save(img_path)
        print(f"Rendered page {i+1} to {img_path}")
