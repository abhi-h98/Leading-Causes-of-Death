from xml.etree import ElementTree as ET

def process_row(zoo):
    x = {"_id" : zoo.attrib["_id"],
    "_uuid" : zoo.attrib["_uuid"],
    "_position" : zoo.attrib["_position"],
    "_address" : zoo.attrib["_address"],
    "year" : zoo[0].text,
#    "_113_cause_name" : zoo[1].text,
    "cause_name" : zoo[2].text,
    "state" : zoo[3].text,
    "deaths" : zoo[4].text,
    "aadr" : zoo[5].text
    }
    return x

def print_rows(wee, mama):
    for i, item in enumerate(wee):
        if mama == item["year"]:
            print("Record "+str(i)+" (id:" + str(item["_id"])+"): "+"During "+ str(item["year"])+" the leading cause of death in "+ str(item["state"]) + " was " + str(item["cause_name"]))
    return

def main():
    tree = ET.parse('leading_causes_of_death.xml')
    root = tree.getroot()
    year = input("Please enter a year: ")
    cod_list = []
    for row in root[0]:
        cod_list.append(process_row(row))
    print_rows(cod_list, year)

if __name__=='__main__':
    main()
