import streamlit as st
import os 
import moviepy.editor as mp
from PIL import Image
import numpy as np
import tempfile
import time

class watermakin_video():
    
    def __init__(self) -> None:
        # Setting page layout
        st.set_page_config(
            page_title="Watermarkin Video",  
            page_icon="📹", 
            layout="wide", 
            initial_sidebar_state="expanded", 
        )
        st.title("\tSelamat Datang di Watermarkin Video")
        st.caption('Watermarkin Video, me-watermark video jadi lebih mudah')

        self.upload_file()     
    
    def upload_file(self):
        self.uploaded_logo = st.file_uploader("Unggah file logo sebagai watermark", accept_multiple_files= False)

        self.uploaded_video = st.file_uploader("Unggah video yg ingin di-watermark", accept_multiple_files= False)     
        if self.uploaded_video:   
            
            if st.button("Watermark Video"):
                self.watermarking_video()
            
        else:
            st.write("Tolong unggah gambar logo dan video yg ingin di-watermark")
             
            
    def watermarking_video(self):
        self.col1, self.col2 = st.columns(2)
        self.logo = Image.open(self.uploaded_logo)
        self.logo = np.array(self.logo)
        
        self.tfile = tempfile.NamedTemporaryFile(delete=False) 
        self.tfile.write(self.uploaded_video.read())

        self.video = mp.VideoFileClip(self.tfile.name)
        self.file_name = 'video_watermarked'
        self.logo = (mp.ImageClip(self.logo)
                .set_duration(self.video.duration)
                .margin(left=0, bottom=60, opacity=0) # (optional) logo-border padding
                .set_pos(("left","bottom")))
            
        self.new_file_name = "{}.mp4".format(os.path.basename(self.file_name))
        self.final = mp.CompositeVideoClip([self.video, self.logo])

        st.write("Hasil video setelah watermark:")
        self.final.write_videofile(self.new_file_name)
        st.video(self.new_file_name)

        st.write("Video sudah di watermark, Yey!")
        time.sleep(10)
        os.remove(self.new_file_name)
        
                    
abc = watermakin_video()