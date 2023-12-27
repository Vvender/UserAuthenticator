from PyQt5 import QtCore, QtGui, QtWidgets
import Gui.Icons.login_rc as login_rc


class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(450, 550)
        Login.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        Login.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Login.sizePolicy().hasHeightForWidth())
        Login.setSizePolicy(sizePolicy)
        Login.setMinimumSize(QtCore.QSize(450, 550))
        Login.setMaximumSize(QtCore.QSize(675, 825))
        Login.setStyleSheet("")
        self.mainBody = QtWidgets.QWidget(Login)
        self.mainBody.setGeometry(QtCore.QRect(40, 40, 370, 480))
        self.mainBody.setStyleSheet("")
        self.mainBody.setObjectName("mainBody")
        self.lbl_frame_back = QtWidgets.QLabel(self.mainBody)
        self.lbl_frame_back.setGeometry(QtCore.QRect(40, 39, 281, 421))
        self.lbl_frame_back.setStyleSheet("background-color:#2596be;\n"
                                          "border-radius:20px;\n"
                                          "")
        self.lbl_frame_back.setText("")
        self.lbl_frame_back.setObjectName("lbl_frame_back")
        self.lbl_frame_middle = QtWidgets.QLabel(self.mainBody)
        self.lbl_frame_middle.setGeometry(QtCore.QRect(40, 39, 281, 421))
        self.lbl_frame_middle.setStyleSheet(
            "background-color:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:0.715909,stop:0 rgba(0,0,0,9), stop:0.375 rgba(0,0,0,50),stop:0.835227 rgba(0,0,0,75));\n"
            "border-radius:20px;\n"
            "")
        self.lbl_frame_middle.setText("")
        self.lbl_frame_middle.setObjectName("lbl_frame_middle")
        self.lbl_frame_front = QtWidgets.QLabel(self.mainBody)
        self.lbl_frame_front.setGeometry(QtCore.QRect(50, 50, 261, 401))
        self.lbl_frame_front.setStyleSheet("background-color:rgba(0,0,0,100);\n"
                                           "border-radius:15px;")
        self.lbl_frame_front.setText("")
        self.lbl_frame_front.setObjectName("lbl_frame_front")
        self.btn_git = QtWidgets.QPushButton(self.mainBody)
        self.btn_git.setGeometry(QtCore.QRect(60, 400, 32, 32))
        self.btn_git.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_git.setStyleSheet("QPushButton#btn_git{\n"
                                   "    background-color: transparent;\n"
                                   "    color:rgba(255, 255, 255, 210);\n"
                                   "    border-radius:5px;\n"
                                   "}\n"
                                   "QPushButton#btn_git:hover{\n"
                                   "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                   "}\n"
                                   "QPushButton#btn_git:pressed{\n"
                                   "    padding-left:5px;\n"
                                   "    padding-top:5px;\n"
                                   "    background-color:rgba(105, 118, 132, 200);\n"
                                   "}")
        self.btn_git.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/Icons/code.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_git.setIcon(icon)
        self.btn_git.setIconSize(QtCore.QSize(32, 32))
        self.btn_git.setObjectName("btn_git")
        self.btn_linkedin = QtWidgets.QPushButton(self.mainBody)
        self.btn_linkedin.setGeometry(QtCore.QRect(130, 400, 32, 32))
        self.btn_linkedin.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_linkedin.setStyleSheet("QPushButton#btn_linkedin{\n"
                                        "    background-color: transparent;\n"
                                        "    color:rgba(255, 255, 255, 210);\n"
                                        "    border-radius:5px;\n"
                                        "}\n"
                                        "QPushButton#btn_linkedin:hover{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                        "}\n"
                                        "QPushButton#btn_linkedin:pressed{\n"
                                        "    padding-left:5px;\n"
                                        "    padding-top:5px;\n"
                                        "    background-color:rgba(105, 118, 132, 200);\n"
                                        "}")
        self.btn_linkedin.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/Icons/linkedin.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_linkedin.setIcon(icon1)
        self.btn_linkedin.setIconSize(QtCore.QSize(32, 32))
        self.btn_linkedin.setObjectName("btn_linkedin")
        self.btn_email = QtWidgets.QPushButton(self.mainBody)
        self.btn_email.setGeometry(QtCore.QRect(200, 400, 32, 32))
        self.btn_email.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_email.setStyleSheet("QPushButton#btn_email{\n"
                                     "    background-color: transparent;\n"
                                     "    color:rgba(255, 255, 255, 210);\n"
                                     "    border-radius:5px;\n"
                                     "}\n"
                                     "QPushButton#btn_email:hover{\n"
                                     "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                     "}\n"
                                     "QPushButton#btn_email:pressed{\n"
                                     "    padding-left:5px;\n"
                                     "    padding-top:5px;\n"
                                     "    background-color:rgba(105, 118, 132, 200);\n"
                                     "}")
        self.btn_email.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/Icons/mail.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_email.setIcon(icon2)
        self.btn_email.setIconSize(QtCore.QSize(32, 32))
        self.btn_email.setObjectName("btn_email")
        self.btn_cv = QtWidgets.QPushButton(self.mainBody)
        self.btn_cv.setGeometry(QtCore.QRect(270, 400, 32, 32))
        self.btn_cv.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cv.setStyleSheet("QPushButton#btn_cv{\n"
                                  "    background-color: transparent;\n"
                                  "    color:rgba(255, 255, 255, 210);\n"
                                  "    border-radius:5px;\n"
                                  "}\n"
                                  "QPushButton#btn_cv:hover{\n"
                                  "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                  "}\n"
                                  "QPushButton#btn_cv:pressed{\n"
                                  "    padding-left:5px;\n"
                                  "    padding-top:5px;\n"
                                  "    background-color:rgba(105, 118, 132, 200);\n"
                                  "}")
        self.btn_cv.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/Icons/clipboard.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cv.setIcon(icon3)
        self.btn_cv.setIconSize(QtCore.QSize(32, 32))
        self.btn_cv.setObjectName("btn_cv")
        self.btn_minimize = QtWidgets.QPushButton(self.mainBody)
        self.btn_minimize.setGeometry(QtCore.QRect(220, 60, 16, 16))
        self.btn_minimize.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimize.setStyleSheet("background-color: transparent;\n"
                                        "")
        self.btn_minimize.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/Icons/chevron-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_minimize.setIcon(icon4)
        self.btn_minimize.setIconSize(QtCore.QSize(32, 32))
        self.btn_minimize.setObjectName("btn_minimize")
        self.btn_expand = QtWidgets.QPushButton(self.mainBody)
        self.btn_expand.setGeometry(QtCore.QRect(250, 60, 16, 16))
        self.btn_expand.setMaximumSize(QtCore.QSize(16, 16))
        self.btn_expand.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_expand.setStyleSheet("background-color: transparent;\n"
                                      "")
        self.btn_expand.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/Icons/maximize-2 .svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_expand.setIcon(icon5)
        self.btn_expand.setIconSize(QtCore.QSize(32, 32))
        self.btn_expand.setObjectName("btn_expand")
        self.btn_exit = QtWidgets.QPushButton(self.mainBody)
        self.btn_exit.setGeometry(QtCore.QRect(280, 60, 16, 16))
        self.btn_exit.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_exit.setStyleSheet("background-color: transparent;\n"
                                    "")
        self.btn_exit.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/Icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_exit.setIcon(icon6)
        self.btn_exit.setIconSize(QtCore.QSize(32, 32))
        self.btn_exit.setObjectName("btn_exit")
        self.pages = QtWidgets.QStackedWidget(self.mainBody)
        self.pages.setGeometry(QtCore.QRect(60, 140, 241, 251))
        self.pages.setStyleSheet(
            "background-color:qlineargradient(spread:pad,x1:0,y1:0,x2:0,y2:0.715909,stop:0 rgba(0,0,0,9), stop:0.375 rgba(0,0,0,25),stop:0.835227 rgba(0,0,0,25));\n"
            "border-radius:40px;")
        self.pages.setObjectName("pages")
        self.login_page = QtWidgets.QWidget()
        self.login_page.setObjectName("login_page")
        self.btn_lgn_register = QtWidgets.QPushButton(self.login_page)
        self.btn_lgn_register.setGeometry(QtCore.QRect(140, 200, 75, 23))
        self.btn_lgn_register.setStyleSheet("QPushButton#btn_lgn_register{\n"
                                            "    background-color: transparent;\n"
                                            "    color:rgba(255, 255, 255, 210);\n"
                                            "    border-radius:5px;\n"
                                            "}\n"
                                            "QPushButton#btn_lgn_register:hover{\n"
                                            "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                            "}\n"
                                            "QPushButton#btn_lgn_register:pressed{\n"
                                            "    padding-left:5px;\n"
                                            "    padding-top:5px;\n"
                                            "    background-color:rgba(105, 118, 132, 200);\n"
                                            "}")
        self.btn_lgn_register.setObjectName("btn_lgn_register")
        self.btn_lgn_login = QtWidgets.QPushButton(self.login_page)
        self.btn_lgn_login.setGeometry(QtCore.QRect(20, 150, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_lgn_login.setFont(font)
        self.btn_lgn_login.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_lgn_login.setStyleSheet("QPushButton#btn_lgn_login{\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
                                         "    color:rgba(255, 255, 255, 210);\n"
                                         "    border-radius:5px;\n"
                                         "}\n"
                                         "QPushButton#btn_lgn_login:hover{\n"
                                         "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                         "}\n"
                                         "QPushButton#btn_lgn_login:pressed{\n"
                                         "    padding-left:5px;\n"
                                         "    padding-top:5px;\n"
                                         "    background-color:rgba(105, 118, 132, 200);\n"
                                         "}")
        self.btn_lgn_login.setObjectName("btn_lgn_login")
        self.line_lgn_password = QtWidgets.QLineEdit(self.login_page)
        self.line_lgn_password.setGeometry(QtCore.QRect(20, 85, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_lgn_password.setFont(font)
        self.line_lgn_password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                             "border:none;\n"
                                             "border-bottom:2px solid rgba(105,1118,132,255);\n"
                                             "color:rgba(255,255,255,230);\n"
                                             "padding-bottom:7px;")
        self.line_lgn_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_lgn_password.setAlignment(QtCore.Qt.AlignCenter)
        self.line_lgn_password.setObjectName("line_lgn_password")
        self.line_lgn_userName = QtWidgets.QLineEdit(self.login_page)
        self.line_lgn_userName.setGeometry(QtCore.QRect(20, 25, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_lgn_userName.setFont(font)
        self.line_lgn_userName.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                             "border:none;\n"
                                             "border-bottom:2px solid rgba(105,1118,132,255);\n"
                                             "color:rgba(255,255,255,230);\n"
                                             "padding-bottom:7px;")
        self.line_lgn_userName.setAlignment(QtCore.Qt.AlignCenter)
        self.line_lgn_userName.setObjectName("line_lgn_userName")
        self.btn_lgn_info = QtWidgets.QPushButton(self.login_page)
        self.btn_lgn_info.setGeometry(QtCore.QRect(30, 200, 75, 23))
        self.btn_lgn_info.setStyleSheet("QPushButton#btn_lgn_info{\n"
                                        "    background-color: transparent;\n"
                                        "    color:rgba(255, 255, 255, 210);\n"
                                        "    border-radius:5px;\n"
                                        "}\n"
                                        "QPushButton#btn_lgn_info:hover{\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                        "}\n"
                                        "QPushButton#btn_lgn_info:pressed{\n"
                                        "    padding-left:5px;\n"
                                        "    padding-top:5px;\n"
                                        "    background-color:rgba(105, 118, 132, 200);\n"
                                        "}")
        self.btn_lgn_info.setObjectName("btn_lgn_info")
        self.pages.addWidget(self.login_page)
        self.info_page = QtWidgets.QWidget()
        self.info_page.setObjectName("info_page")
        self.btn_info_return = QtWidgets.QPushButton(self.info_page)
        self.btn_info_return.setGeometry(QtCore.QRect(10, 190, 221, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_info_return.setFont(font)
        self.btn_info_return.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_info_return.setStyleSheet("QPushButton#btn_info_return{\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
                                           "    color:rgba(255, 255, 255, 210);\n"
                                           "    border-radius:5px;\n"
                                           "}\n"
                                           "QPushButton#btn_info_return:hover{\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                           "}\n"
                                           "QPushButton#btn_info_return:pressed{\n"
                                           "    padding-left:5px;\n"
                                           "    padding-top:5px;\n"
                                           "    background-color:rgba(105, 118, 132, 200);\n"
                                           "}")
        self.btn_info_return.setObjectName("btn_info_return")
        self.lbl_info_message = QtWidgets.QLabel(self.info_page)
        self.lbl_info_message.setGeometry(QtCore.QRect(10, 20, 221, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_info_message.setFont(font)
        self.lbl_info_message.setStyleSheet("color:rgba(255,255,255,210);\n"
                                            "border-radius:20px;\n"
                                            "")
        self.lbl_info_message.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_info_message.setWordWrap(True)
        self.lbl_info_message.setObjectName("lbl_info_message")
        self.pages.addWidget(self.info_page)
        self.register_page = QtWidgets.QWidget()
        self.register_page.setObjectName("register_page")
        self.btn_rg_register = QtWidgets.QPushButton(self.register_page)
        self.btn_rg_register.setGeometry(QtCore.QRect(20, 185, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.btn_rg_register.setFont(font)
        self.btn_rg_register.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_rg_register.setStyleSheet("QPushButton#btn_rg_register{\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(20, 47, 78, 219), stop:1 rgba(85, 98, 112, 226));\n"
                                           "    color:rgba(255, 255, 255, 210);\n"
                                           "    border-radius:5px;\n"
                                           "}\n"
                                           "QPushButton#btn_rg_register:hover{\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                           "}\n"
                                           "QPushButton#btn_rg_registern:pressed{\n"
                                           "    padding-left:5px;\n"
                                           "    padding-top:5px;\n"
                                           "    background-color:rgba(105, 118, 132, 200);\n"
                                           "}")
        self.btn_rg_register.setObjectName("btn_rg_register")
        self.line_rg_password = QtWidgets.QLineEdit(self.register_page)
        self.line_rg_password.setGeometry(QtCore.QRect(20, 50, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_rg_password.setFont(font)
        self.line_rg_password.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                            "border:none;\n"
                                            "border-bottom:2px solid rgba(105,1118,132,255);\n"
                                            "color:rgba(255,255,255,230);\n"
                                            "padding-bottom:7px;")
        self.line_rg_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.line_rg_password.setAlignment(QtCore.Qt.AlignCenter)
        self.line_rg_password.setObjectName("line_rg_password")
        self.line_rg_userName = QtWidgets.QLineEdit(self.register_page)
        self.line_rg_userName.setGeometry(QtCore.QRect(20, 10, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_rg_userName.setFont(font)
        self.line_rg_userName.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                            "border:none;\n"
                                            "border-bottom:2px solid rgba(105,1118,132,255);\n"
                                            "color:rgba(255,255,255,230);\n"
                                            "padding-bottom:7px;")
        self.line_rg_userName.setAlignment(QtCore.Qt.AlignCenter)
        self.line_rg_userName.setObjectName("line_rg_userName")
        self.line_rg_email = QtWidgets.QLineEdit(self.register_page)
        self.line_rg_email.setGeometry(QtCore.QRect(20, 100, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_rg_email.setFont(font)
        self.line_rg_email.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                         "border:none;\n"
                                         "border-bottom:2px solid rgba(105,1118,132,255);\n"
                                         "color:rgba(255,255,255,230);\n"
                                         "padding-bottom:7px;")
        self.line_rg_email.setAlignment(QtCore.Qt.AlignCenter)
        self.line_rg_email.setObjectName("line_rg_email")
        self.line_rg_phone = QtWidgets.QLineEdit(self.register_page)
        self.line_rg_phone.setGeometry(QtCore.QRect(20, 140, 200, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.line_rg_phone.setFont(font)
        self.line_rg_phone.setStyleSheet("background-color:rgba(0,0,0,0);\n"
                                         "border:none;\n"
                                         "border-bottom:2px solid rgba(105,1118,132,255);\n"
                                         "color:rgba(255,255,255,230);\n"
                                         "padding-bottom:7px;")
        self.line_rg_phone.setAlignment(QtCore.Qt.AlignCenter)
        self.line_rg_phone.setObjectName("line_rg_phone")
        self.pages.addWidget(self.register_page)
        self.btn_toggle_password = QtWidgets.QPushButton(self.mainBody)
        self.btn_toggle_password.setGeometry(QtCore.QRect(60, 50, 31, 31))
        self.btn_toggle_password.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_toggle_password.setStyleSheet("QPushButton#btn_toggle_password{\n"
                                               "    background-color: transparent;\n"
                                               "    color:rgba(255, 255, 255, 210);\n"
                                               "    border-radius:5px;\n"
                                               "}\n"
                                               "QPushButton#btn_toggle_password:hover{\n"
                                               "    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(40, 67, 98, 219), stop:1 rgba(105, 118, 132, 226));\n"
                                               "}\n"
                                               "QPushButton#btn_toggle_password:pressed{\n"
                                               "    padding-left:5px;\n"
                                               "    padding-top:5px;\n"
                                               "    background-color:rgba(105, 118, 132, 200);\n"
                                               "}")
        self.btn_toggle_password.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/Icons/eye.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_toggle_password.setIcon(icon7)
        self.btn_toggle_password.setIconSize(QtCore.QSize(32, 32))
        self.btn_toggle_password.setObjectName("btn_toggle_password")
        self.lbl_login = QtWidgets.QLabel(self.mainBody)
        self.lbl_login.setGeometry(QtCore.QRect(110, 90, 141, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_login.setFont(font)
        self.lbl_login.setStyleSheet("color:rgba(255,255,255,210);\n"
                                           "border-radius:40px;\n"
                                           "")
        self.lbl_login.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_login.setObjectName("lbl_lgn_login_2")

        self.retranslateUi(Login)
        self.pages.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Login)

        # Tab Order
        Login.setTabOrder(self.btn_toggle_password, self.btn_minimize)
        Login.setTabOrder(self.btn_minimize, self.btn_expand)
        Login.setTabOrder(self.btn_expand, self.btn_exit)
        Login.setTabOrder(self.btn_exit, self.line_lgn_userName)
        Login.setTabOrder(self.line_lgn_userName, self.line_lgn_password)
        Login.setTabOrder(self.line_lgn_password, self.btn_lgn_login)
        Login.setTabOrder(self.btn_lgn_login, self.btn_lgn_info)
        Login.setTabOrder(self.btn_lgn_info, self.btn_lgn_register)
        Login.setTabOrder(self.btn_lgn_register, self.btn_git)
        Login.setTabOrder(self.btn_git, self.btn_linkedin)
        Login.setTabOrder(self.btn_linkedin, self.btn_email)
        Login.setTabOrder(self.btn_email, self.btn_cv)
        Login.setTabOrder(self.btn_cv, self.btn_info_return)
        Login.setTabOrder(self.btn_info_return, self.line_rg_userName)
        Login.setTabOrder(self.line_rg_userName, self.line_rg_password)
        Login.setTabOrder(self.line_rg_password, self.line_rg_email)
        Login.setTabOrder(self.line_rg_email, self.line_rg_phone)
        Login.setTabOrder(self.line_rg_phone, self.btn_rg_register)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Form"))
        self.btn_lgn_register.setText(_translate("Login", "Register"))
        self.btn_lgn_login.setText(_translate("Login", "Log In"))
        self.line_lgn_password.setPlaceholderText(_translate("Login", "Password"))
        self.line_lgn_userName.setPlaceholderText(_translate("Login", "User Name"))
        self.btn_lgn_info.setText(_translate("Login", "Info"))
        self.btn_info_return.setText(_translate("Login", "Return"))
        self.lbl_info_message.setText(
            _translate("Login", "<html><head/><body><p align=\"center\">Info Message</p></body></html>"))
        self.btn_rg_register.setText(_translate("Login", "Register"))
        self.line_rg_password.setPlaceholderText(_translate("Login", "Password"))
        self.line_rg_userName.setPlaceholderText(_translate("Login", "User Name"))
        self.line_rg_email.setPlaceholderText(_translate("Login", "Email"))
        self.line_rg_phone.setPlaceholderText(_translate("Login", "Phone"))
        self.lbl_login.setText(_translate("Login", "Log In"))
