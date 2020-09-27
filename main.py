import pyttsx3 as pt
import PyPDF2 as pdf


book = open('Notice.pdf', 'rb')


reader = pdf.PdfFileReader(book)
pages = reader.numPages
print(pages)
speaker = pt.init()

speed = speaker.getProperty("rate")
speaker.setProperty("rate", 150)
page = reader.getPage(0)
text = page.extractText()

speaker.say(text)
speaker.runAndWait()