from entities.entity import entity_parser


def patient_vitals_status(patient_record_data):
    bp_status = " "
    pulse_rate_status = " "
    oxygen_level_status = " "
    temperature_level_status = " "
    print("Computing status value for patient vitals")
    bp_measured_value = patient_record_data[1]
    pulse_rate_measured_value = patient_record_data[2]
    oxygen_level_measured_value = patient_record_data[3]
    temperature_measured_value = patient_record_data[4]
    bp_measured_value_systolic = bp_measured_value[:bp_measured_value.index("/")]
    bp_measured_value_diastolic = bp_measured_value[bp_measured_value.index("/") + 1:]

    if int(bp_measured_value_systolic) < 140:
        if int(bp_measured_value_diastolic) < 100:
            bp_status = "Normal"
            print("BP Status:", bp_status)
        else:
            bp_status = "Abnormal"
            print("BP Status:", bp_status)
    else:
        bp_status = "Abnormal"
        print("BP Status:", bp_status)

    if int((pulse_rate_measured_value)) >= 60:
        if int((pulse_rate_measured_value)) <= 100:
            pulse_rate_status = "Normal"
            print("Pulse Rate Status:", pulse_rate_status)
        else:
            pulse_rate_status = "Abnormal"
            print("Pulse Rate Status:", pulse_rate_status)
    else:
        pulse_rate_status = "Abnormal"
        print("Pulse Rate Status:", pulse_rate_status)

    if int(oxygen_level_measured_value) > 90:
        if int(oxygen_level_measured_value) <= 100:
            oxygen_level_status = "Normal"
            print("Oxygen level status:", oxygen_level_status)
        else:
            oxygen_level_status = "Abnormal"
            print("Oxygen level status:", oxygen_level_status)
    else:
        oxygen_level_status = "Abnormal"
        print("Oxygen level status:", oxygen_level_status)

    if float(temperature_measured_value) >= 36:
        if float(temperature_measured_value) <= 38:
            temperature_level_status = "Normal"
            print("Temperature level status:", temperature_level_status)
        else:
            temperature_level_status = "Abnormal"
            print("Temperature level status:", temperature_level_status)
    else:
        temperature_level_status = "Abnormal"
        print("Temperature level status:", temperature_level_status)

    return True
