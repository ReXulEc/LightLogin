import json
import sys
from settings import * # You can customize on 'settings.py' file
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton, QLabel, QLineEdit, QGridLayout, QMessageBox)
from PyQt5 import QtGui


#Json Database
f = open(database, )
data = json.load(f)


class LoginWindow(QWidget):
	def __init__(panel):
		super().__init__()
		panel.setWindowTitle(mainbaslik)
		panel.setWindowIcon(QtGui.QIcon('Extra/ico.ico'))
		panel.resize(500, 120)

		label_name = QLabel('<font size="4"> %s </font>' % mainisim )
		panel.lineEdit_username = QLineEdit()
		panel.lineEdit_username.setPlaceholderText(isimplaceholder)

		layout = QGridLayout()
		layout.addWidget(label_name, 0, 0)
		layout.addWidget(panel.lineEdit_username, 0, 1)


		label_password = QLabel('<font size="4"> %s </font>' % mainsifre)
		panel.lineEdit_password = QLineEdit()
		panel.lineEdit_password.setPlaceholderText(sifreplaceholder)
		layout.addWidget(label_password, 1, 0)
		layout.addWidget(panel.lineEdit_password, 1, 1)

		button_login = QPushButton(girisButon)
		button_login.clicked.connect(panel.check_password)
		layout.addWidget(button_login, 2, 0, 1, 2)
		layout.setRowMinimumHeight(2, 75)

		panel.setLayout(layout)

	def check_password(panel):
		msg = QMessageBox()

		if panel.lineEdit_username.text() in data and panel.lineEdit_password.text() == data[panel.lineEdit_username.text()]:
			msg.setWindowTitle(basariliB)
			msg.setText(basariliNormal + '\n' + basariliIsim + panel.lineEdit_username.text() + '\n' + basariliSifre + panel.lineEdit_password.text())
			msg.exec_()
		else:
			msg.setWindowTitle(hataliB)
			msg.setText(hataliNormal + hataliErrorMsg)
			msg.exec_()

if __name__ == '__main__':
	uyglm = QApplication(sys.argv)

	realapp = LoginWindow()
	realapp.show()

	sys.exit(uyglm.exec_())