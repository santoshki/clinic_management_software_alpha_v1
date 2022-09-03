parsed_entry_data = []


def entry_data_parser(form_data):
    print("Parsing entry data")
    try:
        patient_firstname = form_data["first_name"]
        patient_middlename = form_data["middle_name"]
        patient_lastname = form_data["last_name"]
        patient_emergency_contact_name = form_data["emergency_name"]
        patient_emergency_contact_number = form_data["emg_contact_num"]
        patient_emergency_email_id = form_data["emergency_email_id"]
        patient_gender_value = form_data.get("gender")
        patient_age = form_data["age"]
        health_issue = form_data["health_issue"]
        patient_email_id = form_data["patient_email_id"]
        patient_contact_number = form_data["patient_contact_number"]
        patient_unique_identification_number = form_data["unique_identification_number"]
        patient_city_town = form_data["city_town"]
        patient_state = form_data["state"]
        patient_postal_address = form_data["postal_address"]
        patient_pin_code = form_data["pin_code"]
        doctor_physician_name = form_data.get("doctors")
        patient_visit_number = form_data["visit_number"]
        patient_visit_time = form_data["visit_time"]
        parsed_entry_data.extend((patient_firstname, patient_middlename, patient_lastname, patient_emergency_contact_name,
                                  patient_emergency_contact_number, patient_emergency_email_id, patient_gender_value, patient_age, health_issue,
                                  patient_email_id, patient_contact_number, patient_unique_identification_number, patient_city_town,
                                  patient_state, patient_postal_address, patient_pin_code, doctor_physician_name, patient_visit_number,
                                  patient_visit_time))
        return parsed_entry_data
    except Exception as e:
        print("Exception occurred:", e)
        return -1
