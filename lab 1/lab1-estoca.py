import pyaudio 
import wave

FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
CHUNK = 1024
duracion = 4
archivo = "grabacion.wav"

def inicio():
    audio = pyaudio.PyAudio()
    stream=audio.open(format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK)
    #grabacion
    print("grabando....")
    frames = []
    for i in range(0, int(RATE/CHUNK*duracion)):
        data=stream.read(CHUNK)
        frames.append(data)
    print("grabacion terminada")
    #Detenemos grabacion
    stream.stop_stream()
    stream.close()
    audio.terminate()
    #crear y guardar
    waveFile = wave.open(archivo, "wb")
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b"".join(frames))
    waveFile.close()

inicio()