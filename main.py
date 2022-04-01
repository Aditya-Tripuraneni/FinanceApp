import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.uic import loadUi
import financeDataBase

#testing comment again for master

def verify(user_input):
    try:
        int(user_input)
        print("Possible")
        return True
    except ValueError:
        print(f"Could not convert {user_input}!")
        return False


class FinanceMenu(QDialog):
    def __init__(self):
        super(FinanceMenu, self).__init__()
        loadUi("financeMenu.ui", self)
        self.enterAllDataButton.clicked.connect(self.send_all_data)
        self.viewTotalFunButton.clicked.connect(self.view_total_fun_expenses)
        self.viewTotalTransportationButton.clicked.connect(self.view_total_transport_expenses)
        self.viewTotalFoodButton.clicked.connect(self.view_total_food_expenses)
        self.viewTotalClothesButton.clicked.connect(self.view_total_clothes_expenses)
        self.viewTotalBillsButton.clicked.connect(self.view_total_bills_expenses)
        self.viewTotalOtherButton.clicked.connect(self.view_total_other_expenses)
        self.viewTotalExpenses.clicked.connect(self.view_all_expenses)
        self.viewFunGraph.clicked.connect(lambda: financeDataBase.graph("FUN"))
        self.viewTransportGraph.clicked.connect(lambda: financeDataBase.graph("TRANSPORTATION"))
        self.viewFoodGraph.clicked.connect(lambda: financeDataBase.graph("FOOD"))
        self.viewClothesGraph.clicked.connect(lambda: financeDataBase.graph("CLOTHES"))
        self.viewBillsGraph.clicked.connect(lambda: financeDataBase.graph("BILLS"))
        self.viewOtherGraph.clicked.connect(lambda: financeDataBase.graph("OTHER"))
        self.viewPieChart.clicked.connect(financeDataBase.graph_all)
        self.settingsButton.clicked.connect(self.go_settings)
        self.deletePrevFun.clicked.connect(lambda: financeDataBase.delete_recent("FUN"))
        self.deletePrevTransportation.clicked.connect(lambda: financeDataBase.delete_recent("TRANSPORTATION"))
        self.deletePrevFood.clicked.connect(lambda: financeDataBase.delete_recent("FOOD"))
        self.deletePrevClothes.clicked.connect(lambda: financeDataBase.delete_recent("CLOTHES"))
        self.deletePrevBills.clicked.connect(lambda: financeDataBase.delete_recent("BILLS"))
        self.deletePrevOther.clicked.connect(lambda: financeDataBase.delete_recent("OTHER"))
        self.enterGoalButton.clicked.connect(self.send_goal)
        self.goal = financeDataBase.get_data("GOAL")
        self.checkGoalButton.clicked.connect(self.check_at_goal)



    def send_all_data(self):
        if verify(self.funEntry.text()):
            financeDataBase.send_data("FUN", self.funEntry.text())
            print("Successful")
        if verify(self.transportationEntry.text()):
            financeDataBase.send_data("TRANSPORTATION", self.transportationEntry.text())
            print("Transportation was sent successfully")

        if verify(self.foodEntry.text()):
            financeDataBase.send_data("FOOD", self.foodEntry.text())
            print("Food was sent successfully")

        if verify(self.clothesEntry.text()):
            financeDataBase.send_data("CLOTHES", self.clothesEntry.text())
            print("Clothes sent successfully ")

        if verify(self.billsEntry.text()):
            financeDataBase.send_data("BILLS", self.billsEntry.text())
            print("Bills send successfully")

        if verify(self.otherEntry.text()):
            financeDataBase.send_data("OTHER", self.otherEntry.text())
            print("other sent successfully")

        # Clearing remaining text for user
        self.funEntry.setText("")
        self.transportationEntry.setText("")
        self.foodEntry.setText("")
        self.clothesEntry.setText("")
        self.billsEntry.setText("")
        self.otherEntry.setText("")

    def send_goal(self):
        if verify(self.goalEntry.text()):
            financeDataBase.update_record("GOAL", self.goalEntry.text())
        self.goalEntry.setText("")

    def check_at_goal(self):
        if financeDataBase.get_total_spent() > self.goal[0][0]:
            print("You have exceeded your budget!")
            self.spentSpecificLabel.setText("You are over budget")
        elif 0 <= (self.goal[0][0] - financeDataBase.get_total_spent()) <= 500:
            self.spentSpecificLabel.setText(f"You are $500 within the budget, your budget is ${self.goal[0][0]}")
        elif financeDataBase.get_total_spent() < self.goal[0][0]:
            self.spentSpecificLabel.setText("You are under budget don't worry!")
        else:
            self.spentSpecificLabel.setText("You reached budget!")

    def view_total_fun_expenses(self):
        spent = financeDataBase.sum_partic_expense("FUN")
        if spent is not None:
            self.spentSpecificLabel.setText(f"You spent ${round(spent)} on Fun")
        else:
            self.spentSpecificLabel.setText("Nothing spent on fun yet! Try entering something")

    def view_total_transport_expenses(self):
        spent = financeDataBase.sum_partic_expense("TRANSPORTATION")
        if spent is not None:
            self.spentSpecificLabel.setText(f"You spent ${round(spent)} on Transportation")
        else:
            self.spentSpecificLabel.setText("Nothing spent on transportation yet! Try entering something")

    def view_total_food_expenses(self):
        spent = financeDataBase.sum_partic_expense("FOOD")
        if spent is not None:
            self.spentSpecificLabel.setText(f"You spent ${round(spent)} on Food")
        else:
            self.spentSpecificLabel.setText("Nothing spent on food yet! Try entering something")

    def view_total_clothes_expenses(self):
        spent = financeDataBase.sum_partic_expense("CLOTHES")
        if spent is not None:
            self.spentSpecificLabel.setText(f"You spent ${round(spent)} on Clothes")
        else:
            self.spentSpecificLabel.setText("Nothing spent on clothes yet! Try entering something")

    def view_total_bills_expenses(self):
        spent = financeDataBase.sum_partic_expense("BILLS")
        if spent is not None:
            self.spentSpecificLabel.setText(f"You spent ${round(spent)} on Bills")
        else:
            self.spentSpecificLabel.setText("Nothing spent on bills yet! Try entering something")

    def view_total_other_expenses(self):
        spent = financeDataBase.sum_partic_expense("OTHER")
        if spent is not None:
            self.spentSpecificLabel.setText(f"You spent ${round(spent)} on Other")
        else:
            self.spentSpecificLabel.setText("Nothing spent on other yet! Try entering something")

    def view_all_expenses(self):
        spent = financeDataBase.get_total_spent()
        self.spentSpecificLabel.setText(f"TOTAL Expenses: ${round(spent)}")

    def go_settings(self):
        settings_window = Settings()
        widget.addWidget(settings_window)
        widget.setCurrentIndex(widget.currentIndex() + 1)


class Settings(QDialog):
    def __init__(self):
        super(Settings, self).__init__()
        loadUi("settings.ui", self)
        self.homeButton.clicked.connect(self.go_home)
        self.submitButton.clicked.connect(self.change_back_colour)

    def go_home(self):
        widget.setCurrentIndex(widget.currentIndex() - 1)

    def change_back_colour(self):
        state = self.colorSelectBox.currentText()

        if state == "Mauve":
            window.setStyleSheet("""QDialog#Dialog{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, 
            y2:1, stop:0 rgba(66, 39, 90, 1), stop:1 rgba(115, 75, 109, 1)) }""")
        elif state == "Green Blue":
            window.setStyleSheet("""QDialog#Dialog{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, 
            y2:1, stop:0 rgba(67, 206, 162, 1), stop:1 rgba(24, 90, 157, 1)) }""")
        else:
            window.setStyleSheet("""QDialog#Dialog{ background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, 
            y2:1, stop:0 rgba(221, 214, 243, 1), stop:1 rgba(250, 172, 168, 1)) }""")


app = QApplication(sys.argv)

widget = QtWidgets.QStackedWidget()
window = FinanceMenu()

widget.addWidget(window)

widget.setFixedWidth(1000)
widget.setFixedHeight(1000)
widget.show()
app.exec_()
