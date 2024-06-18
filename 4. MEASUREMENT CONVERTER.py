
# ICT 09 – Programming 1

# FINAL PROJECT

# 4. Measurement converter:
# - This should show a menu to the user. The menu should contain at least 5 unit of
# measurement (i.e. mm to cm, ft to m, etc) and perform the conversion with inputs coming
# from the user.

def measurement_converter():
    def mm_to_cm(mm):
        return mm / 10

    def ft_to_m(ft):
        return ft * 0.3048

    def in_to_cm(inches):
        return inches * 2.54

    def lb_to_kg(pounds):
        return pounds * 0.453592

    def mi_to_km(miles):
        return miles * 1.60934

    def gal_to_l(gallons):
        return gallons * 3.78541

    def m_to_ft(meters):
        return meters * 3.28084

    def cm_to_mm(cm):
        return cm * 10

    def cm_to_in(cm):
        return cm * 0.393701

    def kg_to_lb(kg):
        return kg * 2.20462

    conversions = {
        "1": ("mm to cm", mm_to_cm),
        "2": ("ft to m", ft_to_m),
        "3": ("in to cm", in_to_cm),
        "4": ("lb to kg", lb_to_kg),
        "5": ("m to ft", m_to_ft),
        "6": ("cm to mm", cm_to_mm),
        "7": ("cm to in", cm_to_in),
        "8": ("kg to lb", kg_to_lb),
    }

    print("Measurement Converter")
    for key, (name, _) in conversions.items():
        print(f"{key}. {name}")

    choice = input("Choose a conversion: ")
    value = float(input("Enter the value to convert: "))
    result = conversions[choice][1](value)
    print(f"Converted value: {result}")

if __name__ == "__main__":
    measurement_converter()
