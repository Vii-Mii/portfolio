import streamlit as st

def show():
    # Custom CSS for styling
    st.markdown("""
    <style>
        .tech-icon {
            width: 30px;
            height: 30px;
            margin: 5px;
            vertical-align: middle;
            transition: transform 0.2s;
        }
        .tech-icon:hover {
            transform: scale(1.2);
        }
        .skill-header {
            background-color: #f0f2f6;
            padding: 10px 15px;
            border-radius: 8px;
            margin: 15px 0;
            border-left: 4px solid #1E88E5;
            display: flex;
            align-items: center;
            gap: 10px;
        }
        .skill-content {
            background-color: #f8f9fa;
            padding: 15px;
            border-radius: 8px;
            margin: 10px 0;
            border: 1px solid #e0e0e0;
        }
        .skill-item {
            display: flex;
            align-items: center;
            margin: 8px 0;
            padding: 5px;
            transition: transform 0.2s;
        }
        .skill-item:hover {
            transform: translateX(5px);
            background-color: #f0f2f6;
            border-radius: 5px;
        }
    </style>
    """, unsafe_allow_html=True)
    
    # Page Title with Consistent Styling and Emoji
    st.markdown("""
        <div style='text-align: center; padding: 2rem;'>
        <h1>
            🛠️ Skills & Expertise
        </h1>
        <p style='color: #666;'>
            Leveraging modern technologies to build scalable solutions
            </p>
    """, unsafe_allow_html=True)
    
    # Overview Section
    with st.container():
        st.markdown("""
        """, unsafe_allow_html=True)
        
        # Metrics in columns with enhanced styling
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric(
                "Experience",
                "2+ Years",
                delta="↑1 in 2023",
                delta_color="normal"
            )
        
        with col2:
            st.metric(
                "Technologies",
                "15+",
                delta="↑5 in 2023",
                delta_color="normal"
            )
        
        with col3:
            st.metric(
                "Projects",
                "10+",
                delta="↑3 in 2023",
                delta_color="normal"
            )
    
    st.divider()
    
    # Technical Skills Section with Modern Layout
    st.markdown("""
    <h2 style='color: #1E88E5; margin-bottom: 1rem;'>💻 Technical Expertise</h2>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Core Technologies Section
        st.markdown("<h3 style='color: #333;'>Core Technologies</h3>", unsafe_allow_html=True)
        
        # Web Technologies
        st.markdown("""
        <div class="skill-header">
            <h4>Web Technologies</h4>
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original.svg" class="tech-icon" title="HTML5"/>
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original.svg" class="tech-icon" title="CSS3"/>
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" class="tech-icon" title="JavaScript"/>
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/react/react-original.svg" class="tech-icon" title="React"/>
        </div>
        <div class="skill-content">
            <div class="skill-item">🌐 HTML5/CSS3 - Modern Web Development</div>
            <div class="skill-item">💫 JavaScript - Dynamic Functionality</div>
            <div class="skill-item">⚛️ React - Interactive UI Components</div>
            <div class="skill-item">🎯 Django - Backend Framework</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Python Development
        st.markdown("""
        <div class="skill-header">
            <h4>Python Development</h4>
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" class="tech-icon"/>
            <img src="https://www.vectorlogo.zone/logos/numpy/numpy-icon.svg" class="tech-icon"/>
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/pandas/pandas-original.svg" class="tech-icon"/>
        </div>
        <div class="skill-content">
            <div class="skill-item">🔄 Data Processing & Analysis</div>
            <div class="skill-item">🔌 API Development & Integration</div>
            <div class="skill-item">🤖 Automation Scripts & Tools</div>
            <div class="skill-item">📊 ETL Pipeline Development</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Database Technologies
        st.markdown("""
        <div class="skill-header">
            <h4>Database Technologies</h4>
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg" class="tech-icon"/>
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original-wordmark.svg" class="tech-icon"/>
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/postgresql/postgresql-original.svg" class="tech-icon"/>
        </div>
        <div class="skill-content">
            <div class="skill-item">💾 MySQL - Relational Database</div>
            <div class="skill-item">🔶 MongoDB - NoSQL Database</div>
            <div class="skill-item">📊 Database Design & Modeling</div>
            <div class="skill-item">⚡ Query Optimization & Performance</div>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        # Cloud & Tools Section
        st.markdown("<h3 style='color: #333;'>Cloud & Tools</h3>", unsafe_allow_html=True)
        
        # AWS Cloud
        st.markdown("""
        <div class="skill-header">
            <h4>AWS Cloud</h4>
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg" class="tech-icon"/>
        </div>
        <div class="skill-content">
            <div class="skill-item">🖥️ EC2 - Virtual Servers</div>
            <div class="skill-item">📦 S3 - Cloud Storage</div>
            <div class="skill-item">🗄️ RDS - Database Services</div>
            <div class="skill-item">λ Lambda - Serverless Computing</div>
        </div>
        """, unsafe_allow_html=True)
        
        # Development Tools
        st.markdown("""
        <div class="skill-header">
            <h4>Development Tools</h4>
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/git/git-original.svg" class="tech-icon"/>
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg" class="tech-icon"/>
            <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/vscode/vscode-original.svg" class="tech-icon"/>
        </div>
        <div class="skill-content">
            <div class="skill-item">📚 Git - Version Control</div>
            <div class="skill-item">🐳 Docker - Containerization</div>
            <div class="skill-item">🔄 Jenkins - CI/CD Pipeline</div>
            <div class="skill-item">💻 VS Code - Development IDE</div>
        </div>
        """, unsafe_allow_html=True)
        
        # API & Integration with icon
        st.markdown("""
        <div class="skill-header">
            <h4>API & Integration</h4>
            <img src="https://www.vectorlogo.zone/logos/getpostman/getpostman-icon.svg" class="tech-icon"/>
        </div>
        <div class="skill-content">
            <div class="skill-item"> 🔌 RESTful APIs</div>
            <div class="skill-item"> 📄 XML Processing</div>
            <div class="skill-item"> 📐 API Design</div>
            <div class="skill-item"> 🔄 Integration Patterns</div>
        </div>
        """, unsafe_allow_html=True)
        
    
    st.divider()
    
    # Professional Skills Section
    st.markdown("""
    <h2 style='color: #1E88E5; margin: 2rem 0 1rem 0;'>👥 Professional Skills</h2>
    """, unsafe_allow_html=True)
    
    col3, col4 = st.columns(2)
    
    with col3:
        st.markdown("""
        <div class="skill-header">
            <h4>Process Management</h4>
        </div>
        <div class="skill-content">
            <div class="skill-item">🎯 Incident Management</div>
            <div class="skill-item">🔄 Change Management</div>
            <div class="skill-item">🔍 Problem Management</div>
            <div class="skill-item">📋 ITIL Framework</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col4:
        st.markdown("""
        <div class="skill-header">
            <h4>Leadership & Communication</h4>
        </div>
        <div class="skill-content">
            <div class="skill-item">👥 Team Collaboration</div>
            <div class="skill-item">📢 Stakeholder Management</div>
            <div class="skill-item">📊 Resource Planning</div>
            <div class="skill-item">👨‍💻 Technical Mentoring</div>
        </div>
        """, unsafe_allow_html=True)
    
   