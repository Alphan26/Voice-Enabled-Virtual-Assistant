import time
import numpy as np
import nltk
import speech_recognition
import pyttsx3
import random
import string
import threading
import joblib
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords

answer = ""
count = 0
recognizer = speech_recognition.Recognizer()
engine = pyttsx3.init()
model = joblib.load("logistic_regression_model.pkl")


def process_input(text):
    translator = str.maketrans('', '', string.punctuation)
    prediction_input = text.lower().translate(translator)
    tokens_word = word_tokenize(prediction_input)  # Metni tokenlara böler
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()

    # Stop words'leri çıkar ve kelimeleri lemmatize et
    tokens = [lemmatizer.lemmatize(word) for word in tokens_word if word not in stop_words]

    return tokens


def get_response(prediction_input):
    output = model.predict(prediction_input)
    # buradan cevap 0 ya da 1 olarak geri dönecek.
    # output = output.argmax()
    # # buradaki output olumlu ya da olumsuz diye cevap verecek
    # response_tag = le.inverse_transform([output])[0]
    # answer = random.choice(responses[response_tag])
    return output
    # bu answer değişkenini xml in kullanıp update etmesi lazım.


def chatbot_thread():
    global recognizer
    while True:
        try:
            with speech_recognition.Microphone() as mic:
                recognizer.adjust_for_ambient_noise(mic, duration=0.2)
                audio = recognizer.listen(mic, timeout=5)
                starting_time = time.time()
                print("Waiting for your response")
                text = recognizer.recognize_google(audio, language="en")
                text = text.lower()
                print("Did you say ", text)

                if text == "goodbye":
                    engine.say("Goodbye, have a nice day")
                    end_time = time.time()
                    print(end_time - starting_time)
                    engine.runAndWait()
                    break

                prediction_input = process_input(text)
                global answer
                answer = get_response(prediction_input)
                # buradaki answer cevabını xml dosyasına gömmem lazım şimdi

                # engine.say(answer)
                ending_time = time.time()
                elapsed_time = ending_time - starting_time
                print(elapsed_time)
                # Bu koda gerek kalmayacak twilio api zaten hallediyor.

        except speech_recognition.RequestError as e:
            print("Could not request results; {0}".format(e))

        except speech_recognition.UnknownValueError:
            recognizer = speech_recognition.Recognizer()
            continue


# Chatbot işlemini multithreading kullanarak başlatın
chatbot_thread = threading.Thread(target=chatbot_thread)
chatbot_thread.start()
# num_processes = 4  # Kullanılacak işlemci çekirdek sayısı
# processes = []

# for _ in range(num_processes):
#     p = multiprocessing.Process(target=chatbot_process)
#     p.start()
#     processes.append(p)
#
# for p in processes:
#     p.join()

# while True:
#     try:
#         with speech_recognition.Microphone() as mic:
#             recognizer.adjust_for_ambient_noise(mic, duration=0.2)
#             starting_time = time.time()
#             audio = recognizer.listen(mic, timeout=5)
#
#             # Listen and try to understand
#             text = recognizer.recognize_google(audio, language="tr-TR")  # tr-TR
#             text = text.lower()
#             print("Did you say ", text)
#
#             # Preprocess the input text
#             translator = str.maketrans('', '', string.punctuation)
#             prediction_input = text.lower().translate(translator)
#             # prediction_input = ''.join(letters.lower() for letters in text if letters not in string.punctuation)
#
#             # Tokenize and pad the input text
#             prediction_input = tokenizer.texts_to_sequences([prediction_input])
#             # metni tokenlaştırıp sayı haline getiriyoruz.
#             prediction_input = np.array(prediction_input).reshape(-1)
#             # nd arraye çevirdik
#             prediction_input = pad_sequences([prediction_input], input_shape)
#             # input değerlerin tokenları aynı boyutta olması gerektiği için aynı boyuta getiriyoruz.
#
#             # Make a prediction
#             output = model.predict(prediction_input)
#             output = output.argmax()
#
#             # Get the response tag and choose a random answer
#             response_tag = le.inverse_transform([output])[0]
#             answer = random.choice(responses[response_tag])
#
#             if text == "goodbye":
#                 engine.say("Goodbye, have a nice day")
#                 end_time = time.time()
#                 print(end_time - starting_time)
#                 engine.runAndWait()
#                 break
#
#             engine.say(answer)
#             ending_time = time.time()
#             elapsed_time = ending_time - starting_time
#             print(answer)
#             print(elapsed_time)
#             engine.runAndWait()
#
#     except speech_recognition.RequestError as e:
#         print("Could not request results; {0}".format(e))
#
#     except speech_recognition.UnknownValueError:
#         recognizer = speech_recognition.Recognizer()
#         continue
