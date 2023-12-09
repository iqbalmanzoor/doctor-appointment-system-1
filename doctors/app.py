from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///doctors.db'  # Change the database name
db = SQLAlchemy(app)

# Define Doctor model
class Doctor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(50))
    lastName = db.Column(db.String(50))
    speciality = db.Column(db.String(50))

# Routes
@app.route('/doctors', methods=["GET"])
def getDoctors():
    doctors = Doctor.query.all()
    doctor_list = [
        {
            'id': doctor.id,
            'firstName': doctor.firstName,
            'lastName': doctor.lastName,
            'speciality': doctor.speciality
        }
        for doctor in doctors
    ]
    return jsonify(doctor_list)

@app.route('/doctor/<int:id>', methods=["GET"])
def getDoctor(id):
    doctor = Doctor.query.get(id)
    if doctor:
        return jsonify({
            'id': doctor.id,
            'firstName': doctor.firstName,
            'lastName': doctor.lastName,
            'speciality': doctor.speciality
        })
    else:
        return jsonify({'message': 'Doctor not found'}), 404

# Create tables
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)
