from gtts import gTTS

tts = gTTS("Hello, audio test")
tts.save("test.mp3")

print("Audio saved")