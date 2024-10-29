import librosa
import numpy as np
import matplotlib.pyplot as plt

# بارگذاری فایل صوتی
audio_file = 'sample_audio.wav'  # فایل صوتی خودت را جایگزین کن
y, sr = librosa.load(audio_file, sr=None)

# نمایش شکل موج
plt.figure(figsize=(12, 4))
librosa.display.waveshow(y, sr=sr)
plt.title('شکل موج صوت')
plt.show()
