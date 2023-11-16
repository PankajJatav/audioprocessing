import streamlit as st
from streamlit.logger import get_logger
import numpy as np
LOGGER = get_logger(__name__)
import matplotlib.pyplot as plt
import librosa

def run():
    st.set_page_config(
        page_title="Sound",
        page_icon="👋",
    )

    st.write("# Welcome to Sound! 👋")

    st.sidebar.header("Sound")
    st.sidebar.write("Sound is a vibration that travels through the air or another medium and can be heard when it reaches our ears")
    st.sidebar.subheader("Frame rate")
    st.sidebar.write("Frame rate refers to the number of individual pictures (frames) shown in one second when we're watching a video or animation")
    st.sidebar.subheader("Amplitude")
    st.sidebar.write("Amplitude is the height or strength of a sound or a wave.")
    st.sidebar.subheader("Frequency")
    st.sidebar.write("Frequency is how fast something vibrates or repeats.")

    st.sidebar.success("A simple sin wave. Please feel free to explore to different values")

    st.session_state.sample_rate = st.slider('Sample Rate', 1, 2*44100, 44100)

    seconds = 5

    frequency_la = st.slider('Frequency', 1, 20000, 440)

    amplitude = st.slider('Amplitude', 0.0, 1.0, 0.1, step=0.1)

    t = np.linspace(0, seconds, seconds * st.session_state.sample_rate, False)

    st.session_state.note_la = amplitude * np.sin(frequency_la * t * 2 * np.pi)

    st.session_state.note_la = np.append(st.session_state.note_la, [1])

    st.line_chart(
        st.session_state.note_la[0:int(1 + 4*st.session_state.sample_rate/frequency_la)],
    )

    st.audio(st.session_state.note_la, sample_rate=st.session_state.sample_rate)

    fig = plt.figure(figsize=(10, 4))

    librosa.display.waveshow(st.session_state.note_la[:-1], sr=st.session_state.sample_rate, alpha=0.5)

    plt.title('Sine Wave')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    st.pyplot(fig)

if __name__ == "__main__":
    run()