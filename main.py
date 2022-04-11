# E-juice nicotine mixing calculator
import os
from flask import Flask, render_template, request

Flask_App = Flask(__name__)

@Flask_App.route('/', methods=['GET'])
def index():
    """ Display the index page at '/' """

    return render_template('index.html')

@Flask_App.route('/operation_result/', methods=['POST'])
def operation_result():
    """ Route where to send calculator form input """

    error = None
    result = None

    # request.form looks for:
    # html tags with matching "name="
    amount = request.form['Input1']
    current = request.form['Input2']
    nic_base = request.form['Input3']
    target = request.form['Input4']

    try:

        input1 = float(amount)
        input2 = float(current)
        input3 = float(nic_base)
        input4 = float(target)

        # Calculate what the new target should be from user input if current is > 0mg
        # target_converted = int(target) - int(current)
        target_converted = float(input4) - float(input2)

        # Run calculation based on 0mg ejuice
        if input2 == 0:
            result = round(input1 / input3 * input4, 2)

        # Run calculation based on  > 0mg ejuice
        else:
            result = round(input1 / input3 * target_converted, 2)

        return render_template(
            'index.html',
            input1=input1,
            input2=input2,
            input3=input3,
            input4=input4,
            result=result,
            calculation_success=True
        )

    except ValueError:
        return render_template(
            'index.html',
            input1=amount,
            input2=current,
            input3=nic_base,
            input4=target,
            result="Bad Input",
            calculation_success=False,
            error="Cannot perform calculation based on input, please check your input"            
        )

@Flask_App.route('/other_page/', methods=['GET'])
def other_page():
    """ Display the other_page at '/other_page' """

    return render_template('other_page.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 7001))
    Flask_App.run(debug=True, host='0.0.0.0', port=port)