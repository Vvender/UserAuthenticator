import sys
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget
from event_handler import EventHandler
from Gui.ui_login import Ui_Login


class MainWindow:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.ui_window = QWidget()
        self.ui = Ui_Login()
        self.ui.setupUi(self.ui_window)
        self.ui_window.show()

        # Create an instance of EventHandler and pass the app and ui objects
        self.event_handler = EventHandler(self.app, self.ui)

        # Main Button Events
        self.ui.btn_minimize.clicked.connect(self.ui_window.showMinimized)
        self.ui.btn_expand.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_exit.clicked.connect(self.app.quit)
        self.ui.btn_toggle_password.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_git.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_linkedin.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_email.clicked.connect(self.event_handler.main_event_handler)
        self.ui.btn_cv.clicked.connect(self.event_handler.main_event_handler)

        # Mouse Press Events
        # self.ui.lbl_frame_back.mousePressEvent()

        # Login Button Events
        self.ui.btn_lgn_login.clicked.connect(self.event_handler.login_event_handler)
        self.ui.btn_lgn_info.clicked.connect(self.event_handler.login_event_handler)
        self.ui.btn_lgn_register.clicked.connect(self.event_handler.login_event_handler)

        # Register Button Events
        self.ui.btn_rg_register.clicked.connect(self.event_handler.register_event_handler)

        # Message Button Events
        self.ui.btn_info_return.clicked.connect(self.event_handler.message_event_handler)

        # Countdown Event
        self.event_handler.countdown_timer = QTimer()
        self.event_handler.countdown_timer.timeout.connect(self.event_handler.update_countdown_label)


if __name__ == "__main__":
    main_app = MainWindow()
    sys.exit(main_app.app.exec_())
