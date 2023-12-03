import random
from datetime import datetime, timedelta
import db_connect


def random_past_date(days_back):
    return datetime.today() - timedelta(days=random.randint(1, days_back))

def random_diagnosis():
    # Assuming you want a list of diagnoses
    return ['Diagnosis ' + str(random.randint(1, 100)) for _ in range(random.randint(1, 5))]

def random_recommendations():
    # Assuming you want a list of recommendations
    return ['Recommendation ' + str(random.randint(1, 100)) for _ in range(random.randint(1, 5))]

# Define working days as array of text for "ClinicRoom" table
def random_working_days():
    days_of_week = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница']
    return [random.choice(days_of_week) for _ in range(random.randint(1, 5))]


first_names = ['Дмитрий', 'Виктория', 'Алиса', 'Дора', 'Максим']
last_names = ['Зотовский', 'Шмидт', 'Тест', 'Коричневый', 'Даман']

# Generate a random phone number
def random_phone_number():
    return ''.join([str(random.randint(0, 9)) for _ in range(10)])

# Generate random date in the past 30 years
def random_past_date(years_back=30):
    start = datetime.today().replace(year=datetime.today().year - years_back)
    end = datetime.today()
    return start + (end - start) * random.random()

# Function to insert random data into "ClinicRoom"
def insert_clinic_rooms(cursor, n):
    query = """
    INSERT INTO public."ClinicRoom"
    (id, room_number, working_days, responsible_person, internal_phone_number)
    VALUES (%s, %s, %s, %s, %s)
    """
    for i in range(1, n+1):
        cursor.execute(query, (
            i,
            random.randint(1, 200), # room_number
            random_working_days(),   # working_days
            random.randint(1, 15),   # responsible_person (Doctor ID)
            random_phone_number()    # internal_phone_number
        ))

# Helper functions (defined previously, such as random_phone_number, etc.)

def random_date_of_birth(min_age=25, max_age=60):
    today = datetime.today()
    start_date = today.replace(year=today.year - max_age)
    end_date = today.replace(year=today.year - min_age)
    return start_date + (end_date - start_date) * random.random()

def random_gender():
    return random.choice(['Мужчина', 'Женщина'])

def random_specialization():
    specializations = ['Кардиолог','Отоларинголог']
    return random.choice(specializations)

# Function to insert random data into "Doctor"
def insert_doctors(cursor, n):
    query = """
    INSERT INTO public."Doctor"
    (id, first_name, last_name, middle_name, specialization, gender, date_of_birth, date_of_empoloyment, education, contract_details)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    for i in range(1, n+1):
        cursor.execute(query, (
            i + 10,
            random.choice(first_names),
            random.choice(last_names),
            random.choice(last_names),
            random_specialization(),
            random_gender(),
            random_date_of_birth().date(), # date_of_birth
            random_past_date(10).date(),   # date_of_empoloyment
            "Мед ВУЗ",               # education
            "Полный рабочий день"                     # contract_details
        ))

# Function to insert random data into "Patient"
def insert_patients(cursor, n):
    query = """
    INSERT INTO public."Patient"
    (id, first_name, last_name, middle_name, date_of_birth)
    VALUES (%s, %s, %s, %s, %s)
    """
    for i in range(1, n+1):
        cursor.execute(query, (
            i,
            random.choice(first_names),
            random.choice(last_names),
            random.choice(last_names),
            random_date_of_birth(18, 80).date() # date_of_birth with wider age range
        ))

# Function to insert random data into "MedicalCard"
def insert_medical_cards(cursor, n):
    query = """
    INSERT INTO public."MedicalCard" (id, patient_id, doctor_id, visit_date, diagnosis, current_condition, recommendations)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    for i in range(1, n+1):
        cursor.execute(query, (
            i,
            random.randint(1, n),  # Random patient_id
            random.randint(1, n),  # Random doctor_id
            random_past_date(300).date(),
            random_diagnosis(),
            'Stable',  # Example current condition
            random_recommendations(),
        ))

# Function to insert random data into "Visit"
def insert_visits(cursor, n):
    query = """
    INSERT INTO public."Visit" (id, patient, doctor, diagnosis, recomendation, date_of_visit, payment)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    for i in range(4, n+1):
        cursor.execute(query, (
            i,
            random.randint(1, n),  # Random patient_id
            random.randint(1, n),  # Random doctor_id
            'Diagnosis ' + str(i),
            random_recommendations(),
            random_past_date(100).date(),
            random.randint(50, 500),  # Example payment amount
        ))

# Function to map visits to medical cards in "MedicalCard_visits"
def insert_medicalcard_visits(cursor, n):
    query = """
    INSERT INTO public."MedicalCard_visits" (medicalcard_id, visit_id)
    VALUES (%s, %s)
    """
    for i in range(1, n+1):
        cursor.execute(query, (
            random.randint(1, n),  # Random medicalcard_id
            i,  # visit_id matching the inserted visit records
        ))

def main():
    n_records_doctor = 10
    n_records_patient = 15
    n_records_medical_card = 15
    n_records_visit = 15
    n_records_medical_card_visits = 15
    with db_connect.ConnectionCursor() as cursor:
        # insert_medical_cards(cursor, n_records_medical_card)
        # insert_visits(cursor, n_records_visit)
        insert_medicalcard_visits(cursor, n_records_medical_card_visits)
        # insert_clinic_rooms(cursor, n_records_doctor)
        # insert_patients(cursor, n_records_patient)

if __name__ == '__main__':
    main()