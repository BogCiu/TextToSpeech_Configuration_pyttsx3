import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty("voices")
for single_voice in voices:
    if single_voice.__str__().upper().__contains__("FR"):
        single_voice_name = single_voice.name.__str__().split(' ')[1]
        print(single_voice.id)

        engine.setProperty("voice",single_voice.id)
        engine.say(f"Bonjour Monde, mon nom est {single_voice_name}")
        engine.runAndWait()