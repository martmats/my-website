from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        bill = float(request.form['bill'])
        tip = int(request.form['tip'])
        people = int(request.form['people'])

        tip_percentage = tip / 100
        total_tip = bill * tip_percentage
        total_tip_total = total_tip + bill
        total_amount = total_tip_total / people

        total_round = round(total_amount, 2)

        return render_template('index.html', total=total_round)
    except ValueError:
        return render_template('index.html', error="Invalid input. Please enter numbers only.")

if __name__ == '__main__':
    app.run(debug=True)
