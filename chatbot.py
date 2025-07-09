import nltk
import random
import string

from nltk.chat.util import Chat, reflections
from nltk.corpus import wordnet


nltk.download('punkt')
nltk.download('wordnet')


pairs = [
    ["hi|hello|hey", ["Hello!", "Hi there!", "Hey!"]],
    ["what is your name?", ["I'm a Chatbot!", "You can call me Bot."]],
    ["how are you?", ["I'm fine, thank you!", "Doing well!"]],
    ["bye|goodbye", ["Bye!", "See you!", "Goodbye!"]],
]


chatbot = Chat(pairs, reflections)
chatbot.converse()
