import streamlit as st
from pathlib import Path
from urllib.parse import quote

st.set_page_config(
    page_title="Bharath NS | Portfolio",
    page_icon="✦",
    layout="wide",
    initial_sidebar_state="expanded",
)

ROOT = Path(__file__).parent
ASSETS = ROOT / "assets"
PROFILE =ROOT / "profile.png"
RESUME = ROOT / "resume.pdf.pdf"

# ---------- Premium black & gold styling ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@600;700&display=swap');

:root { --gold: #d6ad55; --gold-light: #f0d58e; --ink: #090909; }
.stApp {
    background:
      radial-gradient(ellipse at 85% 5%, rgba(214,173,85,.10), transparent 32%),
      linear-gradient(145deg, #080808 0%, #111 55%, #090909 100%);
    color: #f5f1e8;
    font-family: 'DM Sans', sans-serif;
}
.block-container { max-width: 1200px; padding-top: 2rem; padding-bottom: 3rem; }
h1, h2, h3 { color: var(--gold) !important; font-family: 'Playfair Display', serif !important; }
p, li, label, .stMarkdown { color: #e8e2d6; }
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #171510, #0c0c0c);
    border-right: 1px solid rgba(214,173,85,.35);
}
section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] h2 { color: var(--gold) !important; }
.hero {
    padding: clamp(25px, 5vw, 55px);
    border: 1px solid rgba(214,173,85,.55);
    border-radius: 24px;
    background: linear-gradient(125deg, rgba(30,27,20,.98), rgba(12,12,12,.96));
    box-shadow: 0 18px 55px rgba(0,0,0,.35), inset 0 0 35px rgba(214,173,85,.045);
    animation: rise .8s ease both;
}
.eyebrow { color: var(--gold-light); letter-spacing: .22em; font-size: .75rem; font-weight: 700; }
.hero-title { font-family: 'Playfair Display',serif; color: #f5e6bd; font-size: clamp(2.5rem, 6vw, 4.5rem); line-height: 1.08; margin: 12px 0; }
.hero-sub { color: var(--gold); font-size: clamp(1.05rem, 2vw, 1.35rem); font-weight: 600; }
.gold-line { width: 90px; height: 3px; background: var(--gold); border-radius: 10px; margin: 22px 0; }
.project-card {
    background: linear-gradient(145deg, #1b1a17, #101010);
    border: 1px solid rgba(214,173,85,.38);
    border-radius: 18px; padding: 23px; min-height: 245px;
    transition: transform .25s ease, border-color .25s ease, box-shadow .25s ease;
    animation: rise .65s ease both;
}
.project-card:hover {
    transform: translateY(-7px);
    border-color: var(--gold-light);
    box-shadow: 0 14px 32px rgba(214,173,85,.12);
}
.project-number { color: var(--gold); font-size: .78rem; letter-spacing: .18em; font-weight: 700; }
.project-icon { font-size: 1.8rem; }
.project-tech { color: var(--gold-light); font-size: .85rem; }
.skill-chip {
    display: inline-block; border: 1px solid rgba(214,173,85,.45);
    background: rgba(214,173,85,.08); color: #f0d58e;
    border-radius: 999px; padding: 7px 13px; margin: 4px; font-size: .88rem;
}
.timeline {
    border-left: 2px solid var(--gold); padding: 4px 0 4px 20px; margin: 12px 0 24px;
}
div.stButton > button, div.stDownloadButton > button, a[kind="primary"] {
    background: linear-gradient(100deg, #d6ad55, #f0d58e) !important;
    color: #111 !important; border: 0 !important; border-radius: 10px !important;
    font-weight: 700 !important; transition: transform .2s ease, box-shadow .2s ease !important;
}
div.stButton > button:hover, div.stDownloadButton > button:hover {
    transform: translateY(-2px); box-shadow: 0 8px 22px rgba(214,173,85,.22);
}
a { color: var(--gold-light) !important; }
[data-testid="stMetric"] {
    background: #171612; border: 1px solid rgba(214,173,85,.3);
    padding: 15px; border-radius: 14px;
}
[data-testid="stMetricValue"] { color: var(--gold-light); }
@keyframes rise { from {opacity:0; transform:translateY(14px)} to {opacity:1; transform:translateY(0)} }
@media (max-width: 700px) {
    .block-container { padding: 1rem 1rem 2rem; }
    .hero { padding: 24px 20px; }
    .project-card { min-height: auto; }
}
</style>
""", unsafe_allow_html=True)

# ---------- Sidebar navigation ----------
with st.sidebar:
    st.markdown("<h2 style='text-align:center; letter-spacing:.12em;'>BHARATH NS</h2>", unsafe_allow_html=True)
    st.caption("ASPIRING AI/ML ENGINEER")
    st.markdown("---")
    page = st.radio(
        "NAVIGATION",
        ["Home", "About Me", "Skills", "Projects", "Education", "Contact"],
        label_visibility="collapsed",
    )
    st.markdown("---")
    st.markdown("[GitHub ↗](https://github.com/bharathnsnirvani-cmd/bharath-portfolio.git)")
    st.markdown("[LinkedIn ↗](https://www.linkedin.com/in/bharath-n-s-36847a442/)")
    st.caption("Designed with Python + Streamlit")

# ---------- Reusable data ----------
projects = [
    {
        "number": "01", "icon": "🌧️", "name": "Landslide Risk Prediction",
        "description": "An AI/ML project focused on estimating landslide risk using relevant environmental and geographic data.",
        "tech": "Python · Machine Learning",
    },
    {
        "number": "02", "icon": "🏥", "name": "Smart Patient Intake Care",
        "description": "An intelligent patient intake concept designed to simplify healthcare information collection and workflows.",
        "tech": "Python · LLM · PostgreSQL",
    },
    {
        "number": "03", "icon": "🪖", "name": "Smart Helmet for Rider Safety",
        "description": "A technology-based safety concept designed to support safer riding through smart sensing and alerts.",
        "tech": "IoT · Sensors · Programming",
    },
    {
        "number": "04", "icon": "🧭", "name": "Smart Local Tourism Portal",
        "description": "A web platform concept promoting Karnataka destinations, local guides, homestays and cultural businesses.",
        "tech": "Python · Streamlit / Web Development",
    },
]

def project_card(project):
    st.markdown(f"""
    <div class="project-card">
      <div class="project-number">PROJECT {project['number']}</div>
      <div class="project-icon">{project['icon']}</div>
      <h3>{project['name']}</h3>
      <p>{project['description']}</p>
      <div class="project-tech">{project['tech']}</div>
    </div>
    """, unsafe_allow_html=True)

# ---------- Pages ----------
if page == "Home":
    left, right = st.columns([1.55, 1], gap="large")
    with left:
        st.markdown("""
        <div class="hero">
          <div class="eyebrow">WELCOME TO MY PORTFOLIO</div>
          <div class="hero-title">Hi, I'm<br>Bharath NS.</div>
          <div class="hero-sub">Aspiring AI/ML Engineer · Developer · Lifelong Learner</div>
          <div class="gold-line"></div>
          <p>I enjoy exploring technology, writing code and building thoughtful solutions with Artificial Intelligence and Machine Learning.</p>
          <p>Currently pursuing B.E. in Artificial Intelligence and Machine Learning.</p>
        </div>
        """, unsafe_allow_html=True)
        st.write("")
        c1, c2 = st.columns(2)
        with c1:
            st.link_button("Explore my GitHub ↗", "https://github.com/bharathns17-ctrl", use_container_width=True)
        with c2:
            st.link_button("Connect on LinkedIn ↗", "https://www.linkedin.com/in/bharath-n-s-36847a442/", use_container_width=True)
    with right:
        if PROFILE.exists():
            st.image(str(PROFILE), use_container_width=True)
        else:
            st.error("Profile photo is not found!S") 
    st.write("")
    st.markdown("### A little about my journey")
    m1, m2, m3 = st.columns(3)
    m1.metric("projects", "04")
    m2.metric("Core languages", "03")
    m3.metric("Focus", "AI + Software")
    st.caption("An evolving portfolio — projects and skills will be updated as I learn and build.")

elif page == "About Me":
    st.title("About Me")
    st.markdown("### Curious mind. Practical builder. Continuous learner.")
    st.write(
        "Hello! I'm Bharath NS, pursuing a Bachelor of Engineering in Artificial Intelligence "
        "and Machine Learning at Cambridge Institute of Technology, North Campus. "
        "I am interested in programming, AI tools and building useful technology projects."
    )
    st.write(
        "My career goal is to grow into an AI/ML engineering role, contribute to meaningful "
        "products and keep strengthening my foundations in software development."
    )
    st.markdown("### Strengths")
    for item in ["Quick learner", "Problem-solving mindset", "Team collaboration", "Leadership", "Continuous learning"]:
        st.markdown(f"- {item}")

elif page == "Skills":
    st.title("Skills & Technologies")
    st.write("A snapshot of the tools and topics I have explored so far.")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Programming")
        for skill in ["Python", "C", "Java"]:
            st.markdown(f'<span class="skill-chip">{skill}</span>', unsafe_allow_html=True)
        st.markdown("### Development tools")
        for skill in ["VS Code", "Git", "GitHub", "Streamlit"]:
            st.markdown(f'<span class="skill-chip">{skill}</span>', unsafe_allow_html=True)
    with col2:
        st.markdown("### AI & data")
        for skill in ["Machine Learning", "Generative AI", "Deep Learning fundamentals", "NumPy / pandas (learning)"]:
            st.markdown(f'<span class="skill-chip">{skill}</span>', unsafe_allow_html=True)
        st.markdown("### AI tools")
        for skill in ["ChatGPT", "Gemini", "Google AI Studio"]:
            st.markdown(f'<span class="skill-chip">{skill}</span>', unsafe_allow_html=True)
    st.info("Skill labels describe areas explored; they are not proficiency ratings.")

elif page == "Projects":
    st.title("Projects")
    st.write("Selected work and project concepts from my learning journey.")
    rows = st.columns(2, gap="large")
    for i, project in enumerate(projects):
        with rows[i % 2]:
            project_card(project)
            st.markdown(
                "[View my GitHub profile ↗](https://github.com/bharathns17-ctrl)"
            )
            st.write("")

elif page == "Education":
    st.title("Education")
    st.markdown("""
    <div class="timeline">
      <h3>Bachelor of Engineering</h3>
      <b>Artificial Intelligence and Machine Learning</b><br>
      Cambridge Institute of Technology, North Campus<br>
      <span style="color:#d6ad55;">Currently pursuing · Expected graduation: 2029</span>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("### Academic highlights")
    a, b, c = st.columns(3)
    a.metric("SSLC", "92%")
    b.metric("PUC", "93%")
    c.metric("2nd semester SGPA", "9.7")
    st.caption("Academic figures are based on details previously shared.")

elif page == "Contact":
    st.title("Let's Connect")
    st.write("I'm open to learning opportunities, collaborations and conversations about technology.")
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("### Contact details")
        st.markdown("📧 [bharathnsnirvani@gmail.com](mailto:bharathnsnirvani@gmail.com)")
        st.markdown("💻 [GitHub](https://github.com/bharathns17-ctrl)")
        st.markdown("🔗 [LinkedIn](https://www.linkedin.com/in/bharath-n-s-36847a442/)")
    with c2:
        st.markdown("### Send a message")
        with st.form("contact_form"):
            sender = st.text_input("Your name")
            sender_email = st.text_input("Your email")
            message = st.text_area("Your message")
            submitted = st.form_submit_button("Prepare email")
        if submitted:
            if not sender.strip() or not sender_email.strip() or not message.strip():
                st.warning("Please fill in all three fields.")
            else:
                subject = quote(f"Portfolio enquiry from {sender}")
                body = quote(f"Name: {sender}\nEmail: {sender_email}\n\n{message}")
                mailto = f"mailto:bharathnsnirvani@gmail.com?subject={subject}&body={body}"
                st.success("Your email draft is ready. Select the link below to open your email app.")
                st.markdown(f"[Open email draft ↗]({mailto})")

    st.markdown("---")
    st.markdown("### Resume")
    if RESUME.exists():
        with open(RESUME, "rb") as file:
            st.download_button(
                "Download my resume ↓",
                data=file,
                file_name="Bharath_NS_Resume.pdf",
                mime="application/pdf",
            )
    else:
        st.info("To enable resume download, add your latest PDF as assets/resume.pdf.")

# ---------- Footer ----------
st.markdown("---")
st.markdown(
    "<p style='text-align:center;color:#d6ad55;'>© 2026 Bharath NS · Built with Python & Streamlit ✦</p>",
    unsafe_allow_html=True,
)
