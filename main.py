from flask import request, render_template, flash
import pickle



@app.route('/', methods=['GET', 'POST'])
def introLevel():
    if request.method == 'POST' :

        input_text = request.form.get("input-text")
        model = request.form.get("model")

        if (model == 'CNN'):
            pred_result = predict(input_text, model)
        elif (model == 'LSTM'):
            pred_result = predict(input_text, model)
        elif (model == 'GRU'):
            pred_result = predict(input_text, model)

        return render_template('home.html', text=pred_result[0], result=pred_result[1])

    else:
        return render_template('home.html')


def predict(txt, model_type):
    #TODO create prediction function
    return [txt, model_type]
