from flask import request, render_template, flash, session
import pickle
from app import app


def predict(txt, model_type):
    #TODO create prediction function
    res = txt + ' is a ' + model_type
    return res


@app.route('/', methods=['GET', 'POST'])
def introLevel():

    if request.method == 'POST' :
        input_text = request.form.get("input-text")
        model = request.form.get("model")

        try:
            if (model == 'CNN'):
                pred_result = predict(input_text, model)
            elif (model == 'LSTM'):
                pred_result = predict(input_text, model)
            elif (model == 'GRU'):
                pred_result = predict(input_text, model)    
            return render_template('home.html', text=pred_result)
        except UnboundLocalError:
             flash(u'Input text tidak boleh kosong')
             return render_template('home.html')

    else:
        return render_template('home.html')



if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0', port='7777')
