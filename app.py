import streamlit as st
import os
from classfinder import getclass
from queryprocessor import get_name_color,itself 
from corecode import findinstant
from colormodule import coloredobject
import tempfile

def process_videos(video_path, user_query,slider_value):
    #objects,colors=itself(user_query)
    objects,colors=get_name_color(user_query)
    print(objects,'...........',colors)
    cls=getclass(objects)
    print('class:', cls)
    if len(cls)==0:
        return ['object not in dataset']
    if len(colors)==0:
        lists,oplist=findinstant(video_path,cls,slider_value)
    else:
        oplist=coloredobject(video_path,cls,colors,slider_value)
    return oplist
    
  

def view_folder_videos(folder_path):
    """Displays a list of video files in the specified folder (optional)."""
    if folder_path and os.path.isdir(folder_path):
        filenames = os.listdir(folder_path)
        st.subheader("Files in the specified folder:")
        for filename in filenames:
            if filename.endswith(('.mp4', '.avi', '.mov')):  # Check for common video extensions
                st.write(filename)
    else:
        st.warning("Invalid folder path or folder does not exist.") if folder_path else st.write("No folder path provided.")

def app():
    # User input for search query (optional)
    st.subheader(" Video Moment Retrieval System")
    user_query = st.text_input("Enter your search query for videos:")
    slider_value = st.slider("Confidence value between 0.1 and 1:", 0.1, 1.0, step=0.1,value=0.5)  # Step adjusted for finer control


    # File selection for processing (multiple selection allowed)
    uploaded_files = st.file_uploader("Select video files to process:", accept_multiple_files =True, type=".mp4")

    if st.button("Submit"):
        if uploaded_files:
            all_outputs = []
            for uploaded_file in uploaded_files:
                with tempfile.TemporaryDirectory() as temp_dir:
                    path = os.path.join(temp_dir, uploaded_file.name)
                    with open(path, "wb") as f:
                        f.write(uploaded_file.getvalue())

                    oplist = process_videos(path, user_query,slider_value)
                    all_outputs.append((uploaded_file.name,oplist))
                    # Store results with filename

            st.subheader(" Output in hr min sec ")
            for filename, oplist in all_outputs:
                st.write(f"**File:** {filename}")
                st.text_area("", value="".join(str(oplist)), height=200)  # Multi-line output

            else:
                st.warning("Please select video files.")

if __name__ == "__main__":
  app()
