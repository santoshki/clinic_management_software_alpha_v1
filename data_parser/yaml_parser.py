import yaml


def parse_normal_values():
    with open("C:\\Users\\Santiago\\PycharmProject\\clinic_management_software_alpha_v1\\database\\normal_values.yaml", "r") as f:
        doc = yaml.load(f, Loader=yaml.FullLoader)
    print(doc)
    bp_range = doc["BP range"]
    gender_value = bp_range["gender"]
    age_group = bp_range["age"]
    bp_range_values = age_group[0]

    print(bp_range, gender_value, age_group, bp_range_values)



if __name__ == '__main__':
    parse_normal_values()