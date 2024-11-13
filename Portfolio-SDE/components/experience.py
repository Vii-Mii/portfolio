import streamlit as st

def show():
    # Professional Journey Timeline
    
    
    # Header with animation
    st.markdown("""
    <div style='text-align: center; padding: 2rem;'>
        <h1>💼 Professional Journey</h1>
        <p style='color: #666;'>Building, Optimizing, and Transforming</p>
    </div>
    """, unsafe_allow_html=True)
    st.markdown("""
    ### 🚀 Professional Journey
    <div style='background-color: #f8f9fa; padding: 1.5rem; border-radius: 10px; margin-top: 1rem;'>
        <div style='display: flex; align-items: center; margin-bottom: 1rem;'>
            <div style='background-color: #1E88E5; width: 12px; height: 12px; border-radius: 50%; margin-right: 1rem;'></div>
            <div>
                <strong>2022 - Present</strong>: Application Archival Service Specialist
                <br><small style='color: #666;'>Advanced to leading complex archival projects</small>
            </div>
        </div>
        <div style='display: flex; align-items: center;'>
            <div style='background-color: #4CAF50; width: 12px; height: 12px; border-radius: 50%; margin-right: 1rem;'></div>
            <div>
                <strong>2021 - 2022</strong>: Technical Analyst
                <br><small style='color: #666;'>Started journey in database management and automation</small>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    st.divider()
    
    # Current Role
    with st.container():
        st.markdown("""
        <div style='background-color: #f0f2f6; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #1E88E5;'>
        <h3>Application Archival Service Specialist | HCLTECH</h3>
        <p style='color: #666;'>Aug 2022 - Present | Chennai, India</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
            #### 🎯 Key Achievements
            
            - 📈 **Data Optimization Impact**
              - Managed 30+ legacy, GxP, and non-GxP applications
              - Reduced retrieval times by 40%
              - Enhanced regulatory compliance measures
            
            - 🔄 **Process Automation**
              - Implemented automated archival on Serrala CDN
              - Reduced manual data handling by 60%
              - Achieved 20% storage cost reduction
            
            - 👥 **Leadership & Implementation**
              - Led cross-functional team initiatives
              - Improved user access efficiency by 25%
              - Delivered end-to-end project enhancements
            
            - 🔒 **Compliance & Security**
              - Established secure data access protocols
              - Cut audit preparation time by 30%
              - Ensured GxP compliance standards
            """)
        
        with col2:
            st.markdown("""
            #### 💻 Tech Stack
            <div style='background-color: #f8f9fa; padding: 1rem; border-radius: 5px;'>
            <p><img src='https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg' 
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> Python</p>
            
            <p><img src='https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg'
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> MySQL</p>
            
            <p><img src='https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original.svg'
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> MongoDB</p>
            
            <p><img src='https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg'
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> Pandas</p>
            
            <p><img src='https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg'
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> Git</p>
            </div>

            #### 📊 Impact Metrics
            <div style='background-color: #f8f9fa; padding: 1rem; border-radius: 5px; margin-top: 1rem;'>
            <p>🎯 Applications Managed: <b>30+</b></p>
            <p>⚡ Performance Gain: <b>40%</b></p>
            <p>💹 Cost Reduction: <b>20%</b></p>
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    # Previous Role
    with st.container():
        st.markdown("""
        <div style='background-color: #f0f2f6; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #4CAF50;'>
        <h3>Technical Analyst | HCLTECH</h3>
        <p style='color: #666;'>Oct 2021 - Aug 2022 | Chennai, India</p>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
            #### 🎯 Key Achievements
            
            - 🔍 **Database Management**
              - Developed automated SQL monitoring scripts
              - Achieved 99.9% data integrity
              - Reduced error-handling time by 50%
            
            - 📊 **Process Automation**
              - Automated data extraction and reporting
              - Cut report delivery time by 50%
              - Enhanced stakeholder decision-making
            
            - 🔒 **Security Enhancement**
              - Implemented robust access controls
              - Minimized unauthorized access risks
              - Strengthened data security protocols
            """)
        
        with col2:
            st.markdown("""
            #### 🛠️ Tools & Platforms
            <div style='background-color: #f8f9fa; padding: 1rem; border-radius: 5px;'>
            <p><img src='https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original.svg'
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> MySQL</p>
            
            <p><img src='https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg'
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> Python</p>
            
            <p><img src='https://www.vectorlogo.zone/logos/servicenow/servicenow-icon.svg'
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> ServiceNow</p>
            
            <p><img src='https://www.vectorlogo.zone/logos/atlassian_jira/atlassian_jira-icon.svg'
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> Serrala</p>
            </div>

            #### 📈 Performance Metrics
            <div style='background-color: #f8f9fa; padding: 1rem; border-radius: 5px; margin-top: 1rem;'>
            <p>🎯 Data Integrity: <b>99.9%</b></p>
            <p>⚡ Time Reduction: <b>50%</b></p>
            <p>🔒 Security Score: <b>95%</b></p>
            </div>
            """, unsafe_allow_html=True)
    
    st.divider()
    
    