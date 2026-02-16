# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'program.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QProgressBar,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_Program(object):
    def setupUi(self, Program):
        if not Program.objectName():
            Program.setObjectName(u"Program")
        Program.resize(505, 82)
        self.horizontalLayout_2 = QHBoxLayout(Program)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Program)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.progress_bar = QProgressBar(Program)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(24)

        self.verticalLayout.addWidget(self.progress_bar)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.download_button = QToolButton(Program)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setMinimumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.download_button)

        self.install_button = QToolButton(Program)
        self.install_button.setObjectName(u"install_button")
        self.install_button.setMinimumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.install_button)

        self.download_and_install_button = QToolButton(Program)
        self.download_and_install_button.setObjectName(u"download_and_install_button")
        self.download_and_install_button.setMinimumSize(QSize(30, 30))

        self.horizontalLayout.addWidget(self.download_and_install_button)


        self.horizontalLayout_2.addLayout(self.horizontalLayout)


        self.retranslateUi(Program)

        QMetaObject.connectSlotsByName(Program)
    # setupUi

    def retranslateUi(self, Program):
        Program.setWindowTitle(QCoreApplication.translate("Program", u"Program", None))
        self.label.setText(QCoreApplication.translate("Program", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.download_button.setText(QCoreApplication.translate("Program", u"...", None))
        self.install_button.setText(QCoreApplication.translate("Program", u"...", None))
        self.download_and_install_button.setText(QCoreApplication.translate("Program", u"...", None))
    # retranslateUi

