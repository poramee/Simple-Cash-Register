from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import QRect, QPropertyAnimation
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
        self.output.setMargin(20)

        # totalLabel init.
        self.totalLabel = self.findChild(QtWidgets.QLabel, 'totalLabel')
        self.totalLabel.hide()

        # controlStack 2nd page init
        self.cashbn = self.findChild(QtWidgets.QLabel, 'cashbn')
        self.cardbn = self.findChild(QtWidgets.QLabel, 'cardbn')
        self.othersbn = self.findChild(QtWidgets.QLabel, 'othersbn')
        self.cancelbn = self.findChild(QtWidgets.QLabel, 'cancelbn')

        self.cashbn.mousePressEvent = self.cashbnpress
        self.cashbn.mouseReleaseEvent = self.cashbnrelease
        self.cardbn.mousePressEvent = self.cardbnpress
        self.cardbn.mouseReleaseEvent = self.cardbnrelease
        self.othersbn.mousePressEvent = self.othersbnpress
        self.othersbn.mouseReleaseEvent = self.othersbnrelease
        self.cancelbn.mousePressEvent = self.cancelbnpress
        self.cancelbn.mouseReleaseEvent = self.cancelbnrelease

        # controlStack 3rd page init
        self.bn20 = self.findChild(QtWidgets.QLabel, 'bn20')
        self.bn50 = self.findChild(QtWidgets.QLabel, 'bn50')
        self.bn100 = self.findChild(QtWidgets.QLabel, 'bn100')
        self.bn500 = self.findChild(QtWidgets.QLabel, 'bn500')
        self.bn1000 = self.findChild(QtWidgets.QLabel, 'bn1000')
        self.c1 = self.findChild(QtWidgets.QLabel, 'c1')
        self.c2 = self.findChild(QtWidgets.QLabel, 'c2')
        self.c5 = self.findChild(QtWidgets.QLabel, 'c5')
        self.c10 = self.findChild(QtWidgets.QLabel, 'c10')

        self.bn20.mousePressEvent = self.bn20press
        self.bn20.mouseReleaseEvent = self.bn20release
        self.bn50.mousePressEvent = self.bn50press
        self.bn50.mouseReleaseEvent = self.bn50release
        self.bn100.mousePressEvent = self.bn100press
        self.bn100.mouseReleaseEvent = self.bn100release
        self.bn500.mousePressEvent = self.bn500press
        self.bn500.mouseReleaseEvent = self.bn500release
        self.bn1000.mousePressEvent = self.bn1000press
        self.bn1000.mouseReleaseEvent = self.bn1000release
        self.c1.mousePressEvent = self.c1press
        self.c1.mouseReleaseEvent = self.c1release
        self.c2.mousePressEvent = self.c2press
        self.c2.mouseReleaseEvent = self.c2release
        self.c5.mousePressEvent = self.c5press
        self.c5.mouseReleaseEvent = self.c5release
        self.c10.mousePressEvent = self.c10press
        self.c10.mouseReleaseEvent = self.c10release
        # set controlStack
        self.controlStack.setCurrentIndex(0)

        # show windows
        self.show()

        # assign numpadgeometry value for animation
        self.numpadgeometry = []
        for i in range(0,13):
            self.numpadgeometry.append(self.numpad[i].geometry())
    
    
    
    def numpadPress(self,num):
        self.anim = QPropertyAnimation(self.numpad[num],b"geometry")
        self.anim.setStartValue(QRect(self.numpad[num].geometry()))
        self.anim.setEndValue(QRect(self.numpadgeometry[num].adjusted(5,5,-5,-5)))
        self.anim.setDuration(50)
        self.anim.start()
        self.numpad[num].setStyleSheet("background-color: rgb(200, 200, 200);\ncolor: rgb(0, 0, 0);")
    def numpadRelease(self,num):
        self.anim = QPropertyAnimation(self.numpad[num],b"geometry")
        self.anim.setStartValue(QRect(self.numpad[num].geometry()))
        self.anim.setEndValue(QRect(self.numpadgeometry[num]))
        self.anim.setDuration(100)
        self.anim.start()

        self.numpad[num].setStyleSheet(self.numpadDefaultStyleSheet)
        if self.output.text() == "0":
            self.output.setText(str(num))
        elif len(self.output.text()) < 15: # check if textbox is available for another input(15 char. max.)
            self.output.setText(self.output.text() + str(num))

    def cancelAndGoBack(self):
        self.totalLabel.hide()
        self.output.setStyleSheet("color: rgb(255, 255, 255);")
        self.controlStack.setCurrentIndex(0)

    def num0press(self, event):
        self.numpadPress(0)
    def num0release(self,event):
        self.anim = QPropertyAnimation(self.numpad[0],b"geometry")
        self.anim.setStartValue(QRect(self.numpad[0].geometry()))
        self.anim.setEndValue(QRect(self.numpadgeometry[0]))
        self.anim.setDuration(100)
        self.anim.start()
        self.numpad[0].setStyleSheet(self.numpadDefaultStyleSheet)
        if self.output.text() != "0" and len(self.output.text()) < 15: # check if textbox is available for another input(15 char. max.)
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
        self.anim = QPropertyAnimation(self.numpad[10],b"geometry")
        self.anim.setStartValue(QRect(self.numpad[10].geometry()))
        self.anim.setEndValue(QRect(self.numpadgeometry[10]).adjusted(5,5,-5,-5))
        self.anim.setDuration(50)
        self.anim.start()
        self.numpad[10].setStyleSheet("background-color: rgb(200, 200, 200);\ncolor: rgb(0, 0, 0);")
    def num10release(self,event):
        self.anim = QPropertyAnimation(self.numpad[10],b"geometry")
        self.anim.setStartValue(QRect(self.numpad[10].geometry()))
        self.anim.setEndValue(QRect(self.numpadgeometry[10]))
        self.anim.setDuration(100)
        self.anim.start()
        self.numpad[10].setStyleSheet(self.numpadDefaultStyleSheet)
        if "." not in self.output.text() and len(self.output.text()) < 14: # check if textbox is available for another input(15 char. max.)
            self.output.setText(self.output.text() + ".")
    # 'clear'
    def num11press(self, event):
        self.anim = QPropertyAnimation(self.numpad[11],b"geometry")
        self.anim.setStartValue(QRect(self.numpad[11].geometry()))
        self.anim.setEndValue(QRect(self.numpadgeometry[11]).adjusted(5,5,-5,-5))
        self.anim.setDuration(50)
        self.anim.start()
        self.numpad[11].setStyleSheet("background-color: rgb(200, 0, 0);\ncolor: rgb(200, 200, 200);")
    def num11release(self,event):
        self.anim = QPropertyAnimation(self.numpad[11],b"geometry")
        self.anim.setStartValue(QRect(self.numpad[11].geometry()))
        self.anim.setEndValue(QRect(self.numpadgeometry[11]))
        self.anim.setDuration(100)
        self.anim.start()
        self.numpad[11].setStyleSheet(self.numpadClearDefaultStyleSheet)
        self.output.setText("0")
    # 'enter'
    def num12press(self, event):
        self.anim = QPropertyAnimation(self.numpad[12],b"geometry")
        self.anim.setStartValue(QRect(self.numpad[12].geometry()))
        self.anim.setEndValue(QRect(self.numpadgeometry[12]).adjusted(5,5,-5,-5))
        self.anim.setDuration(50)
        self.anim.start()
        self.numpad[12].setStyleSheet("background-color: rgb(197, 60, 0);\ncolor: rgb(200, 200, 200);")
    def num12release(self,event):
        self.anim = QPropertyAnimation(self.numpad[12],b"geometry")
        self.anim.setStartValue(QRect(self.numpad[12].geometry()))
        self.anim.setEndValue(QRect(self.numpadgeometry[12]))
        self.anim.setDuration(100)
        self.anim.start()
        self.numpad[12].setStyleSheet(self.numpadEnterDefaultStyleSheet)
        
        self.totalLabel.show()
        self.output.setStyleSheet(self.numpadEnterDefaultStyleSheet)
        # change controlStack Page
        self.controlStack.setCurrentIndex(1)
    
    # controlStack p2
    def setBtnPress(self,label):
        label.setStyleSheet("color: rgb(54, 200, 255);background-color: rgba(0, 139, 255, 150);")
    def setBtnRelease(self,label):
        label.setStyleSheet("color: rgb(54, 200, 255);background-color: rgba(0, 139, 255, 0);")

    def cashbnpress(self,event):
        self.setBtnPress(self.cashbn)
    def cashbnrelease(self,event):
        self.setBtnRelease(self.cashbn)
        self.controlStack.setCurrentIndex(2)
    
    def cardbnpress(self,event):
        self.setBtnPress(self.cardbn)
    def cardbnrelease(self,event):
        self.setBtnRelease(self.cardbn)
    
    def othersbnpress(self,event):
        self.setBtnPress(self.othersbn)
    def othersbnrelease(self,event):
        self.setBtnRelease(self.othersbn)

    def cancelbnpress(self,event):
        self.cancelbn.setStyleSheet("color: rgb(255, 26, 9);background-color: rgba(255, 0, 15, 150);")
    def cancelbnrelease(self,event):
        self.cancelbn.setStyleSheet("color: rgb(255, 26, 9);background-color: rgba(255, 0, 15, 0);")
        self.cancelAndGoBack()
    
    def bn20press(self,event):
        print("WIP")
    def bn20release(self,event):
        print("WIP")

    def bn50press(self,event):
        print("WIP")
    def bn50release(self,event):
        print("WIP")
    
    def bn100press(self,event):
        print("WIP")
    def bn100release(self,event):
        print("WIP")
    
    def bn500press(self,event):
        print("WIP")
    def bn500release(self,event):
        print("WIP")

    def bn1000press(self,event):
        print("WIP")
    def bn1000release(self,event):
        print("WIP")

    def c1press(self,event):
        print("WIP")
    def c1release(self,event):
        print("WIP")

    def c2press(self,event):
        print("WIP")
    def c2release(self,event):
        print("WIP")

    def c5press(self,event):
        print("WIP")
    def c5release(self,event):
        print("WIP")

    def c10press(self,event):
        print("WIP")
    def c10release(self,event):
        print("WIP")



app = QtWidgets.QApplication(sys.argv)
window = Ui()

app.exec_()
