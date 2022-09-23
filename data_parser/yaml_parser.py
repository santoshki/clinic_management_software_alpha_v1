import yaml


def parse_normal_values():
    with open("C:\\Users\\Santiago\\PycharmProject\\clinic_management_software_alpha_v1\\database\\normal_values.yaml",
              "r") as f:
        doc = yaml.load(f, Loader=yaml.FullLoader)
    #print(doc)
    gender_value = "Male"
    age = "24"
    bp_range = doc["BP range"]
    gender = bp_range["gender"]
    for g in gender:
        if gender_value == str(g):
            print(g)
    ages = bp_range["age"]
    for ag in ages:
        ag = str(ag)
        low = ag[:2]
        high = ag[-2:]
        if int(low) <= int(age) <= int(high):
            print(ag)
    age_group = age[0]
    value = bp_range["value"]
    print(age_group, value[5])


if __name__ == '__main__':
    parse_normal_values()
