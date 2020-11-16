from flask import request, render_template, flash, session
import pickle
from app import app
import numpy as np
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.models import load_model


tokenizer=pickle.load(open('tranform.pkl','rb'))

LSTM = load_model('LSTM_model.h5')
GRU = load_model('GRU_model.h5')
CNN = load_model('CNN_model.h5')

def LSTMmodel(sentence):
    word_tokenize = tokenizer.texts_to_sequences([sentence])
    input = pad_sequences(word_tokenize, maxlen=20, padding='post', truncating='post')
    input = np.array(input)
    value = LSTM.predict(input)[0][0]*100
    statement = str('Tingkat sarkasme '+"{:.2f}".format(value)+'%')
    if value>50:
        result = 'LSTM: ' + sentence + ' Termasuk kalimat sarkas \n '+ statement
    else:
        result = 'LSTM: ' + sentence + '  Bukan kalimat sarkas \n ' + statement
    return result
        
def GRUmodel(sentence):
    word_tokenize = tokenizer.texts_to_sequences([sentence])
    input = pad_sequences(word_tokenize, maxlen=20, padding='post', truncating='post')
    input = np.array(input)
    value = GRU.predict(input)[0][0]*100
    statement = str('Tingkat sarkasme '+"{:.2f}".format(value)+'%')
    if value>50:
        result = 'GRU: ' + sentence + '  Termasuk kalimat sarkas \n '+ statement
    else:
        result = 'GRU: ' + sentence + '  Bukan kalimat sarkas \n ' + statement
    return result
        
def CNNmodel(sentence):
    word_tokenize = tokenizer.texts_to_sequences([sentence])
    input = pad_sequences(word_tokenize, maxlen=20, padding='post', truncating='post')
    input = np.array(input)
    value = CNN.predict(input)[0][0]*100
    statement = str('Tingkat sarkasme '+"{:.2f}".format(value)+'%')
    if value>50:
        result = 'CNN: ' + sentence + '  Termasuk kalimat sarkas \n ' + statement
    else:
        result = 'CNN: ' + sentence + '  Bukan kalimat sarkas \n ' + statement
    return result



@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST' :
        input_text = request.form.get("input-text")
        model = request.form.get("model")

        try:
            if (model == 'CNN'):
                pred_result = CNNmodel(input_text)
            elif (model == 'LSTM'):
                pred_result = LSTMmodel(input_text)
            elif (model == 'GRU'):
                pred_result = GRUmodel(input_text)    
            return render_template('home.html', text=pred_result)
        except UnboundLocalError:
             flash(u'Input text tidak boleh kosong')
             return render_template('home.html')

    else:
        return render_template('home.html')



if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port='7777')
