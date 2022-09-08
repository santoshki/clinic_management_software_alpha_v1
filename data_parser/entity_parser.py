def entry_data_parser(entry_form_data):
    print("Parsing entry data")
    parsed_entry_data = []
    try:
        patient_firstname = entry_form_data["first_name"]
        patient_middlename = entry_form_data["middle_name"]
        patient_lastname = entry_form_data["last_name"]
        patient_emergency_contact_name = entry_form_data["emergency_name"]
        patient_emergency_contact_number = entry_form_data["emg_contact_num"]
        patient_emergency_email_id = entry_form_data["emergency_email_id"]
        patient_gender_value = entry_form_data.get("gender")
        patient_age = entry_form_data["age"]
        health_issue = entry_form_data["health_issue"]
        patient_email_id = entry_form_data["patient_email_id"]
        patient_contact_number = entry_form_data["patient_contact_number"]
        patient_unique_identification_number = entry_form_data["unique_identification_number"]
        patient_city_town = entry_form_data["city_town"]
        patient_state = entry_form_data["state"]
        patient_postal_address = entry_form_data["postal_address"]
        patient_pin_code = entry_form_data["pin_code"]
        doctor_physician_name = entry_form_data.get("doctors")
        patient_visit_number = entry_form_data["visit_number"]
        patient_visit_time = entry_form_data["visit_time"]
        parsed_entry_data.extend \
            ((patient_firstname, patient_middlename, patient_lastname, patient_emergency_contact_name,
              patient_emergency_contact_number, patient_emergency_email_id, patient_gender_value, patient_age,
              health_issue,
              patient_email_id, patient_contact_number, patient_unique_identification_number, patient_city_town,
              patient_state, patient_postal_address, patient_pin_code, doctor_physician_name, patient_visit_number,
              patient_visit_time))
        return parsed_entry_data
    except Exception as e:
        print("Exception occurred:", e)
        return -1


def patient_vitals_data_parser(vitals_form_data):
    print("Parsing patient vitals data...")
    parsed_vitals_data = []
    try:
        bp_measured_value = vitals_form_data["bp_measured_value"]
        pulse_rate_measured_value = vitals_form_data["pulse_rate_measured_value"]
        oxygen_level_measured_value = vitals_form_data["oxygen_levels_measured_value"]
        temperature_measured_value = vitals_form_data["temperature_measured_value"]
        height_measured_value = vitals_form_data["height_measured_value"]
        weight_measured_value = vitals_form_data["weight_measured_value"]
        parsed_vitals_data.extend((bp_measured_value, pulse_rate_measured_value, oxygen_level_measured_value, temperature_measured_value,
                                    height_measured_value, weight_measured_value))
        return parsed_vitals_data
    except Exception as e:
        print("Exception occurred:", e)
        return -1
