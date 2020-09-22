import speech_recognition as sr
def main():

    r = sr.Recognizer()
    print("Do you want to record or wanted a text file for your recording?")
    print("Press 1 if you wanted to record")
    print("Press 2 if you wanted the text file for your recording")
    ans=int(input())
    if ans==1:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source)
                print("Enter the file name in which you wanted to record")
                a=input()
                b=a+'.txt'
                a+='.wav'
                print("Please say something")
                audio = r.listen(source)
                print("Recognizing Now .... ")
                # recognize speech using google
                try:
                    print("You have said \n" + r.recognize_google(audio))
                    print("Audio Recorded Successfully \n ")
                except Exception as e:
                    print("Error :  " + str(e))
                 # write audio
                with open(a, "wb") as f:
                    f.write(audio.get_wav_data())
    elif ans==2:
            print("Enter the audio file name")
            a=input()
            a=a+'.wav'
            print("Enter the file name in which you wanted to save the text")
            k=input()
            b=k+'.txt'
            with sr.AudioFile(a) as source:
                audio = r.listen(source)
                try:
                        text = r.recognize_google(audio)
                        print('Working on...')
                        print(text)
                        file1 = open(b,"w+")
                        file1.writelines(text) 
                        file1.close()
                except:
                        print('Sorry.. run again...')
    else:
            print("Invalid response")
if __name__ == "__main__":
    main()
