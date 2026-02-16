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
import resources.resource_rc

class Ui_Program(object):
    def setupUi(self, Program):
        if not Program.objectName():
            Program.setObjectName(u"Program")
        Program.resize(775, 65)
        Program.setMinimumSize(QSize(150, 60))
        self.horizontalLayout_3 = QHBoxLayout(Program)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.icon_label = QLabel(Program)
        self.icon_label.setObjectName(u"icon_label")
        self.icon_label.setMinimumSize(QSize(40, 40))
        self.icon_label.setMaximumSize(QSize(50, 50))

        self.horizontalLayout_3.addWidget(self.icon_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(Program)
        self.label.setObjectName(u"label")

        self.horizontalLayout_2.addWidget(self.label)

        self.status_label = QLabel(Program)
        self.status_label.setObjectName(u"status_label")
        self.status_label.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.status_label)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.progress_bar = QProgressBar(Program)
        self.progress_bar.setObjectName(u"progress_bar")
        self.progress_bar.setValue(24)

        self.verticalLayout.addWidget(self.progress_bar)


        self.horizontalLayout_3.addLayout(self.verticalLayout)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.download_button = QToolButton(Program)
        self.download_button.setObjectName(u"download_button")
        self.download_button.setMinimumSize(QSize(30, 30))
        icon = QIcon()
        icon.addFile(u":/icons/icons/download.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.download_button.setIcon(icon)

        self.horizontalLayout.addWidget(self.download_button)

        self.install_button = QToolButton(Program)
        self.install_button.setObjectName(u"install_button")
        self.install_button.setMinimumSize(QSize(30, 30))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/install.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.install_button.setIcon(icon1)

        self.horizontalLayout.addWidget(self.install_button)

        self.download_and_install_button = QToolButton(Program)
        self.download_and_install_button.setObjectName(u"download_and_install_button")
        self.download_and_install_button.setMinimumSize(QSize(30, 30))
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/download_and_install.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.download_and_install_button.setIcon(icon2)

        self.horizontalLayout.addWidget(self.download_and_install_button)


        self.horizontalLayout_3.addLayout(self.horizontalLayout)


        self.retranslateUi(Program)

        QMetaObject.connectSlotsByName(Program)
    # setupUi

    def retranslateUi(self, Program):
        Program.setWindowTitle(QCoreApplication.translate("Program", u"Program", None))
        self.icon_label.setText("")
        self.label.setText(QCoreApplication.translate("Program", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u043f\u0440\u043e\u0433\u0440\u0430\u043c\u043c\u044b", None))
        self.status_label.setText("")
#if QT_CONFIG(tooltip)
        self.progress_bar.setToolTip(QCoreApplication.translate("Program", u"asd", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.progress_bar.setStatusTip(QCoreApplication.translate("Program", u"asd", None))
#endif // QT_CONFIG(statustip)
#if QT_CONFIG(whatsthis)
        self.progress_bar.setWhatsThis(QCoreApplication.translate("Program", u"asd", None))
#endif // QT_CONFIG(whatsthis)
        self.download_button.setText("")
        self.install_button.setText("")
        self.download_and_install_button.setText("")
    # retranslateUi

