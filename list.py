from flask import Flask, jsonify, request

app = Flask(__name__)

students = [
    { "name":"Suraj","phone no":2222}
]
@app.route('/add-students', methods=['POST'])
def create_students():
    # request-stores the information from body
    content = request.get_json()
    # taking variables to append the values
    name = content['name']
    phone_no= content['phone no']
    # joining the values and converting into string
    res = name + "," + phone_no
    file_path = r'C:\Users\Ribani\PycharmProjects\FlaskProject\students.txt'
    # content of the file
    with open(file_path, 'r') as file_object:
        lines = file_object.readlines()
    # return jsonify(lines)
    data = [line.strip() for line in lines if line.strip()]
    no_exist=0
    for line in data:
        no=line.split(",")[1]
        if no==phone_no:
            no_exist=1
            break

    # return jsonify({"students_from_file": data})

     # Append instead of overwrite ('a' instead of 'w')
    if no_exist==0:
         with open(file_path, 'a') as file_object:
            file_object.write(res + '\n')
         return jsonify({"message": "Student added successfully", "data": {"name": name, "phone_no": phone_no}})
    else:
        return jsonify({"message": "Student already exists!", "data": {}})

@app.route('/list-students', methods=['GET'])
def get_students():
    file_path = r'C:\Users\Ribani\PycharmProjects\FlaskProject\students.txt'
    # content of the file
    with open(file_path, 'r') as file_object:
        lines = file_object.readlines()
        # return jsonify({"students": lines})
    students =[]
    for line in lines:
        lines = line.strip()
        if not lines:
            continue
        parts= lines.split(",")
        name = parts[0]
        phone_no = parts[1]
        students.append({"name": name, "phone no": phone_no})
        return jsonify({"data": students})
@app.route('/show-students', methods=['GET'])
def show_students():
    phone = request.args.get('phone').strip()
    # return jsonify({"data": phone})
    file_path = r'C:\Users\Ribani\PycharmProjects\FlaskProject\students.txt'
    # content of the file
    with open(file_path, 'r') as file_object:
        data = file_object.readlines()

    found_name = ''

    for line in data:
        lines = line.strip()
        parts = lines.split(",")
        name = parts[0].strip()
        phone_no = parts[1].strip()

        if int(phone_no) == int(phone):
            return jsonify({
                "message": "Student found!",
                "data": {
                    "name": name,
                    "phone no": phone
                }
            })
    if found_name=='':
        return jsonify({"message": "Student not found!", "data": {}})


if __name__ =='__main__':
    app.run(debug=True)
