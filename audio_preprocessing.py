import librosa 
def segment_audio(file='./test_audio/harvard.wav'):
    audio_data, sample_rate = librosa.load(file, sr= None)
    