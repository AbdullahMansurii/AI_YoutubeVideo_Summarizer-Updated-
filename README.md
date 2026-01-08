# 🎥 YouTube AI Summarizer

Transform any YouTube video into a concise, actionable summary powered by Groq AI.

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/Groq-000000?style=for-the-badge&logo=ai&logoColor=white)

## ✨ Features

- 🚀 **Fast AI Summaries** - Powered by Groq's LPU for lightning-fast inference
- 🎯 **Smart Extraction** - Automatically extracts key takeaways and actionable steps
- 🎨 **Modern UI** - Beautiful dark theme with emerald green accents
- 📥 **Export Summaries** - Download summaries as Markdown files
- 🔒 **Secure** - API keys stored safely in environment variables

## 🖼️ Preview

The app features a modern dark slate theme with emerald green accents for excellent readability and a premium feel.

## 🚀 Quick Start

### Prerequisites

- Python 3.8+
- Groq API Key ([Get one here](https://console.groq.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/AbdullahMansurii/AI_YoutubeVideo_Summarizer-Updated-.git
   cd AI_YoutubeVideo_Summarizer-Updated-
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

4. **Run the application**
   ```bash
   streamlit run streamlit_app.py
   ```

5. **Open your browser**
   
   The app will automatically open at `http://localhost:8501`

## 📖 How to Use

1. **Paste YouTube URL** - Enter any YouTube video URL in the input field
2. **Generate Summary** - Click the "✨ Generate Summary" button
3. **Wait for Processing** - The app fetches the transcript and generates a summary (30-60 seconds)
4. **View Results** - Summary displays with:
   - Main message/core idea
   - 3-5 key takeaways
   - Overall summary
   - Implementation steps (if applicable)
5. **Download** - Click "📥 Download Summary" to save as `.md` file

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **AI Model**: Groq (llama-3.3-70b-versatile)
- **Transcript API**: youtube-transcript-api
- **Language**: Python 3.8+

## 📁 Project Structure

```
YT_Summarizer_AI/
├── streamlit_app.py      # Main Streamlit application
├── app.py                # YouTube summarizer core logic
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (not tracked)
├── .gitignore           # Git ignore rules
└── README.md            # This file
```

## 🎨 UI Design

### Color Scheme
- **Background**: Dark slate (`#0f172a` → `#1e293b`)
- **Primary Accent**: Emerald green (`#10b981`)
- **Secondary Accent**: Cyan (`#06b6d4`)
- **Text**: Light slate (`#e2e8f0`)

### Typography
- **Headings**: Space Grotesk
- **Body**: Inter

## 🔐 Security

- API keys are stored in `.env` file (excluded from Git)
- Never commit your `.env` file to version control
- The `.gitignore` file ensures sensitive data stays local

## 📝 Summary Format

Each generated summary includes:

- **Main Message**: The core idea of the video
- **Key Takeaways**: 3-5 important points
- **Overall Summary**: Concise overview
- **Implementation Steps**: Actionable steps (when applicable)

## 🚀 Deployment

### Streamlit Cloud (Recommended)

1. Push your code to GitHub
2. Go to [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your repository
4. Add `GROQ_API_KEY` to secrets
5. Deploy!

### Other Options
- Heroku
- AWS/GCP/Azure
- Docker containers

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

**Abdullah Mansuri**
- GitHub: [@AbdullahMansurii](https://github.com/AbdullahMansurii)

## 🙏 Acknowledgments

- [Groq](https://groq.com/) for the amazing LPU and AI models
- [Streamlit](https://streamlit.io/) for the awesome framework
- [YouTube Transcript API](https://github.com/jdepoix/youtube-transcript-api) for transcript extraction

---

⭐ If you find this project useful, please consider giving it a star!
