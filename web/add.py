import eel
eel.init("Interface_Eel_Library/web")

@eel.expose
def add(data1, data2):
    print(data1, data2)
    num1 = int(data1)
    num2 = int(data2)
    result = num1 + num2
    print(result)
    return result

eel.start("home.html")