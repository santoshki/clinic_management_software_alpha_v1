import datetime


def patient_id_generator(patient_firstname, patient_middlename, patient_lastname):
    current_timestamp = int((datetime.datetime.now() - datetime.datetime(1970, 1, 1)).total_seconds())
    id_first_seq = patient_firstname[0:2]
    id_second_seq = 'x'
    id_third_seq = 'y'
    if patient_middlename != ' ':
        id_second_seq = patient_middlename[0:1]
    if patient_lastname != ' ':
        id_third_seq = patient_lastname[0:1]
    str_current_timestamp = str(current_timestamp)
    id_last_seq = str_current_timestamp[-4:]
    patient_reg_id = id_first_seq + id_second_seq + id_third_seq + id_last_seq
    print("Generated patient registration id:", patient_reg_id)
    return patient_reg_id
