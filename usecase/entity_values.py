from entities.entity import entity_parser
def patient_vitals_status(patient_record_data):
    print("Computing status value for patient vitals")
    bp_measured_value = patient_record_data[1]
    print("BP measured value:", bp_measured_value)
    bp_measured_value_systolic = bp_measured_value[:bp_measured_value.index("/")]
    bp_measured_value_diastolic = bp_measured_value[bp_measured_value.index("/") + 1:]
    print("Systolic:", bp_measured_value_systolic)
    print("Diastolic:", bp_measured_value_diastolic)
    if int(bp_measured_value_systolic) < 140:
        if int(bp_measured_value_diastolic) < 100:
            print("Normal")

    return True