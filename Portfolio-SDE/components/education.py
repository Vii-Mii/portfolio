import streamlit as st
import plotly.graph_objects as go

def create_timeline():
    fig = go.Figure(data=[go.Scatter(
        x=[2015, 2017, 2021],
        y=[0, 0, 0],
        mode='markers+text',
        text=['Secondary<br>Education', 'Higher<br>Secondary', 'Engineering<br>Degree'],
        textposition='top center',
        marker=dict(size=20, symbol='diamond', color=['#1976D2', '#1976D2', '#1976D2']),
    )])
    
    fig.update_layout(
        showlegend=False,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=True),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        plot_bgcolor='rgba(0,0,0,0)',
        paper_bgcolor='rgba(0,0,0,0)',
        height=200,
        margin=dict(l=0, r=0, t=30, b=30)
    )
    return fig

def show():
    # Header Section
    st.markdown("""
    <div style='text-align: center; padding: 2rem;'>
        <h1>🎓 Educational Journey</h1>
        <p style='color: #666;'>Building Strong Foundations in Technology and Engineering</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Educational Timeline
    st.plotly_chart(create_timeline(), use_container_width=True)
    
    # Engineering Degree
    with st.container():
        st.markdown("""
        <div style='background-color: #f0f2f6; padding: 1.5rem; border-radius: 10px;'>
        <h2>🎓 Bachelor of Engineering</h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
            ### Electronics and Communication Engineering
            #### VelTech MultiTech, Chennai
            
            🎯 **Academic Excellence**
            - CGPA: **8.2/10**
            - Graduated: August 2021
            
            #### Key Areas of Study
            - Communication Systems
            - Programming Fundamentals
            - Network Theory
            - Signal Processing
            """)
        
        with col2:
            # Academic Performance Metrics
            st.markdown("### Performance Metrics")
            st.progress(82, "Overall CGPA")
            st.progress(90, "Technical Subjects")
            st.progress(85, "Laboratory Work")
            
            st.markdown("""
            ### Skills Gained
            - Problem Solving
            - Technical Analysis
            - Project Management
            - Team Collaboration
            """)
    
    st.divider()
    
    # Higher Secondary Education
    with st.container():
        st.markdown("""
        <div style='background-color: #f0f2f6; padding: 1.5rem; border-radius: 10px;'>
        <h2>📚 Higher Secondary Education</h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
            ### P.A.K H.S School, Chennai
            #### Higher Secondary Certificate (HSC)
            
            🎯 **Academic Performance**
            - Percentage: **84.30%**
            - Graduated: May 2017
            
            #### Focus Areas
            - Mathematics
            - Computer Science
            """)
        
        with col2:
            st.markdown("### Subject Performance")
            st.progress(87, "Computer Science")
            st.progress(85, "Mathematics")
            
    
    st.divider()
    
    # Secondary Education
    with st.container():
        st.markdown("""
        <div style='background-color: #f0f2f6; padding: 1.5rem; border-radius: 10px;'>
        <h2>📝 Secondary Education</h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
            ### P.A.K H.S School, Chennai
            #### Secondary School Leaving Certificate (SSLC)
            
            🎯 **Academic Excellence**
            - Percentage: **92.86%**
            - Graduated: May 2015
            """)
        
        with col2:
            st.markdown("### Academic Highlights")
            st.progress(93, "Overall Performance")
            st.progress(100, "Mathematics")
            st.progress(90, "Science")
    
    st.divider()
    
    # Professional Certifications
    st.markdown("""
    ## 🏆 Professional Certifications
    """)
    
    cert_col1, cert_col2 = st.columns(2)
    
    with cert_col1:
        st.markdown("""
        ### Technical Certifications
        
        #### AWS Certified Cloud Practitioner
        - Credential ID: c2dc030a-0fe9-46b6-915e-1285e99bb1aa
        - Validates cloud expertise and AWS fundamentals
        
        #### Python and Django Framework
        - Complete Course Certification
        - Advanced web development concepts
        """)
    
    with cert_col2:
        st.markdown("""
        ### Specialized Training
        
        #### MongoDB M001 Certification
        - Database design and management
        - NoSQL database concepts
        
        #### Problem Solving (HackerRank)
        - Advanced algorithm implementation
        - Data structure optimization
        """)
    
    # Continuous Learning
    st.markdown("""
    ## 📚 Continuous Learning
    
    ### Current Focus Areas
    - Cloud Architecture and Design Patterns
    - Advanced System Design
    - DevOps Practices
    
    """)