from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def currency_converter():
    if request.method == 'POST':
        # Get user inputs from the form
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']
        amount = request.form['amount']

       amount = float(amount)
        except ValueError:
            return render_template('errors.html', error_message='Invalid amount.')

        

    return render_template('form.html')
