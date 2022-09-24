import yaml


def parse_normal_values():
    with open("C:\\Users\\Santiago\\PycharmProject\\clinic_management_software_alpha_v1\\database\\normal_values.yaml",
              "r") as f:
        doc = yaml.load(f, Loader=yaml.FullLoader)
    #print(doc)
    gender_value = "Male"
    age = "37"
    bp_range = doc["BP range"]
    gender = bp_range["gender"]
    for i in range(0, len(gender)):
        if gender_value == str(gender[i]):
            gender_index = i
    ages = bp_range["age"]
    if gender_index == 0:
        value_low_index = 5
        value_high_index = 13
    else:
        value_low_index = 14
        value_high_index = 22

    for j in range(0, len(ages)):
        ag = str(ages[j])
        low = ag[:2]
        high = ag[-2:]
        if int(low) <= int(age) <= int(high):
            value_index = j
            print(j)
    '''for ag in ages:
        ag = str(ag)
        low = ag[:2]
        high = ag[-2:]
        if int(low) <= int(age) <= int(high):
            print(ag)'''
    age_group = age[0]
    values = bp_range["value"]
    print("value_low_index:", value_low_index)
    value = values[value_low_index + value_index -5]
    print(age_group, value)


if __name__ == '__main__':
    parse_normal_values()
