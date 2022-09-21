import yaml


def parse_normal_values():
    with open("C:\\Users\\Santiago\\PycharmProject\\clinic_management_software_alpha_v1\\database\\normal_values.yaml", "r") as f:
        doc = yaml.load(f, Loader=yaml.FullLoader)
    print(doc)
    txt = doc["BP range"]
    print(txt)



if __name__ == '__main__':
    parse_normal_values()