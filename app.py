from math import sin, cos, tan, sqrt,exp, log, acosh,asinh,asin, acos, atanh
from flask import Flask, render_template, url_for, request

app = Flask(__name__)


# route == link == url

# main route
@app.route("/")
def main():
    return render_template("index.html", home=True)

@app.route("/advanced")
def advanced():
    return render_template("advanced.html")

@app.route("/simple")
def simple():
    return render_template("simple.html")

@app.route("/carbon")
def carbon_emissions():
    return render_template("carbon_emissions.html")

@app.route("/calculate", methods=["post"])
def calculate():
    first_number = int(request.form["firstNumber"])
    operation = request.form["operation"]
    second_number = int(request.form["secondNumber"])
    note = ""
    color = "alert-success"
    if operation == "plus":
        result = first_number + second_number
        note = "Addition was performed successfully"
    elif operation == "minus":
        result = first_number - second_number
        note = "Subtraction was performed successfully"
    elif operation == "multiply":
        result = first_number * second_number
        note = "Multiplication was performed successfully"
    elif operation == "divide":
        result = first_number / second_number
        note = "Division was performed successfully"
    else:
        note = "This is an error, please try again"
        color = "alert-danger"
        return render_template("simple.html", note=note,color=color)
    return render_template("simple.html", result=result, note=note,color = color)

@app.route("/calculate_advanced", methods=["post"])
def calculate_advanced():
    first_number = int(request.form["firstNumber"])
    operation = request.form["operation"]
    note = ""
    color = "alert-success"
    try:
        if operation == "sin":
            result = sin(first_number)
            note = "Sine was performed successfully"
        elif operation == "cos":
            result = cos(first_number)
            note = "Cosine was performed successfully"
        elif operation == "tan":
            result = tan(first_number)
            note = "Tangent was performed successfully"
        elif operation == "squr":
            result = sqrt(first_number)
            note = "Square root was performed successfully"
        elif operation == "log":
            result = log(first_number)
            note = "Log was performed successfully"
        elif operation == "exp":
            result = exp(first_number)
            note = "exp was performed successfully"
        elif operation == "asinh":
            result = asinh(first_number)
            note = "Asinh was performed successfully"
        elif operation == "acosh":
            result = acosh(first_number)
            note = "Acosh was performed successfully"
        elif operation == "atanh":
            result = atanh(first_number)
            note = "Atanh was performed successfully"
        elif operation == "asin":
            result = asin(first_number)
            note = "Asin was performed successfully"
        elif operation == "acos":
            result = acos(first_number)
            note = "Acos was performed successfully"
        else:
            color = "alert-danger"
            note = "This is an error, please try again"
            return render_template("advanced.html", note=note, color=color)
    except ValueError:
        return render_template("advanced.html", result=0, color="alert-warning", note="Math error!")

    return render_template("advanced.html", result=result, color=color, note=note)


@app.route("/carbon_calculate", methods=["post"])
def carbon_calculate():
    local_import = request.form["local_import"]
    open_green = request.form["open_green"]
    heat_unheat = request.form["heat_unheat"]
    fertilizer = request.form["fertilizer"]
    plant = request.form["plant"]
    soil = request.form["soil"]
    post = request.form["post"]
    glass = request.form["glasshouse"]
    transport = request.form["transport"]
    weight = request.form["weight"]

    fertilizer_value = 0
    plant_value = 0
    soil_value = 0
    post_value = 0
    glass_value = 0

    c = 0
    color = "alert-success"

    def yes_no(name):
        if name == "yes":
            name = 1
        else:
            name = 0
        return name

    fertilizer = yes_no(fertilizer)
    plant = yes_no(plant)
    soil = yes_no(soil)
    post = yes_no(post)
    glass = yes_no(glass)



    if local_import == 'local':
        if open_green == 'open':
            c = 0
            c += 0.091 * fertilizer
            c += 0.0003 * plant_value
            c += 0.071 * soil_value
            c += 0.043 * post_value

            c += 0.00015 * int(transport)
            kg = int(weight)
        elif open_green == 'green':
            if heat_unheat == 'heat':
                c = 0
                c += 0.023 * fertilizer
                c += 0.028 * plant_value
                c += 0.157 * soil_value
                c += 0.091 * post_value
                c += 0.007 * glass_value
                c += 0.758
                c += 0.00015 * int(transport)
                kg = int(weight)
            elif heat_unheat == 'unheat':
                c = 0
                c += 0.01 * fertilizer
                c += 0.025 * plant_value
                c += 0.013 * soil_value
                c += 0.086 * post_value
                c += 0.007 * glass_value
                c += 0.029
                c += 0.00015 * int(transport)
                kg = int(weight)

    elif local_import == 'import':
        c = 0
        c += 0.132 * fertilizer
        c += 0.028 * plant_value
        c += 0.03 * soil_value
        c += 0.033 * post_value
        c += 0.00015 * int(transport)
        kg = int(weight)




    note = "The carbon emission of 1kg of lettuce: " + str(c) + ".\r\n "\
           + "The overall carbon emissions:" + str(c*kg)+" .\r\n" \
           + "The local_import you have chosen: "+ local_import +" .\r\n" \
           + "The open_green you have chosen: " + open_green +" .\r\n" \
           + "The heat_unheat you have chosen: " + heat_unheat + " .\r\n" \
           + "The fertilizer you have chosen: " + str(fertilizer) + " .\r\n" \
           + "The plant you have chosen: " + str(plant) +" .\r\n" \
           + "The soil you have chosen: " + str(soil) +" .\r\n" \
           + "The post you have chosen: " + str(post) +" .\r\n" + \
           "The glass you have chosen: " + str(glass) + " .\r\n"

    return render_template("carbon_emissions.html", result=c, note=note, color=color)


if __name__ == '__main__':
    app.run(debug=True)
