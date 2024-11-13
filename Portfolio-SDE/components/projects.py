import streamlit as st

def show():
    # Header Section
    st.markdown("""
    <div style='text-align: center; padding: 2rem;'>
        <h1>🚀 Technical Projects</h1>
        <p style='color: #666;'>From Concept to Deployment: Building Solutions that Matter</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Project Metrics Overview
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total Projects", "10+", "↑2 in 2023")
    with col2:
        st.metric("Success Rate", "95%", "↑5%")
    with col3:
        st.metric("Code Quality", "A+", "↑10%")
    
    st.divider()
    
    # Project 1: DataSyncX
    with st.container():
        st.markdown("""
        <div style='background-color: #f0f2f6; padding: 1.5rem; border-radius: 10px;'>
        <h2>🔄 DataSyncX | Enterprise Data Synchronization Solution</h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
            #### Project Overview
            DataSyncX is a state-of-the-art Device History Record (DHR) processing and synchronization platform, designed specifically for medical device manufacturers and healthcare industries worldwide. This enterprise-grade solution streamlines the critical process of managing, validating, and archiving Device History Records, ensuring compliance with global regulatory requirements including FDA 21 CFR Part 11 and ISO 13485.

            
            #### 🎯 Key Features
            - 📊 **Real-time Monitoring**
              - Live DHR processing status
              - Performance metrics visualization
              - Error tracking and reporting
            - 🔄 **Processing Engine**
              - Automated data validation
              - Error detection and handling
              - Batch processing capabilities
            - 📈 **Analytics Dashboard**
              - Interactive charts and graphs
              - Historical trend analysis
              - Custom report generation
            
            #### 🛠️ Technical Implementation
            - Built with Python, Streamlit, and MongoDB
            - Implemented role-based access control
            - Developed automated notification system
            - Created interactive data visualization
            
            #### 📈 Impact
            - Enhanced processing efficiency
            - Improved data validation accuracy
            - Real-time monitoring capabilities
            - Streamlined reporting process
            """)
        
        with col2:
            # Project Links with Buttons
            st.markdown("#### 🔗 Project Links")
            
            # Using columns for button alignment
            link_col1, link_col2 = st.columns(2)
            with link_col1:
                st.markdown("""
                <a href='https://github.com/Vii-Mii/DataSyncX' target='_blank'>
                    <button style='
                        background-color: #24292e;
                        color: white;
                        padding: 8px 15px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        width: 100%;
                        margin: 5px 0;
                    '>
                        <img src='https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png' 
                        style='width: 20px; vertical-align: middle; margin-right: 5px;'>
                        GitHub
                    </button>
                </a>
                """, unsafe_allow_html=True)
                
            with link_col2:
                st.markdown("""
                <a href='https://datasyncx-monitor.streamlit.app/' target='_blank'>
                    <button style='
                        background-color: #0066cc;
                        color: white;
                        padding: 8px 15px;
                        border: none;
                        border-radius: 5px;
                        cursor: pointer;
                        width: 100%;
                        margin: 5px 0;
                    '>
                        <img src='https://cdn-icons-png.flaticon.com/512/1150/1150626.png' 
                        style='width: 20px; vertical-align: middle; margin-right: 5px;'>
                        Live Demo
                    </button>
                </a>
                """, unsafe_allow_html=True)

            st.markdown("""
            > **Demo Credentials:**
            > - Username: vijay | Password: datasyncx
            > - Username: suriya | Password: datasyncx
            """)
            
            # Tech Stack with icons
            st.markdown("""
            #### 💻 Tech Stack
            <div style='background-color: #f8f9fa; padding: 1rem; border-radius: 5px;'>
            <p><img src='https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg' 
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> Python 3.9</p>
            
            <p><img src='https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original.svg'
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> MongoDB Atlas</p>
            
            <p><img src='https://docs.streamlit.io/logo.svg'
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> Streamlit</p>
            
            <p><img src='https://raw.githubusercontent.com/devicons/devicon/master/icons/docker/docker-original.svg'
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> Docker</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Performance Metrics
            st.markdown("#### 📊 Performance Metrics")
            st.progress(95, "System Reliability")
            st.progress(90, "Processing Speed")
            st.progress(98, "Data Accuracy")
    
    st.divider()
    
    # Project 2: IDMS
    with st.container():
        st.markdown("""
        <div style='background-color: #f0f2f6; padding: 1.5rem; border-radius: 10px;'>
            <h2>🗄️ IDMS | Large-Scale Data Organization</h2>
        </div>
        """, unsafe_allow_html=True)
        
        col1, col2 = st.columns([2,1])
        with col1:
            st.markdown("""
            #### Project Overview
            A comprehensive data organization system handling millions of records, focusing on 
            efficient data storage, retrieval, and cross-format compatibility. Built with modern 
            technologies and cloud infrastructure.
            
            #### 🎯 Key Achievements
            - 📊 **Data Architecture**
              - Engineered scalable architecture for 3M+ records
              - Implemented on Serrala CDN platform
              - Streamlined data access and retrieval
            
            - 🔍 **Performance Optimization**
              - Reduced query times by 40%
              - Enhanced data accessibility
              - Improved cross-team usability
            
            - 🔄 **System Integration**
              - Implemented XML/JSON compatibility
              - Enabled seamless data exchange
              - Integrated with legacy systems
            
            #### 🛠️ Technical Implementation
            - Designed optimized table structures
            - Created cross-format data handlers
            - Implemented cloud-based storage solutions
            - Built efficient data retrieval systems
            
            #### 📈 Impact
            - 40% faster query response
            - Enhanced data accessibility
            - Improved system integration
            - Streamlined data workflows
            """)
        
        with col2:
            # Tech Stack with icons
            st.markdown("""
            #### 💻 Tech Stack
            <div style='background-color: #f8f9fa; padding: 1rem; border-radius: 5px;'>
            <p><img src='https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg' 
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> Python 3.9</p>
            
            <p><img src='https://raw.githubusercontent.com/devicons/devicon/master/icons/mongodb/mongodb-original.svg'
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> MongoDB Atlas</p>
            
            <p><img src='https://raw.githubusercontent.com/devicons/devicon/master/icons/amazonwebservices/amazonwebservices-original-wordmark.svg'
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> AWS</p>
            
            <p><img src='https://raw.githubusercontent.com/devicons/devicon/master/icons/mysql/mysql-original-wordmark.svg'
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> MySQL</p>
            
            <p><img src='https://www.vectorlogo.zone/logos/w3c_xml/w3c_xml-icon.svg'
            style='width: 20px; vertical-align: middle; margin-right: 5px;'> XML/JSON</p>
            </div>
            """, unsafe_allow_html=True)
            
            # Performance Metrics
            st.markdown("#### 📊 Performance Metrics")
            st.progress(90, "Query Optimization")
            st.progress(85, "Data Processing")
            st.progress(95, "System Integration")
            
            
    
   