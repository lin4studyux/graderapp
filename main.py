from flask import Flask
from flask_restful import Resource, Api
from flask_jsonpify import jsonify

app = Flask(__name__)
api = Api(app)


class grader(Resource):
    def get(self, num_value, unit_of_measure, target_unit_of_measure, student_response):
        output_response = gradecalculater(num_value, unit_of_measure, target_unit_of_measure, student_response)
        result = {'data': str(output_response)}
        return jsonify(result)

api.add_resource(grader, '/grader/<num_value>/<unit_of_measure>/<target_unit_of_measure>/<student_response>')

def gradecalculater(num_value, unit_of_measure, target_unit_of_measure, student_response):

    try:
        if unit_of_measure == "Kelvin":
            if target_unit_of_measure == "Kelvin":
                if round(float(student_response), 1) == round(float(num_value), 1):
                    return "correct"
                else:
                    return "incorrect"
            elif target_unit_of_measure == "Celsius":
                converted_value = round((float(num_value) - 273.15), 1)
                if round(converted_value, 1) == round(float(student_response), 1):
                    return "correct"
                else:
                    return "incorrect"
            elif target_unit_of_measure == "Fahrenheit":
                converted_value = round(float(num_value) * (9.0 / 5.0) - 489.67, 1)
                if round(converted_value, 1) == round(float(student_response), 1):
                    return "correct"
                else:
                    return "incorrect"
            elif target_unit_of_measure == "Rankine":
                converted_value = round(float(num_value) * (9.0 / 5.0), 1)
                if round(converted_value, 1) == round(float(student_response), 1):
                    return "correct"
                else:
                    return "incorrect"
            else:
                return "invalid"

        if unit_of_measure == "Celsius":
            if target_unit_of_measure == "Celsius":
                if round(float(student_response), 1) == round(float(num_value), 1):
                    return "correct"
                else:
                    return "incorrect"
            elif target_unit_of_measure == "Kelvin":
                converted_value = round(float(num_value) + 273.15, 1)
                if round(converted_value, 1) == round(float(student_response), 1):
                    return "correct"
                else:
                    return "incorrect"
            elif target_unit_of_measure == "Fahrenheit":
                converted_value = round(float(num_value) * (9.0 / 5.0) + 32, 1)
                if round(converted_value, 1) == round(float(student_response), 1):
                    return "correct"
                else:
                    return "incorrect"
            elif target_unit_of_measure == "Rankine":
                converted_value = round((float(num_value) + 273.15) * (9.0 / 5.0), 1)
                if round(converted_value, 1) == round(float(student_response), 1):
                    return "correct"
                else:
                    return "incorrect"
            else:
                return "invalid"

        if unit_of_measure == "Fahrenheit":
            if target_unit_of_measure == "Fahrenheit":
                if round(float(student_response), 1) == round(float(num_value), 1):
                    return "correct"
                else:
                    return "incorrect"
            elif target_unit_of_measure == "Kelvin":
                converted_value = round((float(num_value) + 459.67) * (5.0 / 9.0), 1)
                if round(converted_value, 1) == round(float(student_response), 1):
                    return "correct"
                else:
                    return "incorrect"
            elif target_unit_of_measure == "Celsius":
                converted_value = round((float(num_value) - 32) * (5.0 / 9.0), 1)
                if round(converted_value, 1) == round(float(student_response), 1):
                    return "correct"
                else:
                    return "incorrect"
            elif target_unit_of_measure == "Rankine":
                converted_value = round(float(num_value) + 459.67, 1)
                if round(converted_value, 1) == round(float(student_response), 1):
                    return "correct"
                else:
                    return "incorrect"
            else:
                return "invalid"

        if unit_of_measure == "Rankine":
            if target_unit_of_measure == "Rankine":
                if round(float(student_response), 1) == round(float(num_value), 1):
                    return "correct"
                else:
                    return "incorrect"
            elif target_unit_of_measure == "Kelvin":
                converted_value = round(float(num_value) / 1.8, 1)
                if round(converted_value, 1) == round(float(student_response), 1):
                    return "correct"
                else:
                    return "incorrect"
            elif target_unit_of_measure == "Celsius":
                converted_value = round((float(num_value) - 32 - 459.67) / 1.8, 1)
                if round(converted_value, 1) == round(float(student_response), 1):
                    return "correct"
                else:
                    return "incorrect"
            elif target_unit_of_measure == "Fahrenheit":
                converted_value = round(float(num_value) - 459.67, 1)
                if round(converted_value, 1) == round(float(student_response), 1):
                    return "correct"
                else:
                    return "incorrect"
            else:
                return "invalid"

        else:
            return "invalid"

    except:
        if isinstance(student_response, str):
            return "incorrect"
        else:
            return "invalid"

if __name__ == '__main__':
     app.run(port='5002')