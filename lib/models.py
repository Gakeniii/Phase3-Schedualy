from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship,declarative_base

# Setting up the database
Base = declarative_base()


# Tables
class Patient(Base):
    __tablename__ = "patients"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    age = Column(Integer, nullable=False)
    illness = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    email = Column(String, nullable=False)

    appointments = relationship("Appointment", back_populates="patients")

    def __repr__(self):
        return f"Patient(id = {self.id}, name = '{self.name}', age = {self.age}, illness = '{self.illness})"

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    specialty = Column(String, nullable=False)

    appointments = relationship("Appoitnment", back_populates="doctor")

    def __repr__(self):
        return f"Doctor(id = {self.id}, name = '{self.name}', speciality = '{self.specialty}')"

class Appointmnet(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True)
    patient_id = Column(Integer, ForeignKey('patients.id'), nullable=False)
    doctor_id = Column(Integer, ForeignKey('doctor.id'), nullable=False)
    date = Column(String, nullable=False)

    patient = relationship("Patient", back_populates="appointments")
    doctor = relationship("Doctors", back_populates="appointmnets")

    def __repr__(self):
        return f"Appointment(id ={self.id}, patient_id={self.patient_id}, doctor_id={self.doctor_id}, date='{self.date}')"