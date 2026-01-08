import streamlit as st
from app import YoutubeSummarizer
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Page configuration
st.set_page_config(
    page_title="YouTube AI Summarizer",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for premium styling - Modern Dark Theme
st.markdown("""
<style>
    /* Import modern fonts */
    @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap');
    
    /* Global styles */
    * {
        font-family: 'Inter', sans-serif;
    }
    
    /* Main container - Dark slate background */
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e293b 50%, #0f172a 100%);
        color: #e2e8f0;
    }
    
    /* Header styling */
    h1 {
        font-family: 'Space Grotesk', sans-serif;
        background: linear-gradient(135deg, #10b981 0%, #34d399 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 700;
        text-align: center;
        font-size: 3.5rem !important;
        margin-bottom: 0.5rem;
        text-shadow: 0 0 40px rgba(16, 185, 129, 0.3);
    }
    
    .subtitle {
        text-align: center;
        color: #94a3b8;
        font-size: 1.2rem;
        margin-bottom: 2rem;
        font-weight: 400;
    }
    
    /* Input container */
    .stTextInput > div > div > input {
        background: #1e293b !important;
        border: 2px solid #334155 !important;
        border-radius: 12px;
        padding: 14px 18px;
        font-size: 1rem;
        color: #e2e8f0 !important;
        transition: all 0.3s ease;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #10b981 !important;
        box-shadow: 0 0 0 3px rgba(16, 185, 129, 0.2) !important;
        background: #0f172a !important;
    }
    
    .stTextInput > div > div > input::placeholder {
        color: #64748b !important;
    }
    
    /* Button styling - Emerald green */
    .stButton > button {
        background: linear-gradient(135deg, #10b981 0%, #059669 100%) !important;
        color: white !important;
        border: none;
        border-radius: 12px;
        padding: 14px 32px;
        font-size: 1.05rem;
        font-weight: 600;
        width: 100%;
        transition: all 0.3s ease;
        box-shadow: 0 4px 20px rgba(16, 185, 129, 0.4);
    }
    
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 30px rgba(16, 185, 129, 0.6);
        background: linear-gradient(135deg, #059669 0%, #047857 100%) !important;
    }
    
    /* Download button - Cyan accent */
    .stDownloadButton > button {
        background: linear-gradient(135deg, #06b6d4 0%, #0891b2 100%) !important;
        color: white !important;
        border: none;
        border-radius: 12px;
        padding: 12px 28px;
        font-size: 0.95rem;
        font-weight: 600;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(6, 182, 212, 0.4);
    }
    
    .stDownloadButton > button:hover {
        background: linear-gradient(135deg, #0891b2 0%, #0e7490 100%) !important;
        transform: translateY(-2px);
        box-shadow: 0 6px 25px rgba(6, 182, 212, 0.6);
    }
    
    /* Success/Error messages */
    .stSuccess {
        background-color: rgba(16, 185, 129, 0.1) !important;
        border: 1px solid #10b981 !important;
        border-radius: 12px;
        padding: 1rem;
        color: #34d399 !important;
    }
    
    .stError {
        background-color: rgba(239, 68, 68, 0.1) !important;
        border: 1px solid #ef4444 !important;
        border-radius: 12px;
        padding: 1rem;
        color: #f87171 !important;
    }
    
    .stInfo {
        background-color: rgba(59, 130, 246, 0.1) !important;
        border: 1px solid #3b82f6 !important;
        border-radius: 12px;
        padding: 1rem;
        color: #60a5fa !important;
    }
    
    /* Markdown content styling */
    .stMarkdown {
        color: #e2e8f0 !important;
    }
    
    .stMarkdown h3 {
        color: #10b981 !important;
        font-family: 'Space Grotesk', sans-serif;
        margin-top: 1.5rem;
        margin-bottom: 1rem;
    }
    
    .stMarkdown h4 {
        color: #34d399 !important;
    }
    
    .stMarkdown p, .stMarkdown li {
        color: #cbd5e1 !important;
        line-height: 1.7;
    }
    
    .stMarkdown strong {
        color: #e2e8f0 !important;
    }
    
    .stMarkdown code {
        background: #1e293b !important;
        color: #10b981 !important;
        padding: 2px 6px;
        border-radius: 4px;
    }
    
    /* Divider */
    hr {
        border-color: #334155 !important;
        margin: 2rem 0;
    }
    
    /* Spinner */
    .stSpinner > div {
        border-top-color: #10b981 !important;
    }
    
    /* Footer text */
    .footer-text {
        text-align: center;
        color: #64748b;
        font-size: 0.9rem;
        margin-top: 3rem;
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("# 🎥 YouTube AI Summarizer")
st.markdown('<p class="subtitle">Transform any YouTube video into a concise, actionable summary powered by AI</p>', unsafe_allow_html=True)

# Create two columns for better layout
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    # Input field
    youtube_url = st.text_input(
        "YouTube URL",
        placeholder="https://www.youtube.com/watch?v=...",
        label_visibility="collapsed",
        help="Paste any YouTube video URL here"
    )
    
    # Generate button
    generate_button = st.button("✨ Generate Summary", use_container_width=True)

# Process the video when button is clicked
if generate_button:
    if not youtube_url:
        st.error("⚠️ Please enter a YouTube URL")
    elif "youtube.com" not in youtube_url and "youtu.be" not in youtube_url:
        st.error("⚠️ Please enter a valid YouTube URL")
    else:
        try:
            with st.spinner("🔄 Fetching transcript and generating summary... This may take a minute."):
                # Create summarizer instance
                summarizer = YoutubeSummarizer(youtube_url)
                
                # Check if summary was generated
                if summarizer.summary:
                    st.success("✅ Summary generated successfully!")
                    
                    # Display summary in a nice container
                    st.markdown("---")
                    st.markdown("### 📝 Summary")
                    st.markdown(summarizer.summary)
                    
                    # Download button
                    st.download_button(
                        label="📥 Download Summary",
                        data=summarizer.summary,
                        file_name=f"summary_{summarizer.video_id}.md",
                        mime="text/markdown",
                        use_container_width=True
                    )
                else:
                    st.error("❌ Failed to generate summary. Please try again.")
                    
        except ValueError as e:
            st.error(f"❌ Invalid URL: {str(e)}")
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.info("💡 Tip: Make sure the video has captions/subtitles available")

# Footer
st.markdown("---")
st.markdown(
    '<p class="footer-text">Powered by Groq AI • Built with Streamlit</p>',
    unsafe_allow_html=True
)
