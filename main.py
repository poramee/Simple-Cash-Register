from PyQt5 import QtTest, QtWidgets, uic
from PyQt5.QtCore import QEasingCurve, QPropertyAnimation, QRect
from datetime import datetime
import sys
import csv
import json
import os
from PyQt5.QtWidgets import QAbstractItemView, QGraphicsDropShadowEffect, QGraphicsOpacityEffect, QTableWidgetItem
from PyQt5.QtGui import QColor
from shutil import copyfile

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
        self.bncnt20 = self.findChild(QtWidgets.QLabel, 'bncnt20')
        self.bncnt50 = self.findChild(QtWidgets.QLabel, 'bncnt50')
        self.bncnt100 = self.findChild(QtWidgets.QLabel, 'bncnt100')
        self.bncnt500 = self.findChild(QtWidgets.QLabel, 'bncnt500')
        self.bncnt1000 = self.findChild(QtWidgets.QLabel, 'bncnt1000')
        self.ccnt1 = self.findChild(QtWidgets.QLabel, 'ccnt1')
        self.ccnt2 = self.findChild(QtWidgets.QLabel, 'ccnt2')
        self.ccnt5 = self.findChild(QtWidgets.QLabel, 'ccnt5')
        self.ccnt10 = self.findChild(QtWidgets.QLabel, 'ccnt10')
        self.receiveCnt = self.findChild(QtWidgets.QLabel, 'receiveCnt')
        self.changeCnt = self.findChild(QtWidgets.QLabel, 'changeCnt')
        self.cancelbn_cash = self.findChild(QtWidgets.QLabel, 'cancelbn_cash')
        self.finishbn_cash = self.findChild(QtWidgets.QLabel, 'finishbn_cash')

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

        self.bncnt20.mousePressEvent = self.bncnt20press
        self.bncnt50.mousePressEvent = self.bncnt50press
        self.bncnt100.mousePressEvent = self.bncnt100press
        self.bncnt500.mousePressEvent = self.bncnt500press
        self.bncnt1000.mousePressEvent = self.bncnt1000press
        self.ccnt1.mousePressEvent = self.ccnt1press
        self.ccnt2.mousePressEvent = self.ccnt2press
        self.ccnt5.mousePressEvent = self.ccnt5press
        self.ccnt10.mousePressEvent = self.ccnt10press

        self.cancelbn_cash.mousePressEvent = self.cancelbn_cashpress
        self.cancelbn_cash.mouseReleaseEvent = self.cancelbn_cashrelease
        self.finishbn_cash.mousePressEvent = self.finishbn_cashpress
        self.finishbn_cash.mouseReleaseEvent = self.finishbn_cashrelease

        # controlStack card page init.
        self.receiveCnt_card = self.findChild(QtWidgets.QLabel, 'receiveCnt_card')
        self.cancelbn_card = self.findChild(QtWidgets.QLabel, 'cancelbn_card')
        self.finishbn_card = self.findChild(QtWidgets.QLabel, 'finishbn_card')

        self.cancelbn_card.mousePressEvent = self.cancelbn_cardpress
        self.cancelbn_card.mouseReleaseEvent = self.cancelbn_cardrelease
        self.finishbn_card.mousePressEvent = self.finishbn_cardpress
        self.finishbn_card.mouseReleaseEvent = self.finishbn_cardrelease

        # controlStack others page init.
        self.receiveCnt_others = self.findChild(QtWidgets.QLabel, 'receiveCnt_others')
        self.cancelbn_others = self.findChild(QtWidgets.QLabel, 'cancelbn_others')
        self.finishbn_others = self.findChild(QtWidgets.QLabel, 'finishbn_others')

        self.cancelbn_others.mousePressEvent = self.cancelbn_otherspress
        self.cancelbn_others.mouseReleaseEvent = self.cancelbn_othersrelease
        self.finishbn_others.mousePressEvent = self.finishbn_otherspress
        self.finishbn_others.mouseReleaseEvent = self.finishbn_othersrelease

        # controlStack finish page init.
        self.gobackcount = self.findChild(QtWidgets.QLabel, 'gobackcount')

        #controlStack newSession page init.
        self.newsession = self.findChild(QtWidgets.QLabel, 'newsession')
        self.newsession.mousePressEvent = self.newsessionpress
        self.newsession.mouseReleaseEvent = self.newsessionrelease

        # pullDownBtn init.
        self.pullDownbtn = self.findChild(QtWidgets.QLabel, 'pullDownbtn')
        self.pullDownbtn.mousePressEvent = self.pullDownbtnpress
        self.pullDownbtn.mouseReleaseEvent = self.pullDownbtnrelease

        # mainCalculator init.
        self.mainCalculator = self.findChild(QtWidgets.QWidget, 'mainCalculator')

        # read settings
        self.readSettings()

        # set controlStack
        self.controlStack.setCurrentIndex(0)

        # check if the history is shown
        self.ispullDown = False

        # set drop shadow efect
        # self.dropShadowEffect = QGraphicsDropShadowEffect(self)
        # self.dropShadowEffect.setBlurRadius(5)
        # self.dropShadowEffect.setColor(QColor(0,0,0))
        # self.dropShadowEffect.setXOffset(-5)
        # self.setGraphicsEffect(self.dropShadowEffect)

        # history page init.
        self.historyTable = self.findChild(QtWidgets.QTableWidget, 'historyTable')
        self.noHistory = self.findChild(QtWidgets.QWidget, 'noHistory')
        self.totalThisSession = self.findChild(QtWidgets.QLabel, 'totalThisSession')
        self.trashStack = self.findChild(QtWidgets.QStackedWidget, 'trashStack')
        self.endsessionbtn = self.findChild(QtWidgets.QLabel, 'endsessionbtn')
        self.trashbtn = self.findChild(QtWidgets.QLabel, 'trashbtn')

        self.trashbtn.mousePressEvent = self.trashbtnpress
        self.trashbtn.mouseReleaseEvent = self.trashbtnrelease

        self.endsessionbtn.mousePressEvent = self.endsessionbtnpress
        self.endsessionbtn.mouseReleaseEvent = self.endsessionbtnrelease
        

        self.historyTable.itemSelectionChanged.connect(self.historyTablepress)

        self.rowsToDelete = []

        # show windows
        self.show()
        # historyTable init.

        # assign numpadgeometry value for animation
        self.numpadgeometry = []
        for i in range(0,13):
            self.numpadgeometry.append(self.numpad[i].geometry())

        # set controlStack to 'start a new session' page if a session wasn't found.
        if not os.path.exists(".current"):
            self.noHistory.show()
            self.historyTable.hide()
            self.controlStack.setCurrentIndex(6)
        else:
            self.loadHistory()
            self.getSessionTime()
            self.output.setText("0")
        
        # assign bn,c geometry for animation
        self.bn20geometry = self.bn20.geometry()
        self.bn50geometry = self.bn50.geometry()
        self.bn100geometry = self.bn100.geometry()
        self.bn500geometry = self.bn500.geometry()
        self.bn1000geometry = self.bn1000.geometry()
        self.c1geometry = self.c1.geometry()
        self.c2geometry = self.c2.geometry()
        self.c5geometry = self.c5.geometry()
        self.c10geometry = self.c10.geometry()

    def historyTablepress(self):
        select = self.historyTable.selectionModel()
        self.rowsToDelete = []
        if select.hasSelection():
            self.trashStack.setCurrentIndex(1)
            for row in select.selectedRows():
                self.rowsToDelete.append(row.row())
        else:
            self.trashStack.setCurrentIndex(0)
            self.rowsToDelete = []

    def loadHistory(self):
        file = open(".current/currentData.csv","r")
        reader = csv.reader(file,delimiter = ',')
        self.historyTable.setRowCount(0)
        self.historyTable.setColumnCount(5)
        rowCnt = 0
        total = 0
        for row in reader:
            if rowCnt <= 1:
                rowCnt += 1
                continue
            self.historyTable.insertRow(self.historyTable.rowCount())
            total += float(row[3])
            for i in range(5):
                self.historyTable.setItem(self.historyTable.rowCount() - 1,i,QTableWidgetItem(row[i]))
            rowCnt += 1
        if self.historyTable.rowCount() == 0:
            self.historyTable.hide()
            self.noHistory.show()
            self.totalThisSession.hide()
            self.trashStack.hide()
        else:
            self.historyTable.show()
            self.noHistory.hide()
            self.totalThisSession.setText("Total this session: " + str(total))
            self.totalThisSession.show()
            self.trashStack.show()
        file.close()
        self.historyTable = self.findChild(QtWidgets.QTableWidget, 'historyTable')
        self.historyTable.setHorizontalHeaderLabels(["Date","Time","Type","Total","Receive"])
        self.historyTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.historyTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.historyTable.setColumnWidth(0,170)
        self.historyTable.setColumnWidth(1,130)
        self.historyTable.setColumnWidth(2,130)
        self.historyTable.setColumnWidth(3,200)
        self.historyTable.setColumnWidth(4,200)
        self.historyTable.horizontalHeader().setStyleSheet("QHeaderView { font: 18pt \"Avenir Next\"; color: rgb(243, 243, 243); background-color: rgb(50, 50, 50);}")
        self.historyTable.verticalHeader().setStyleSheet("QHeaderView { font: 18pt \"Avenir Next\";}")

    def readSettings(self):
        if not os.path.exists("settings.json"):
            temp = open("settings.json","w")
            path = os.path.expanduser("~/Simple Cash Register/")
            print(path)
            data = {}
            data['settings'] = []
            data['settings'].append({
                'save_dir': path
            })
            json.dump(data,temp)
            temp.close()
        settings = open("settings.json","r")
        data = json.load(settings)
        self.settingsData = data['settings']
        if not os.path.exists(self.settingsData[0]['save_dir']):
            os.makedirs(self.settingsData[0]['save_dir'])

    def numpadPress(self,num):
        self.anim = QPropertyAnimation(self.numpad[num],b"geometry")
        self.anim.setStartValue(QRect(self.numpad[num].geometry()))
        self.anim.setEndValue(QRect(self.numpadgeometry[num].adjusted(5,5,-5,-5)))
        self.anim.setDuration(1)
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

        self.bncnt20.setText("0")
        self.bncnt50.setText("0")
        self.bncnt100.setText("0")
        self.bncnt500.setText("0")
        self.bncnt1000.setText("0")
        self.ccnt1.setText("0")
        self.ccnt2.setText("0")
        self.ccnt5.setText("0")
        self.ccnt10.setText("0")
        self.receiveCnt.setText("0")
        self.changeCnt.setText("0")

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
        self.anim.setDuration(1)
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
        self.anim.setDuration(1)
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
        self.anim.setDuration(1)
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
        self.receiveAmtUpdate()
    
    def cardbnpress(self,event):
        self.setBtnPress(self.cardbn)
    def cardbnrelease(self,event):
        self.setBtnRelease(self.cardbn)
        self.controlStack.setCurrentIndex(3)
        self.receiveCnt_card.setText(self.output.text())
    
    def othersbnpress(self,event):
        self.setBtnPress(self.othersbn)
    def othersbnrelease(self,event):
        self.setBtnRelease(self.othersbn)
        self.controlStack.setCurrentIndex(4)
        self.receiveCnt_others.setText(self.output.text())

    def cancelbnpress(self,event):
        self.cancelbn.setStyleSheet("color: rgb(255, 26, 9);background-color: rgba(255, 0, 15, 150);")
    def cancelbnrelease(self,event):
        self.cancelbn.setStyleSheet("color: rgb(255, 26, 9);background-color: rgba(255, 0, 15, 0);")
        self.cancelAndGoBack()
    
    # controlStack #3 - CASH
    
    def bn20press(self,event):
        self.anim = QPropertyAnimation(self.bn20,b"geometry")
        self.anim.setStartValue(QRect(self.bn20.geometry()))
        self.anim.setEndValue(QRect(self.bn20geometry.adjusted(5,5,-5,-5)))
        self.anim.setDuration(0)
        self.anim.start()

    def bn20release(self,event):
        self.anim = QPropertyAnimation(self.bn20,b"geometry")
        self.anim.setStartValue(QRect(self.bn20.geometry()))
        self.anim.setEndValue(QRect(self.bn20geometry))
        self.anim.setDuration(100)
        self.anim.start()
        self.bncnt20.setText(str(int(self.bncnt20.text()) + 1))
        self.receiveAmtUpdate()

    def bncnt20press(self,event):
        self.bncnt20.setText("0")
        self.receiveAmtUpdate()

    def bn50press(self,event):
        self.anim = QPropertyAnimation(self.bn50,b"geometry")
        self.anim.setStartValue(QRect(self.bn50.geometry()))
        self.anim.setEndValue(QRect(self.bn50geometry.adjusted(5,5,-5,-5)))
        self.anim.setDuration(0)
        self.anim.start()
    def bn50release(self,event):
        self.anim = QPropertyAnimation(self.bn50,b"geometry")
        self.anim.setStartValue(QRect(self.bn50.geometry()))
        self.anim.setEndValue(QRect(self.bn50geometry))
        self.anim.setDuration(100)
        self.anim.start()
        self.bncnt50.setText(str(int(self.bncnt50.text()) + 1))
        self.receiveAmtUpdate()

    def bncnt50press(self,event):
        self.bncnt50.setText("0")
        self.receiveAmtUpdate()
    
    def bn100press(self,event):
        self.anim = QPropertyAnimation(self.bn100,b"geometry")
        self.anim.setStartValue(QRect(self.bn100.geometry()))
        self.anim.setEndValue(QRect(self.bn100geometry.adjusted(5,5,-5,-5)))
        self.anim.setDuration(0)
        self.anim.start()
    def bn100release(self,event):
        self.anim = QPropertyAnimation(self.bn100,b"geometry")
        self.anim.setStartValue(QRect(self.bn100.geometry()))
        self.anim.setEndValue(QRect(self.bn100geometry))
        self.anim.setDuration(100)
        self.anim.start()
        self.bncnt100.setText(str(int(self.bncnt100.text()) + 1))
        self.receiveAmtUpdate()

    def bncnt100press(self,event):
        self.bncnt100.setText("0")
        self.receiveAmtUpdate()
    
    def bn500press(self,event):
        self.anim = QPropertyAnimation(self.bn500,b"geometry")
        self.anim.setStartValue(QRect(self.bn500.geometry()))
        self.anim.setEndValue(QRect(self.bn500geometry.adjusted(5,5,-5,-5)))
        self.anim.setDuration(0)
        self.anim.start()
    def bn500release(self,event):
        self.anim = QPropertyAnimation(self.bn500,b"geometry")
        self.anim.setStartValue(QRect(self.bn500.geometry()))
        self.anim.setEndValue(QRect(self.bn500geometry))
        self.anim.setDuration(100)
        self.anim.start()
        self.bncnt500.setText(str(int(self.bncnt500.text()) + 1))
        self.receiveAmtUpdate()

    def bncnt500press(self,event):
        self.bncnt500.setText("0")
        self.receiveAmtUpdate()

    def bn1000press(self,event):
        self.anim = QPropertyAnimation(self.bn1000,b"geometry")
        self.anim.setStartValue(QRect(self.bn1000.geometry()))
        self.anim.setEndValue(QRect(self.bn1000geometry.adjusted(5,5,-5,-5)))
        self.anim.setDuration(0)
        self.anim.start()
    def bn1000release(self,event):
        self.anim = QPropertyAnimation(self.bn1000,b"geometry")
        self.anim.setStartValue(QRect(self.bn1000.geometry()))
        self.anim.setEndValue(QRect(self.bn1000geometry))
        self.anim.setDuration(100)
        self.anim.start()
        self.bncnt1000.setText(str(int(self.bncnt1000.text()) + 1))
        self.receiveAmtUpdate()

    def bncnt1000press(self,event):
        self.bncnt1000.setText("0")
        self.receiveAmtUpdate()

    def c1press(self,event):
        self.anim = QPropertyAnimation(self.c1,b"geometry")
        self.anim.setStartValue(QRect(self.c1.geometry()))
        self.anim.setEndValue(QRect(self.c1geometry.adjusted(5,5,-5,-5)))
        self.anim.setDuration(0)
        self.anim.start()
    def c1release(self,event):
        self.anim = QPropertyAnimation(self.c1,b"geometry")
        self.anim.setStartValue(QRect(self.c1.geometry()))
        self.anim.setEndValue(QRect(self.c1geometry))
        self.anim.setDuration(100)
        self.anim.start()
        self.ccnt1.setText(str(int(self.ccnt1.text()) + 1))
        self.receiveAmtUpdate()

    def ccnt1press(self,event):
        self.ccnt1.setText("0")
        self.receiveAmtUpdate()

    def c2press(self,event):
        self.anim = QPropertyAnimation(self.c2,b"geometry")
        self.anim.setStartValue(QRect(self.c2.geometry()))
        self.anim.setEndValue(QRect(self.c2geometry.adjusted(5,5,-5,-5)))
        self.anim.setDuration(0)
        self.anim.start()
    def c2release(self,event):
        self.anim = QPropertyAnimation(self.c2,b"geometry")
        self.anim.setStartValue(QRect(self.c2.geometry()))
        self.anim.setEndValue(QRect(self.c2geometry))
        self.anim.setDuration(100)
        self.anim.start()
        self.ccnt2.setText(str(int(self.ccnt2.text()) + 1))
        self.receiveAmtUpdate()

    def ccnt2press(self,event):
        self.ccnt2.setText("0")
        self.receiveAmtUpdate()

    def c5press(self,event):
        self.anim = QPropertyAnimation(self.c5,b"geometry")
        self.anim.setStartValue(QRect(self.c5.geometry()))
        self.anim.setEndValue(QRect(self.c5geometry.adjusted(5,5,-5,-5)))
        self.anim.setDuration(0)
        self.anim.start()
    def c5release(self,event):
        self.anim = QPropertyAnimation(self.c5,b"geometry")
        self.anim.setStartValue(QRect(self.c5.geometry()))
        self.anim.setEndValue(QRect(self.c5geometry))
        self.anim.setDuration(100)
        self.anim.start()
        self.ccnt5.setText(str(int(self.ccnt5.text()) + 1))
        self.receiveAmtUpdate()

    def ccnt5press(self,event):
        self.ccnt5.setText("0")
        self.receiveAmtUpdate()

    def c10press(self,event):
        self.anim = QPropertyAnimation(self.c10,b"geometry")
        self.anim.setStartValue(QRect(self.c10.geometry()))
        self.anim.setEndValue(QRect(self.c10geometry.adjusted(5,5,-5,-5)))
        self.anim.setDuration(0)
        self.anim.start()
        
    def c10release(self,event):
        self.anim = QPropertyAnimation(self.c10,b"geometry")
        self.anim.setStartValue(QRect(self.c10.geometry()))
        self.anim.setEndValue(QRect(self.c10geometry))
        self.anim.setDuration(100)
        self.anim.start()
        self.ccnt10.setText(str(int(self.ccnt10.text()) + 1))
        self.receiveAmtUpdate()


    def ccnt10press(self,event):
        self.ccnt10.setText("0")
        self.receiveAmtUpdate()

    def cancelbn_cashpress(self,event):
        self.cancelbn_cash.setStyleSheet("color: rgb(255, 26, 9);background-color: rgba(255, 0, 15, 150);")
    def cancelbn_cashrelease(self,event):
        self.cancelbn_cash.setStyleSheet("color: rgb(255, 26, 9);background-color: rgba(255, 0, 15, 0);")
        self.cancelAndGoBack()

    def finishbn_cashpress(self,event):
        self.finishbn_cash.setStyleSheet("color: rgb(80,216,144);background-color:rgba(0, 255, 0, 150);")
    def finishbn_cashrelease(self,event):
        self.finishbn_cash.setStyleSheet("color: rgb(80,216,144);background-color:rgba(0, 255, 0, 0);")
        self.save('Cash',float(self.output.text()),float(self.receiveCnt.text()))
        self.goToFinishPage()

    def cancelbn_cardpress(self,event):
        self.cancelbn_card.setStyleSheet("color: rgb(255, 26, 9);background-color: rgba(255, 0, 15, 150);")
    def cancelbn_cardrelease(self,event):
        self.cancelbn_card.setStyleSheet("color: rgb(255, 26, 9);background-color: rgba(255, 0, 15, 0);")
        self.cancelAndGoBack()
    def finishbn_cardpress(self,event):
        self.finishbn_card.setStyleSheet("color: rgb(80,216,144);background-color:rgba(0, 255, 0, 150);")
    def finishbn_cardrelease(self,event):
        self.finishbn_card.setStyleSheet("color: rgb(80,216,144);background-color:rgba(0, 255, 0, 0);")
        self.save('Credit Card',float(self.output.text()),float(self.receiveCnt_card.text()))
        self.goToFinishPage()

    def cancelbn_otherspress(self,event):
        self.cancelbn_others.setStyleSheet("color: rgb(255, 26, 9);background-color: rgba(255, 0, 15, 150);")
    def cancelbn_othersrelease(self,event):
        self.cancelbn_others.setStyleSheet("color: rgb(255, 26, 9);background-color: rgba(255, 0, 15, 0);")
        self.cancelAndGoBack()
    def finishbn_otherspress(self,event):
        self.finishbn_others.setStyleSheet("color: rgb(80,216,144);background-color:rgba(0, 255, 0, 150);")
    def finishbn_othersrelease(self,event):
        self.finishbn_others.setStyleSheet("color: rgb(80,216,144);background-color:rgba(0, 255, 0, 0);")
        self.save('Others',float(self.output.text()),float(self.receiveCnt_others.text()))
        self.goToFinishPage()

    def newsessionpress(self,event):
        self.newsession.setStyleSheet("color: rgb(54, 200, 255);background-color: rgba(0, 139, 255, 150);")
    def newsessionrelease(self,event):
        self.newsession.setStyleSheet("color: rgb(54, 200, 255);background-color: rgba(0, 139, 255, 0);")
        self.createSessionFile()
        self.output.setText("0")
        self.controlStack.setCurrentIndex(0)

    def createSessionFile(self):
        os.makedirs(".current")
        file = open(".current/currentData.csv","a")
        writer = csv.writer(file,delimiter = ',')
        dateTimeObj = datetime.now()
        timestampDate = dateTimeObj.strftime("%d-%b-%Y")
        timestampTime = dateTimeObj.strftime("%H:%M:%S")
        writer.writerow(['Date','Time','Type','Total','Receive'])
        writer.writerow([timestampDate,timestampTime,'sessionTimeStamp','0','0'])
        self.sessionTimeLabel.setText("Session: " + timestampDate + " at " + timestampTime)
        file.close()

    def getSessionTime(self):
        file = open(".current/currentData.csv","r")
        reader = csv.reader(file,delimiter = ',')
        rowCnt = 0
        for row in reader:
            if rowCnt == 1:
                self.sessionTimeLabel.setText("Session: " + row[0] + " at " + row[1])
                break
            rowCnt += 1
        file.close()

    def save(self,typeName,totalAmt,receiveAmt):
        file = open(".current/currentData.csv","a")
        writer = csv.writer(file,delimiter = ',')
        dateTimeObj = datetime.now()
        timestampDate = dateTimeObj.strftime("%d-%b-%Y")
        timestampTime = dateTimeObj.strftime("%H:%M:%S")
        writer.writerow([timestampDate,timestampTime,typeName,totalAmt,receiveAmt])
        file.close()

    def goToFinishPage(self):
        self.controlStack.setCurrentIndex(5)
        self.output.setStyleSheet("color: rgb(255, 255, 255); background-color:rgba(80,216,144, 255);")
        self.gobackcount.setText("GOING BACK IN 2 SECONDS")
        QtTest.QTest.qWait(1000)
        self.gobackcount.setText("GOING BACK IN 1 SECOND")
        QtTest.QTest.qWait(1000)
        self.output.setText("0")
        self.cancelAndGoBack()

    def receiveAmtUpdate(self):
        cnt = 0
        cnt += int(self.bncnt20.text()) * 20
        cnt += int(self.bncnt50.text()) * 50
        cnt += int(self.bncnt100.text()) * 100
        cnt += int(self.bncnt500.text()) * 500
        cnt += int(self.bncnt1000.text()) * 1000
        cnt += int(self.ccnt1.text()) * 1
        cnt += int(self.ccnt2.text()) * 2
        cnt += int(self.ccnt5.text()) * 5
        cnt += int(self.ccnt10.text()) * 10
        self.receiveCnt.setText(str(cnt))
        self.changeCnt.setText(str(cnt - float(self.output.text())))
    
    def endsessionbtnpress(self,event):
        self.setBtnPress(self.endsessionbtn)
    def endsessionbtnrelease(self,event):
        self.setBtnRelease(self.endsessionbtn)
        file = open(".current/currentData.csv","r")
        reader = csv.reader(file,delimiter = ',')
        total = 0
        rowCount = 0
        sessionDate = ""
        sessionTime = ""
        for row in reader:
            if rowCount == 1:
                sessionDate = row[0]
                sessionTime = row[1]
            if rowCount <= 1:
                rowCount += 1
                continue
            total += float(row[3])
            rowCount += 1
        file.close()
        i = 0
        newSessionTime = ""
        for i in sessionTime:
            if i == ":":
                newSessionTime += "_"
            else:
                newSessionTime += i
        self.save('TOTAL',str(total),"-")
        copyfile(".current/currentData.csv", str(self.settingsData[0]['save_dir']) + sessionDate + " " + newSessionTime + ".csv")
        os.remove(".current/currentData.csv")
        os.rmdir(".current")
        self.resetAll()
        self.pullDownbtnrelease(None)
        
    def resetAll(self):
        self.noHistory.show()
        self.historyTable.hide()
        self.cancelAndGoBack()
        self.controlStack.setCurrentIndex(6)
        self.output.setText("")
        self.sessionTimeLabel.setText("")
        self.totalThisSession.hide()
        self.trashStack.hide()
        self.endsessionbtn.hide()

    def pullDownbtnpress(self,event):
        pass
    def pullDownbtnrelease(self,event):
        if not os.path.exists(".current"):
            self.resetAll()
        else:
            self.trashStack.setCurrentIndex(0)
            self.endsessionbtn.show()
            self.trashStack.show()
            self.totalThisSession.show()
            self.loadHistory()
        
        self.anim2 = QPropertyAnimation(self.mainCalculator,b"geometry")
        self.anim2.setStartValue(QRect(self.mainCalculator.geometry()))
        if not self.ispullDown:
            self.anim2.setEndValue(QRect(0,700,1000,800))
        else:
            self.anim2.setEndValue(QRect(0,0,1000,800))
        self.anim2.setDuration(700)
        self.anim2.setEasingCurve(QEasingCurve.OutQuart)
        self.anim2.start()
        self.ispullDown = not self.ispullDown

    def deleteHistoryTable(self):
        lines = list()
        rowCnt = -2
        with open(".current/currentData.csv","r") as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if rowCnt not in self.rowsToDelete:
                    lines.append(row)
                rowCnt += 1
        with open(".current/currentData.csv","w") as writeFile:
            writer = csv.writer(writeFile)
            writer.writerows(lines)
        self.loadHistory()
        
    def trashbtnpress(self,event):
        self.trashbtn.setGeometry(QRect(12,2,23,23))
    def trashbtnrelease(self,event):
        self.anim = QPropertyAnimation(self.trashbtn,b"geometry")
        self.anim.setStartValue(QRect(self.trashbtn.geometry()))
        self.anim.setEndValue(QRect(10,0,30,30))
        self.anim.setDuration(100)
        self.anim.start()
        self.deleteHistoryTable()


app = QtWidgets.QApplication(sys.argv)
window = Ui()

app.exec_()
