from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///appointments.db'
db = SQLAlchemy(app)

# Define Appointment model
class Appointment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    doctor = db.Column(db.String(50))
    date = db.Column(db.String(50))
    rating = db.Column(db.String(50))

# Routes
@app.route('/appointments', methods=["GET"])
def getAppointments():
    appointments = Appointment.query.all()
    appointment_list = [
        {
            'id': appointment.id,
            'doctor': appointment.doctor,
            'date': appointment.date,
            'rating': appointment.rating
        }
        for appointment in appointments
    ]
    return jsonify(appointment_list)

@app.route('/appointment/<int:id>', methods=["GET"])
def getAppointment(id):
    appointment = Appointment.query.get(id)
    if appointment:
        return jsonify({
            'id': appointment.id,
            'doctor': appointment.doctor,
            'date': appointment.date,
            'rating': appointment.rating
        })
    else:
        return jsonify({'message': 'Appointment not found'}), 404

# Wrap the creation of tables in an application context
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7070)
