# Project name: Schedualy
## Description:
  - Schedualy is a CLI Application 
    built with Python that keeps track of patients
    and their appointment dates for practicing doctors of different specialties

## Project set-up
To properly set up the project in your terminal you have to install the virtual environment
  ```console
> pipenv install
> pipenv shell
```
If the sqlAlchemy imports are still giving you a warning on your keyboard, type `ctrl+shift+p`
click Python Interpreter and click the version that coincides with your virtual environment

Next in your terminal inside your virtual environment, initialize the database by running `python3 cli.py`

Enjoy using Schedualy!

# Functions
  # Patient section
  - `add_patient` adds a patient to the database
  - `update_patient` updates a patient's information
  - `view_patient_info` gives you all the patients information
  - `delete_patient` deletes a patient
  - `view_all_patients` lists all the patients
  # Doctors section
  - `add_doctor` adds a doctor to the database
  - `update_doctor` updates a doctor's information
  - `delete_doctor` deletes a doctor from the database
  - `view_all_doctors` lists all the doctors in the database
  # Appointments section
  - `schedule_appointment` schedules an appointment for a patient and the doctor assigned to them
  - `update_appointment` updates the appointment details
  - `delete_appointment` deletes an appointment
  - `view_all_appointments` lists all the appointments that have been scheduled
  # Exit - ends the session
  
  # Best Practices Followed
  - Modular Code: Separate files for CLI logic, models, and database configuration.
  - SQLAlchemy ORM: Ensures easy database management with proper relationships.
  - Virtual Environment: Dependencies isolated using Pipenv.
  - Error Handling: Includes checks for invalid inputs (e.g patient not found)

  - email: gakenisifa@gmail.com
## License 
*Licensed under the MIT License Copyright (c) 2024
  Sifa Gakeni Muriithi

