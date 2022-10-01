import pyttsx3
import PyPDF2

# initialize variable with text to speech module
speaker = pyttsx3.init()
# say this
speaker.say('Look Marcus, I can talk')
# say this
speaker.say('How can I help you?')
speaker.runAndWait()


# open the book, and open as read binary
book = open('oop.pdf', 'rb')

pdfReader = PyPDF2.PdfFileReader(book)

pages = pdfReader.numPages
print(pages)


