import streamlit as st
import requests
from streamlit_lottie import st_lottie


def loteeloader(url):
    r = requests.get(url)
    if r.status_code !=200:
        return None
    else:
        return r.json()
def main():
    # Set layout to wide
    st.set_page_config(layout="wide")

    # Title and small descriptions
    st.subheader("Welcome to a fantastic exploration!")
    st.title("Awesome Streamlit Website")
    st.subheader("Welcome to a fantastic exploration!")
    st.write('Hay this is my webpage')
    # Define your scenes
    scenes = ["Scene 1", "Scene 2", "Scene 3"]
    selected_scene = st.sidebar.selectbox("Select Scene", scenes)

    # Layout with two columns for each scene
    if selected_scene == "Scene 1":
        scene_1()
    elif selected_scene == "Scene 2":
        scene_2()
    elif selected_scene == "Scene 3":
        scene_3()
lottie_img = loteeloader('https://lottie.host/6c16c871-0547-4ee5-80b3-c4323a412c46/J9mFbrzlYR.json')
def scene_1():
    st.write("Scene 1 Content")
    with st.container():
        st.write('---')
        # Two columns layout
        col1, col2 = st.columns(2)


        # Left column with picture
        col1.image("https://www.linearity.io/blog/content/images/size/…webp/2023/06/how-to-create-a-car-NewBlogCover.png", caption="Left Picture", use_column_width=True)

        # Right column with explanation
        with col2:
            st_lottie(lottie_img)
            st.write("Scene 1 Content")
    # Two columns layout
    col1, col2 = st.columns(2)


    # Left column with picture
    col1.image("https://www.linearity.io/blog/content/images/size/…webp/2023/06/how-to-create-a-car-NewBlogCover.png", caption="Left Picture", use_column_width=True)

    # Right column with explanation
    col2.write("Explanation for Scene 1")

def scene_2():
    st.write("Scene 2 Content")
    col1, col2 = st.beta_columns(2)
    col1.image("https://www.linearity.io/blog/content/images/size/…webp/2023/06/how-to-create-a-car-NewBlogCover.png", caption="Left Picture", use_column_width=True)
    col2.write("Explanation for Scene 2")

def scene_3():
    st.write("Scene 3 Content")
    col1, col2 = st.beta_columns(2)
    col1.image("https://www.linearity.io/blog/content/images/size/…webp/2023/06/how-to-create-a-car-NewBlogCover.png", caption="Left Picture", use_column_width=True)
    col2.write("Explanation for Scene 3")

if __name__ == "__main__":
    main()
