from sound_processing import Sound, Processing
from config import Config
import numpy as np
import keyboard as k


if __name__ == "__main__":
    sound = Sound()
    sound.start_recording()     # Начало записи

    processing = Processing(sound.stream, sound.CHUNK, sound.RATE)

    config = Config()

    # keyboard = {
    #     323: "a",
    #     495: "d",
    #     388: "w",
    #     301: "s",
    #     215: "c",
    #     237: "z",
    #     172: "up",
    #     409: "down",
    #     258: "right",
    #     345: "left",
    # }

    frequency_play = 0
    key_frequency_play = False

    try:
        while True:
            processing.get_data()

            if np.log10(np.sqrt(np.mean(processing.audio_data ** 2)) ** 2) * 20 > config.min_volume:   # фильтруем тихий звук
                peak_freq = round(processing.frequency_decomposition())     # Находим главную частоту и округляем ее
            else:
                peak_freq = 0
                # print(4)

            if peak_freq >= config.min_hz:  # фильтруем низкие частоты
                print(f"Частота: {peak_freq}Гц")
                if peak_freq in config.keyboard.keys():
                    if peak_freq != frequency_play:
                        print(1)
                        print(config.keyboard[peak_freq])

                        if frequency_play != 0:
                            k.release(config.keyboard[frequency_play])

                        k.press(config.keyboard[peak_freq])
                        frequency_play = peak_freq
                        key_frequency_play = True

            if key_frequency_play and peak_freq >= 0 and not(peak_freq in config.keyboard.keys()):
                print(3)
                key_frequency_play = False
                k.release(config.keyboard[frequency_play])
                frequency_play = 0

    except:
        print("Остановка.")
        sound.start_recording()
