from flask import Flask,jsonify

app = Flask(__name__)

courses = [{'name': "Rest API",
            'course_id': "0",
            'description': "This is the first project in Flask using Rest API",
            'price': "Check the site"},
           {'name': "Flask",
            'course_id': "1",
            'description': "Using PyCharm for the first time",
            'price': "Check the site for discount"},
            {
            'name': "Django",
            'course_id': "2",
            'description': "Flask is better than Django",
            'price': "No doubt in that"
            }   
           ]

@app.route('/')

def index():
    return 'Hello World!'

@app.route('/courses', methods=['GET'])
def get():
    return jsonify({'Courses': courses})

@app.route('/courses/<int:course_id>', methods=['GET'])
def get_course(course_id):
    return jsonify({'Course': courses[course_id]})

@app.route('/courses', methods=['POST'])
def create():
    course = {
        'name': "Django",
        'course_id': "2",
        'description': "Flask is better than Django",
        'price': "No doubt in that"
    }
    courses.append(course)
    return jsonify({'Created':course})

@app.route('/courses/<int:course_id>',methods=['PUT'])
def course_update(course_id):
    courses[course_id]['description'] = "XYZ"
    return jsonify({'course':courses[course_id]})

@app.route('/courses/<int:course_id>',methods=['DELETE'])
def delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'result':True})


if __name__ == "__main__":
    app.run(debug=True)

#curl -i -H "Content-Type: Application/json" -X POST/PUT/DELETE http://localhost:5000/courses/