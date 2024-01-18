import webbrowser
from PyQt5.QtCore import QUrl
from PyQt5.QtGui import QDesktopServices


class UtilityEventHandler:
    def __init__(self, app, ui):
        self.app = app
        self.ui = ui

    def utility_event_handler(self):
        try:
            # Get the sender of the event
            sender = self.app.sender()
            # Check if the sender is the GitHub button
            if sender == self.ui.btn_git:
                # Open the GitHub URL
                QDesktopServices.openUrl(QUrl('https://github.com/Vvender'))
            # Check if the sender is the LinkedIn button
            elif sender == self.ui.btn_linkedin:
                # Open the LinkedIn URL
                QDesktopServices.openUrl(QUrl('https://www.linkedin.com/in/ozan-çatak-06a35a162/'))
            # Check if the sender is the email button
            elif sender == self.ui.btn_email:
                # Open the default email client with the specified email address
                webbrowser.open('mailto:ozancatak@hotmail.com')
            # Check if the sender is the CV button
            elif sender == self.ui.btn_cv:
                # Open the CV URL
                QDesktopServices.openUrl(QUrl('https://amethyst-nancee-79.tiiny.site'))
        # Handle any exceptions that occur
        except Exception as e:
            custom_exception = CustomExceptionHandler(e)
            print(f"An error occurred during utility event,Error Code: {custom_exception.error_code}, Message: {custom_exception.error_message}")
