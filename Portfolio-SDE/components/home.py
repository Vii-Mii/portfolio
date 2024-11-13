import streamlit as st
import webbrowser

def show():
    # Hero Section
    st.markdown("""
    <div style='text-align: center; padding: 2rem;'>
        <h1>👋 Welcome to My Tech Journey</h1>
        <p style='font-size: 1.2rem; color: #666;'>Where Code Meets Innovation</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.markdown("""
        # Vijayaraj Pushpalingam
        ### Software Engineer
        
        > "Passionate about transforming complex problems into elegant solutions"
        
        🚀 With expertise in legacy system modernization and full-stack development, 
        I specialize in building scalable applications and optimizing database performance.
        
        ### 🎯 What I Bring to the Table:
        - **Innovation**: Transformed legacy systems serving 30+ applications
        - **Technical Excellence**: Full-stack development with modern technologies
        - **Data Expertise**: Managed and optimized multi-million record databases
        - **Leadership**: Led multiple successful project implementations
        
        ### 🌟 Current Focus
        - Exploring Cloud-Native Architecture
        - Contributing to Open Source
        - Mastering System Design Patterns
        """)
        
        # Add small space before resume section
        st.markdown("<br>", unsafe_allow_html=True)
        
        
        
        # Download button in a smaller column for better width control
        resume_col1, resume_col2, resume_col3 = st.columns([1.2, 2, 1.2])
        with resume_col2:
            try:
                with open("Portfolio-SDE/assets/resume.pdf", "rb") as pdf_file:
                    PDFbyte = pdf_file.read()
                
                st.download_button(
                    label="⬇️ Download Resume",
                    data=PDFbyte,
                    file_name="Vijayaraj_Pushpalingam_Resume.pdf",
                    mime="application/pdf",
                    key="resume-download",
                    use_container_width=True,
                )
               
            except FileNotFoundError:
                st.error("Resume file not found. Please ensure resume.pdf is in the assets folder.")
    
    with col2:
        # Custom CSS for social media buttons only
        st.markdown("""
        <style>
            /* Social Media Button Styles */
            .github-btn button {
                background-color: #24292e !important;
                color: white !important;
            }
            .linkedin-btn button {
                background-color: #0077b5 !important;
                color: white !important;
            }
            .leetcode-btn button {
                background-color: #f89f1b !important;
                color: white !important;
            }
            .gfg-btn button {
                background-color: #2f8d46 !important;
                color: white !important;
            }
            .email-btn button {
                background-color: #EA4335 !important;
                color: white !important;
            }
        </style>
        """, unsafe_allow_html=True)
        
        # Contact Links Container
        st.markdown("### 🤝 Let's Connect!")
        
        # Container for social links with reduced width
        _, center_col, _ = st.columns([0.1, 0.8, 0.1])
        with center_col:
            # GitHub
            st.markdown('<div class="github-btn">', unsafe_allow_html=True)
            github_btn = st.button(
                "🔗 GitHub",
                help="Visit my GitHub profile",
                use_container_width=True,
            )
            st.markdown('</div>', unsafe_allow_html=True)
            if github_btn:
                webbrowser.open_new_tab("https://github.com/Vii-Mii")
            
            # LinkedIn
            st.markdown('<div class="linkedin-btn">', unsafe_allow_html=True)
            linkedin_btn = st.button(
                "💼 LinkedIn",
                help="Connect with me on LinkedIn",
                use_container_width=True,
            )
            st.markdown('</div>', unsafe_allow_html=True)
            if linkedin_btn:
                webbrowser.open_new_tab("https://www.linkedin.com/in/vijayaraj-p-0b11821b6/")
            
            # LeetCode
            st.markdown('<div class="leetcode-btn">', unsafe_allow_html=True)
            leetcode_btn = st.button(
                "👨‍💻 LeetCode",
                help="Check my LeetCode profile",
                use_container_width=True,
            )
            st.markdown('</div>', unsafe_allow_html=True)
            if leetcode_btn:
                webbrowser.open_new_tab("https://leetcode.com/VijayarajP/")
            
            # GeeksforGeeks
            st.markdown('<div class="gfg-btn">', unsafe_allow_html=True)
            gfg_btn = st.button(
                "🎯 GeeksforGeeks",
                help="View my GeeksforGeeks profile",
                use_container_width=True,
            )
            st.markdown('</div>', unsafe_allow_html=True)
            if gfg_btn:
                webbrowser.open_new_tab("https://auth.geeksforgeeks.org/user/vjlingam7")
            
            # Email
            st.markdown('<div class="email-btn">', unsafe_allow_html=True)
            email_btn = st.button(
                "📧 Email",
                help="Send me an email",
                use_container_width=True,
            )
            st.markdown('</div>', unsafe_allow_html=True)
            if email_btn:
                webbrowser.open_new_tab("mailto:vjlingam7@gmail.com")
        
        # Quick Highlights
        st.divider()
        st.subheader("🏆 Quick Highlights")
        
        # Metrics in columns
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric(
                "Experience",
                "2+ Years",
                delta="Growing"
            )
        with col2:
            st.metric(
                "Applications",
                "30+",
                delta="Managed"
            )
        with col3:
            st.metric(
                "Projects",
                "15+",
                delta="Delivered"
            )
    # After Current Focus section
    st.divider()
    
    # Resume Download Section
    st.markdown("""
    <style>
    .download-btn {
        text-align: center;
        margin: 20px 0;
    }
    .download-btn button {
        background-color: #4CAF50 !important;
        color: white !important;
        padding: 0.5rem 1rem;
        font-weight: bold !important;
        display: inline-flex !important;
        align-items: center;
        gap: 8px;
    }
    .download-btn button:hover {
        background-color: #45a049 !important;
        border: 2px solid #357a38 !important;
    }
    </style>
    """, unsafe_allow_html=True)

    