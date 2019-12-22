from PyQt5 import QtWidgets, uic
import sys


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('main.ui', self)
        # stack initialization
        self.controlStack = self.findChild(QtWidgets.QStackedWidget, 'stackedWidget')
        # numpad initialization
        self.numpad = []
        for i in range(0, 10):
            self.numpad.append(self.findChild(QtWidgets.QLabel, 'num' + str(i)))
        # numpad[10] = dot, numpad[11] = clear, numpad[12] = enter
        self.numpad.append(self.findChild(QtWidgets.QLabel, 'dot'))
        self.numpad.append(self.findChild(QtWidgets.QLabel, 'clear'))
        self.numpad.append(self.findChild(QtWidgets.QLabel, 'enter'))

        self.numpadDefaultStyleSheet = self.numpad[0].styleSheet()
        self.numpadClearDefaultStyleSheet = self.numpad[11].styleSheet()
        self.numpadEnterDefaultStyleSheet = self.numpad[12].styleSheet()

        self.numpad[0].mousePressEvent = self.num0press
        self.numpad[0].mouseReleaseEvent = self.num0release
        self.numpad[1].mousePressEvent = self.num1press
        self.numpad[1].mouseReleaseEvent = self.num1release
        self.numpad[2].mousePressEvent = self.num2press
        self.numpad[2].mouseReleaseEvent = self.num2release
        self.numpad[3].mousePressEvent = self.num3press
        self.numpad[3].mouseReleaseEvent = self.num3release
        self.numpad[4].mousePressEvent = self.num4press
        self.numpad[4].mouseReleaseEvent = self.num4release
        self.numpad[5].mousePressEvent = self.num5press
        self.numpad[5].mouseReleaseEvent = self.num5release
        self.numpad[6].mousePressEvent = self.num6press
        self.numpad[6].mouseReleaseEvent = self.num6release
        self.numpad[7].mousePressEvent = self.num7press
        self.numpad[7].mouseReleaseEvent = self.num7release
        self.numpad[8].mousePressEvent = self.num8press
        self.numpad[8].mouseReleaseEvent = self.num8release
        self.numpad[9].mousePressEvent = self.num9press
        self.numpad[9].mouseReleaseEvent = self.num9release
        self.numpad[10].mousePressEvent = self.num10press
        self.numpad[10].mouseReleaseEvent = self.num10release
        self.numpad[11].mousePressEvent = self.num11press
        self.numpad[11].mouseReleaseEvent = self.num11release
        self.numpad[12].mousePressEvent = self.num12press
        self.numpad[12].mouseReleaseEvent = self.num12release

        # output init.
        self.output = self.findChild(QtWidgets.QLabel, 'output')
        self.show()
    def numpadPress(self,num):
        self.numpad[num].setStyleSheet("background-color: rgb(50, 50, 50);\ncolor: rgb(0, 0, 0);")
    def numpadRelease(self,num):
        self.numpad[num].setStyleSheet(self.numpadDefaultStyleSheet)
        if self.output.text() == "0":
            self.output.setText(str(num))
        else:
            self.output.setText(self.output.text() + str(num))

    def num0press(self, event):
        self.numpadPress(0)
    def num0release(self,event):
        self.numpad[0].setStyleSheet(self.numpadDefaultStyleSheet)
        if self.output.text() != "0":
            self.output.setText(self.output.text() + "0")
    
    def num1press(self, event):
        self.numpadPress(1)
    def num1release(self,event):
        self.numpadRelease(1)
    
    def num2press(self, event):
        self.numpadPress(2)
    def num2release(self,event):
        self.numpadRelease(2)
    
    def num3press(self, event):
        self.numpadPress(3)
    def num3release(self,event):
        self.numpadRelease(3)

    def num4press(self, event):
        self.numpadPress(4)
    def num4release(self,event):
        self.numpadRelease(4)

    def num5press(self, event):
        self.numpadPress(5)
    def num5release(self,event):
        self.numpadRelease(5)
    
    def num6press(self, event):
        self.numpadPress(6)
    def num6release(self,event):
        self.numpadRelease(6)
    
    def num7press(self, event):
        self.numpadPress(7)
    def num7release(self,event):
        self.numpadRelease(7)
    
    def num8press(self, event):
        self.numpadPress(8)
    def num8release(self,event):
        self.numpadRelease(8)
    
    def num9press(self, event):
        self.numpadPress(9)
    def num9release(self,event):
        self.numpadRelease(9)
    # 'dot'
    def num10press(self, event):
        self.numpadPress(10)
    def num10release(self,event):
        self.numpad[10].setStyleSheet(self.numpadDefaultStyleSheet)
        if "." not in self.output.text():
            self.output.setText(self.output.text() + ".")
    # 'clear'
    def num11press(self, event):
        self.numpad[11].setStyleSheet("background-color: rgb(50, 0, 0);\ncolor: rgb(50, 50, 50);")
    def num11release(self,event):
        self.numpad[11].setStyleSheet(self.numpadClearDefaultStyleSheet)
        self.output.setText("0")
    # 'enter'
    def num12press(self, event):
        self.numpad[12].setStyleSheet("background-color: rgb(47, 0, 0);\ncolor: rgb(50, 50, 50);")
    def num12release(self,event):
        self.numpad[12].setStyleSheet(self.numpadEnterDefaultStyleSheet)
        self.controlStack.setCurrentIndex(1)
        # WIP




app = QtWidgets.QApplication(sys.argv)
window = Ui()

app.exec_()
