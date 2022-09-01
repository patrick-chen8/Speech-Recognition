# we are testing random shit LOL

# Audio signal parameters
# - numbner of channels
# - sample width
# - framerate/sample_rate: 44,100 Hz or 44.1 kHz
# - number of frames
# - values of a frame


from sys import set_asyncgen_hooks
import wave
obj = wave.open("Test.wav", "rb")

print("Number of channels", obj.getnchannels())
print("Sample width", obj.getsampwidth())
print("Frame rate", obj.getframerate())
print("Number of frame", obj.getnframes())
print("parameters", obj.getparams())


t_audio = obj.getnframes() / obj.getframerate()
print (t_audio)

frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames) / 2)

obj.close()

obj_new = wave.open("test_new.wav", "wb")

obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(48000)

obj_new.writeframes(frames)

obj_new.close()
