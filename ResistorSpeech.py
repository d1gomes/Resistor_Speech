import speech_recognition as sr

count = 0 #initialize count
foo = []
#Create Values for Resistors
room = {"black":0, "brown":1, "red":2, "orange":3, "yellow":4, "green":5,
        "blue":6, "purple":7, "silver":8, "grey":8, "white":9}

r = sr.Recognizer()# initialize speech recognizer
with sr.Microphone() as source:# use microphone as source
    r.adjust_for_ambient_noise(source)
    while (count < 3):# only take 3 speech values
        count+=1
        audio = r.listen(source,phrase_time_limit=2)#listen to microphone
        
        try:
            mystring = r.recognize_sphinx(audio)#let sphinx find word from audio
            if mystring == '':#if no string found, dont count up.
                count-=1
            elif (count == 3) and (room[mystring] > 6):#third band cant be purple or up.
                count-=1
            else:
                print("Sphinx thinks you said " + mystring)#output string
                foo.append(room[mystring])
                
    
        except sr.UnknownValueError:
            print("Sphinx could not understand audio")
    
        except sr.RequestError as e:
            print("Sphinx error; {0}".format(e))

resistance = int(str(foo[0]) + str(foo[1])) * (10 ** foo[2])

print("The resistance is " + str(resistance));
