import sys
import random

from PyQt5 import QtWidgets

import design
from query import query_in


DB_REQUEST_RASP = """Select X1.Nomer_pari,X2.Nazvanie_discipl,X1.N_Auditorii,X2.FIO_prep, X2.Nedela
                from gruppazanyatie X1 INNER JOIN zanyatie X2 ON (X1.Nomer_pari = X2.Nomer_pari 
                AND X1.Den_nedeli = X2.Den_nedeli AND X1.N_Auditorii = X2.N_Auditorii) 
                where N_gruppi  = '{}' AND X1.Den_nedeli = '{}'"""
DB_REQUEST_PREP = """Select Nomer_pari,Nazvanie_discipl,N_Auditorii,Nedela
                from zanyatie
                where FIO_prep = '{}' AND Den_nedeli = '{}'"""


class ExampleApp(QtWidgets.QMainWindow, design.Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.comboBox.activated[str].connect(self.combo_activated)
        self.comboBox_2.activated[str].connect(self.combo_2_activated)
        self.pushButton.clicked.connect(self.btn_click)
        self.pushButton_2.clicked.connect(self.btn_click_2)

    def combo_activated(self, text):

        day_of_week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота')
        self.textEdit.clear()

        for chosen_day in day_of_week:
            self.textEdit.append('\t')
            self.textEdit.append('<font size="5"><u>' + chosen_day + '</u></font>')
            try:

                request = query_in(DB_REQUEST_RASP.format(str(text), chosen_day))

                if request:
                    for kortege in request:
                        if kortege[4] == 1:
                            self.textEdit.append(
                                '<font size="4"><span style="color: red;">' + str(kortege[0]) + '</span>' + ' - ' + kortege[
                                    1] + ' ' + ' - ' + kortege[2] + ' - ' + kortege[3] + '</font>')
                        if kortege[4] == 2:
                            self.textEdit.append(
                                '<font size="4"><span style="color: blue;">' + str(kortege[0]) + '</span>' + ' - ' + kortege[
                                    1] + ' ' + ' - ' + kortege[2] + ' - ' + kortege[3] + '</font>')
                        if kortege[4] == 0:
                            self.textEdit.append(
                                '<font size="4"><span style="color: black;">' + str(kortege[0]) + '</span>' + ' - ' + kortege[
                                    1] + ' ' + ' - ' + kortege[2] + ' - ' + kortege[3] + '</font>')

                else:
                    self.textEdit.append("\nВыходной")

            except:
                self.textEdit.append("Error")

    def combo_2_activated(self, text):

        day_of_week = ('Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота')
        self.textEdit_2.clear()

        for chosen_day in day_of_week:
            self.textEdit_2.append('\t')
            self.textEdit_2.append('<font size="5"><u>' + chosen_day + '</u></font>')
            try:
                request = query_in(DB_REQUEST_PREP.format(str(text), chosen_day))
                if request:
                    for kortege in request:
                        if kortege[3] == 1:
                            self.textEdit_2.append(
                                '<font size="4"><span style="color: red;">' + str(kortege[0]) + '</span>' + ' - ' + kortege[
                                    1] + ' ' + ' - ' + kortege[2] + '</font>')
                        if kortege[3] == 2:
                            self.textEdit_2.append(
                                '<font size="4"><span style="color: blue;">' + str(kortege[0]) + '</span>' + ' - ' + kortege[
                                    1] + ' ' + ' - ' + kortege[2] + '</font>')
                        if kortege[3] == 0:
                            self.textEdit_2.append(
                                '<font size="4"><span style="color: black;">' + str(kortege[0]) + '</span>' + ' - ' + kortege[
                                    1] + ' ' + ' - ' + kortege[2] + '</font>')
                else:
                    self.textEdit_2.append("\nВыходной")

            except:
                self.textEdit_2.append("Error")

    def btn_click(self):

        rnd = [random.randint(0, 1) for i in range(0, 10)]
        rndchoice = random.choice(rnd)

        if rndchoice == 1:
            self.label.setText("NOT NULL")
            self.label_2.setText("Lose(")

        if rndchoice == 0:
            self.label.setText("NULL")
            self.label_2.setText("WIN!")

    def btn_click_2(self):

        rnd = [random.randint(0, 1) for i in range(0, 10)]
        rndchoice = random.choice(rnd)

        if rndchoice == 1:
            self.label.setText("NOT NULL")
            self.label_2.setText("WIN!")

        if rndchoice == 0:
            self.label.setText("NULL")
            self.label_2.setText("Lose(")


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = ExampleApp()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()