from django.shortcuts import render
from rest_framework.decorators import APIView
from nltk.corpus import stopwords
import nltk
from nltk.stem.porter import PorterStemmer
import pickle
from .forms import EmailForm
import string

ps = PorterStemmer()
tfidf = pickle.load(open('J:\\Django Projects\\Spam Emaill\\email_spam\\spam\\model\\vectorizer.pkl', 'rb'))
model = pickle.load(open('J:\\Django Projects\\Spam Emaill\\email_spam\\spam\\model\\model.pkl', 'rb'))
# Create your views here.

def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)


def SpamView(request):
    res = None

    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            input_email = form.cleaned_data['email']
            print(input_email)
            transformed_email = transform_text(input_email)
            vector_input = tfidf.transform([transformed_email])
            res = model.predict(vector_input)[0]
    else:
        form = EmailForm()
    return render(request, "spam/index.html", {'form': form, 'res': res})

