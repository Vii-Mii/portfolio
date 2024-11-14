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
        
# Container for social links
            # Replace the social links container section with this:
        _, center_col, _ = st.columns([0.1, 0.8, 0.1])
        with center_col:
            st.markdown("""
                <style>
                    .social-link {
                        display: block;
                        text-decoration: none;
                        margin: 8px 0;
                    }
                    .social-button {
                        width: 100%;
                        padding: 10px;
                        border: none;
                        border-radius: 5px;
                        color: white;
                        font-size: 16px;
                        cursor: pointer;
                        text-align: center;
                    }
                </style>
                
                <a class='social-link' href='https://github.com/Vii-Mii' target='_blank'>
                    <div class='social-button' style='background-color: #24292e;'>
                        🔗 GitHub
                    </div>
                </a>
                
                <a class='social-link' href='https://www.linkedin.com/in/vijayaraj-p-0b11821b6/' target='_blank'>
                    <div class='social-button' style='background-color: #0077b5;'>
                        💼 LinkedIn
                    </div>
                </a>
                
                <a class='social-link' href='https://leetcode.com/VijayarajP/' target='_blank'>
                    <div class='social-button' style='background-color: #f89f1b;'>
                        👨‍💻 LeetCode
                    </div>
                </a>
                
                <a class='social-link' href='https://www.geeksforgeeks.org/user/vii_leaner/' target='_blank'>
                    <div class='social-button' style='background-color: #2f8d46;'>
                        🎯 GeeksforGeeks
                    </div>
                </a>
                
                <a class='social-link' href='mailto:vjlingam7@gmail.com'>
                    <div class='social-button' style='background-color: #EA4335;'>
                        📧 Email
                    </div>
                </a>
            """, unsafe_allow_html=True)
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

    