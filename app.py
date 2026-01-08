#*Imports
from youtube_transcript_api import YouTubeTranscriptApi
import os
from dotenv import load_dotenv
load_dotenv()
GROQ_API_KEY=os.getenv('GROQ_API_KEY')

class YoutubeSummarizer:
    def __init__(self,yt_url):
        print(f'Generatinf Summary for {yt_url}')
        self.yt_url=yt_url
        self.video_id=self.extract_video_id(yt_url)
        self.filename=f'summary_{self.video_id}.md'
        if self.ensure_new():
            self.transcript=self.fetch_transcript( )
            self.summary=self.create_ai_summary()
            self.save_md()
    @property
    def prompt(self):
        return """
            Create a summary of a youtube video based on provided transcript.
            the goal is to extract as much value as possible with clarity and insights over quantity.
            provide the answer in a raw markdown syntax, suitable for notion,with no extra commentary or explanations.
            Highlight the following sections cleary:
            - the main message(the core idea of the video)
            - 3-5 key takeaways
            - short overall summary
            - clear steps to implement the ideas taught in the video(If applicable)

            Here is the transcript:
            """

    def ensure_new(self):
        if os.path.exists(self.filename):
            print(f'Video summary already exists : {self.filename}')
            return False
        return True

    def extract_video_id(self,url):
        '''Extract video id from youtube url links.
            Works for both youtube.com and youtu.be formats.
            :param url: Youtube url
            :return : video ID from youtube
        '''
        if 'youtube.com' in url:
            return url.split('?v=')[-1].split('&')[0]
        elif'youtu.be' in url:
            return url.split('.be/')[-1].split('?')[0]
        
        raise ValueError(f'Invalid URL : {url}')
    
    def fetch_transcript(self,):
        ''' 
        :param: video ID
        :return : full transcript of video
        '''
        #* fetch transcription
        yt_api=YouTubeTranscriptApi()
        yt_trans=yt_api.fetch(self.video_id)

        #* get full transcript
        list_transcript=[t.text for t in yt_trans]
        full_transcript=' '.join(list_transcript)
        return full_transcript
 
    def create_ai_summary(self):
        #*prepare ai prompt
        prompt=self.prompt+self.transcript

        #*ASK AI:
        from groq import Groq
        client = Groq(api_key=GROQ_API_KEY)
        response = client.chat.completions.create(
            model='llama-3.3-70b-versatile',
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2048
        )
        output=response.choices[0].message.content

        #* DISPLAY RESULT
        print('AI summary')
        print(output)

        return output
    
    def save_md(self):
        with open(self.filename,'w')as f:
            f.write(self.summary)

# This class can now be imported and used by streamlit_app.py
