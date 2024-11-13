import numpy as np
import pyaudio
from matplotlib import pyplot as plt


class Sound:
    stream = None

    FORMAT = pyaudio.paInt16  # 16-битный формат
    CHANNELS = 1  # Моно
    RATE = 44100  # Частота дискретизации
    CHUNK = 2048  # Размер блока данных

    def __init__(self):
        self.p = pyaudio.PyAudio()

    def start_recording(self):
        self.stream = self.p.open(format=self.FORMAT,
                                  channels=self.CHANNELS,
                                  rate=self.RATE,
                                  input=True,
                                  frames_per_buffer=self.CHUNK)

    def stop_recording(self):
        self.stream.stop_stream()
        self.stream.close()
        self.p.terminate()


class Processing:
    audio_data = None
    peak_freq = None

    def __init__(self, stream, CHUNK, RATE):
        self.stream = stream
        self.CHUNK = CHUNK
        self.RATE = RATE

    def get_data(self):
        data = self.stream.read(self.CHUNK)
        self.audio_data = np.frombuffer(data, dtype=np.int16)
        return self.audio_data

    def frequency_decomposition(self):
        fft_data = np.fft.fft(self.audio_data)
        fft_magnitude = np.abs(fft_data)

        # plt.ion()
        # plt.clf()
        # plt.plot(fft_magnitude)
        # plt.pause(0.05)

        # Получение частоты
        freq = np.fft.fftfreq(len(fft_magnitude), 1 / self.RATE)
        self.peak_freq = freq[np.argmax(fft_magnitude)]

        return self.peak_freq
