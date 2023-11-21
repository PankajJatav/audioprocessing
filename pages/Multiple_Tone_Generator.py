import streamlit as st
import numpy as np
import sounddevice as sd

def generate_tone(frequency, duration, waveform='sine', volume=0.5, panning=0.5):
    t = np.linspace(0, duration, int(duration * 44100), False)
    if waveform == 'sine':
        return volume * np.sin(2 * np.pi * frequency * t)
    elif waveform == 'square':
        return volume * np.sign(np.sin(2 * np.pi * frequency * t))
    elif waveform == 'sawtooth':
        return volume * (2 * (frequency * t - np.floor(0.5 + frequency * t)))
    elif waveform == 'triangle':
        return volume * np.abs(2 * (frequency * t - np.floor(0.5 + frequency * t))) - 1

def play_tones(tones):
    sample_rate = 44100
    signal = np.zeros(1)
    
    for tone in tones:
        signal += generate_tone(tone['frequency'], tone['duration'], tone['waveform'],
                                 tone['volume'], tone['panning'])
    
    sd.play(signal, sample_rate)
    sd.wait()

def main():
    st.title("Multiple Tone Generator")

    num_tones = st.number_input("Number of Tones", min_value=1, value=1, step=1)

    tones = []

    for i in range(num_tones):
        st.subheader(f"Tone {i + 1}")
        frequency = st.number_input("Frequency (Hz)", min_value=20, value=440, step=1)
        duration = st.number_input("Duration (s)", min_value=0.1, value=1, step=0.1)
        waveform = st.selectbox("Waveform", ['sine', 'square', 'sawtooth', 'triangle'])
        volume = st.slider("Volume", min_value=0.0, max_value=1.0, value=0.5, step=0.01)
        panning = st.slider("Panning", min_value=0.0, max_value=1.0, value=0.5, step=0.01)

        tones.append({
            'frequency': frequency,
            'duration': duration,
            'waveform': waveform,
            'volume': volume,
            'panning': panning,
        })

    if st.button("Play Tones"):
        play_tones(tones)

if __name__ == "__main__":
    main()
