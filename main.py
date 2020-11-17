from flask import request, render_template, flash, session
import pickle
from app import app
import numpy as np
import json
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
        result = 'LSTM: ' + sentence + ' Termasuk kalimat sarkas  '+ statement
    else:
        result = 'LSTM: ' + sentence + '  Bukan kalimat sarkas  ' + statement
    return [result, value]
        
def GRUmodel(sentence):
    word_tokenize = tokenizer.texts_to_sequences([sentence])
    input = pad_sequences(word_tokenize, maxlen=20, padding='post', truncating='post')
    input = np.array(input)
    value = GRU.predict(input)[0][0]*100
    statement = str('Tingkat sarkasme '+"{:.2f}".format(value)+'%')
    if value>50:
        result = 'GRU: ' + sentence + ' Termasuk kalimat sarkas  '+ statement
    else:
        result = 'GRU:  ' + sentence + ' Bukan kalimat sarkas  ' + statement
    return [result, value]
        
def CNNmodel(sentence):
    word_tokenize = tokenizer.texts_to_sequences([sentence])
    input = pad_sequences(word_tokenize, maxlen=20, padding='post', truncating='post')
    input = np.array(input)
    value = CNN.predict(input)[0][0]*100
    statement = str('Tingkat sarkasme '+"{:.2f}".format(value)+'%')
    if value>50:
        result = 'CNN: ' + sentence + ' Termasuk kalimat sarkas ' + statement
    else:
        result = 'CNN: ' + sentence + ' Bukan kalimat sarkas ' + statement
    return [result, value]

def updatemodel(sentence, sarcasm):
    if sarcasm == 'yes':
        labels = 1
    else:
        labels = 0
    word_tokenize = tokenizer.texts_to_sequences([sentence])
    inputtext = pad_sequences(word_tokenize, maxlen=20, padding='post', truncating='post')
    inputtext = np.array(inputtext)
    LSTM = load_model('LSTM_model.h5')
    GRU = load_model('GRU_model.h5')
    CNN = load_model('CNN_model.h5')
    LSTM.fit(inputtext, np.array([labels]))
    GRU.fit(inputtext, np.array([labels]))
    CNN.fit(inputtext, np.array([labels]))
    GRU.save("GRU_model.h5")
    LSTM.save('LSTM_model.h5')
    CNN.save('CNN_model.h5')
    LSTM = load_model('LSTM_model.h5')
    GRU = load_model('GRU_model.h5')
    CNN = load_model('CNN_model.h5')
    finish = 'finish'
    return finish



@app.route('/', methods=['GET', 'POST'])
def home():

    if request.method == 'POST' :
        input_text = request.form.get("input-text")
        model = request.form.get("model")
        pred_val = []

        try:
            if (model == 'CNN'):
                pred_result = CNNmodel(input_text)[0]
                pred_val.append(CNNmodel(input_text)[1])
                pred_val.append(100 - CNNmodel(input_text)[1])
            elif (model == 'LSTM'):
                pred_result = LSTMmodel(input_text)[0]
                pred_val.append(LSTMmodel(input_text)[1])
                pred_val.append(100 - LSTMmodel(input_text)[1])
            elif (model == 'GRU'):
                pred_result = GRUmodel(input_text)[0] 
                pred_val.append(GRUmodel(input_text)[1])
                pred_val.append(100 - GRUmodel(input_text)[1])   
            return render_template('home.html', text=pred_result, val=json.dumps(pred_val))
        except UnboundLocalError:
             flash(u'Input text tidak boleh kosong')
             return render_template('home.html')

    else:
        return render_template('home.html')

@app.route('/updatemodel', methods=['GET', 'POST'])
def model():

    if request.method == 'POST' :
        input_text = request.form.get("input-text")
        is_sarcasm = request.form.get("is_sarcasm")
        str(input_text)
        str(is_sarcasm)
        k=1

        while k<3:
            updatemodel(input_text,is_sarcasm)
            k+=1
        return render_template('updatemodel.html', text='finish')
        #except UnboundLocalError:
         #   return render_template('updatemodel.html', text='Input text tidak boleh kosong')

    else:
        return render_template('updatemodel.html')



if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port='7777')
