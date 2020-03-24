from googletrans import Translator

translator=Translator()

text=input("Ask translation from english to telugu : ").split(",")
translated=translator.translate(text,dest='te')
for translation in translated:
    print(translation.origin, ' -> ',translation.text)
#print(translated)
#print(" Source Language:" + translated.src)
#print( "translated language:" ,translated.text) 
