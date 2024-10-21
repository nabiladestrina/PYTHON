import PySimpleGUI as sg
sg.theme("DrakBlue10")
sg.theme_text_color("#F0fFFF")
window = sg.Window(title="Profile",
layout=[[sg.Text("SELAMAT DATANG DI KELAS",
font=("Arial",25,"italic","bold","underline"))],
[sg.Text("NPM : 2210010634 ")],
[sg.Text("Nama : Nabila Dhea Destrina ")],
[sg.Text("Kelas : 5A Non-Reguler Banjarmasin ")]
],
size=(510,200),
font=("Times", 18))
window()
window.close()