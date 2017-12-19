# Resistor_Speech
Libraries you need to install on Python:
- SpeechRecognition (pip install speechrecognition)
- Pocketsphinx (pip install pocketsphinx)

After you have installed the following libraries you need to clear the text in this file of the python directory: Python\Python36\Lib\site-packages\speech_recognition\pocketsphinx-data\en-US\pronounciation-dictionary.dict

replace all the text with this (remove quotations):
"black B L AE K

blue B L UW

brown B R AW N

green G R IY N

grey G R EY

orange AO R AH N JH

purple P ER P AH L

red R EH D

silver S IH L V ER

white W AY T

yellow Y EH L OW"


This greatly increases pocketsphinx's accuracy when detecting what you said, as it checks for only specific phenomes.
