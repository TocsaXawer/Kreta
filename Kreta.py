from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import *
from PyQt5.QtPrintSupport import *

import os
import sys

class AboutDialog(QDialog):
    def __init__(self, *args, **kwargs):
        super(AboutDialog, self).__init__(*args, **kwargs)

        QBtn = QDialogButtonBox.Ok  # No cancel
        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)
        layout = QVBoxLayout()
        for i in range(0, layout.count()):
            layout.itemAt(i).setAlignment(Qt.AlignHCenter)
        layout.addWidget(self.buttonBox)
        self.setLayout(layout)


class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl("https://mrk.e-kreta.hu/Adminisztracio/Login"))


        self.browser.loadFinished.connect(self.update_title)
        self.setCentralWidget(self.browser)

        self.status = QStatusBar()
        self.setStatusBar(self.status)

        navtb = QToolBar("Navigation")
        navtb.setIconSize(QSize(16, 16))
        self.addToolBar(navtb)




        self.httpsicon = QLabel()  # Yes, really!


        self.urlbar = QLineEdit()
        self.show()

    def update_title(self):
        title = self.browser.page().title()
        self.setWindowTitle("%s - MCS" % title)


app = QApplication(sys.argv)
app.setApplicationName("MCS")
app.setOrganizationName("MCS")
app.setOrganizationDomain("MCS")

window = MainWindow()

app.exec_()