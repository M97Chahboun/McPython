import sys
import ctypes
from PyQt5.QtCore import (pyqtSignal, QEasingCurve, QParallelAnimationGroup, QPointF, QPropertyAnimation, QState, QFile,
                          QStringListModel, QTimer, QStateMachine, QPoint, QRect, QSize, Qt, pyqtSlot, QProcess,
                          QIODevice, QFile,
                          QStringListModel)
from PyQt5.QtGui import QColor, QCursor, QCursor, QFont, QIcon, QImage, QKeySequence, QKeySequence, QPixmap, QRegion, QTextCharFormat, QTextCursor, QTextCursor, QTextCursor, QTextDocument
from PyQt5.QtWidgets import QAction, QApplication, QApplication, QColorDialog, QComboBox, QCompleter, QCompleter, QDialog, QDoubleSpinBox, QFileDialog, QGraphicsDropShadowEffect, QGroupBox, QLabel, QMainWindow, QMessageBox, QPlainTextEdit, QProgressBar, QPushButton, QSlider, QTabWidget, QTextEdit, QWidget
from threading import Thread
from pyautogui import press, hotkey
from functools import partial



class StartTuto(QDialog):
    def __init__(self):
        super(StartTuto, self).__init__()
        QDialog.__init__(self)
        self.Next = 0
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setWindowTitle("لنتعلم معا")
        self.font = QFont('abdo salem')
        self.font.setPointSize(20)
        self.font.setBold(True)
        self.ex = QPushButton(self)
        self.ex.setFont(self.font)
        self.ex.setGeometry(400 + 80, 450, 150, 50)
        self.ex.setText('خروج')
        self.ex.setStyleSheet(
            "QPushButton:hover{background-color:rgb(241, 90, 36);border:5px solid rgb(0, 97, 157);}\n"
            "QPushButton{color:white;background-color: rgb(50, 50, 50);border:5px solid rgb(255, 255, 255);}QPushButton:pressed{color:white;background-color: rgb(50, 50, 50);border:5px solid rgb(255, 255, 255);}\n"
            "")
        self.ex.clicked.connect(self.Exit)
        self.hm = QPushButton(self)
        self.hm.setFont(self.font)
        self.hm.setGeometry(200 + 80, 450, 150, 50)
        self.hm.setText('الرئيسية')
        self.hm.setStyleSheet(
            "QPushButton:hover{background-color:rgb(241, 90, 36);border:5px solid rgb(0, 97, 157);}\n"
            "QPushButton{color:white;background-color: rgb(50, 50, 50);border:5px solid rgb(255, 255, 255);}QPushButton:pressed{color:white;background-color: rgb(50, 50, 50);border:5px solid rgb(255, 255, 255);}\n"
            "")
        self.hm.clicked.connect(self.home)
        self.resize(925, 500)
        self.Ind = ['data', 'if', 'for', 'while', 'def',
                    'class', 'oop', 'exp', 'prj2', 'prj3', 'st']
        self.names = {
            'home': ['المتغير و\n أنواع البيانات', 'الجملة الشرطية\nIF', 'حلقة التقسيم\nFOR', 'حلقة مادام\nWHILE',
                     'الدالة\nDEF', 'الفئة\nClass', 'البرمجة كائنية\nالتوجه OOP', 'العبارات',
                     'المشروع الاول\nRANGE', 'المشروع الثاني\nStr', 'ابدء'],
            'data': ['المتغير', 'الأحرف ', 'الأرقام ', 'القائمة', 'القاموس', 'الخطأ\nالصحيح', 'دوال \nانواع البيانات',
                     'الأمثلة'],
            'if': ['الجملة الشرطية\nIF', 'ادوات المقارنة', 'استعمالات\n ELIF و ELSE'],
            'for': ['فكرة \nFOR', 'استعمالات \nFOR', 'امثلة'], 'while': ['فكرة \nWHILE', 'استعمالات \nWHILE', 'امثلة'],

            'def': ['دالة بسيطة', 'arg\nدالة مع', '*arg\nدالة مع', 'دالة مع\n**kwargs'],
            'class': ['فئة بسيطة\n مع متغير', 'فئة بسيطة\n مع دالة'],
            'oop': ['البناء\n__init__', 'خاصية الاراثة', 'دالة\nsuper()'],
            'exp': ['عبارة\nreturn', 'عبارة\nassert', 'عبارة\nyield'],
            'prj2': ['المشروع'], 'prj3': ['محاكات\nCount', 'محاكات\nFind', 'تطوير\nFind'], 'st': 'exit'}
        self.Home()

    def Home(self):
        self.items = []
        for i in range(len(self.names['home'])):
            item = QPushButton(self)
            item.setText(self.names['home'][i])
            item.setGeometry(395, 350, 120, 80)
            item.setStyleSheet(
                "QPushButton:hover{background-color:rgb(241, 90, 36);border:5px solid rgb(0, 97, 157);}\n"
                "QPushButton{color:white;background-color: rgb(50, 50, 50);border:5px solid rgb(255, 255, 255);}QPushButton:pressed{color:white;background-color: rgb(50, 50, 50);border:5px solid rgb(255, 255, 255);}\n"
                "")
            self.font.setPointSize(15)
            item.setFont(self.font)
            self.items.append(item)
            exec("""item.clicked.connect(partial(self.IND,i=%i))""" % (i))

        self.rootState = QState()
        self.tiledState = QState(self.rootState)
        self.centeredState = QState(self.rootState)
        for i, item in enumerate(self.items):
            self.tiledState.assignProperty(item, 'pos',
                                           QPointF(((i % 6) * 5.3) * 30,
                                                   ((i // 6) * 5.3) * 30))

            self.centeredState.assignProperty(item, 'pos', QPointF())

        self.states = QStateMachine()
        self.states.addState(self.rootState)
        self.states.setInitialState(self.rootState)
        self.rootState.setInitialState(self.centeredState)
        self.group = QParallelAnimationGroup()
        for i, item in enumerate(self.items):
            anim = QPropertyAnimation(item, b'pos')
            anim.setStartValue(QPoint(400, 300))
            anim.setDuration(750 + i * 25)
            anim.setEasingCurve(QEasingCurve.InOutBack)
            self.group.addAnimation(anim)

        for u in self.items:
            trans = self.rootState.addTransition(u.clicked, self.tiledState)
            trans.addAnimation(self.group)
            self.states.start()

    def Exit(self):
        open('Files/choice', 'w').write('exit')
        self.close()

    def home(self):
        open('Files/choice', 'w').write('home')
        self.close()

    def IND(self, i):
        open('Files/choice', 'a').write(str(i))
        if self.Next != 2:
            self.Next += 1
            if self.names[self.Ind[i]] != 'exit':
                a = self.names[self.Ind[i]]
                k = 0
                for i in self.items[0:len(a)]:
                    i.setText(a[k])
                    k += 1
                for i in self.items[len(a):]:
                    i.hide()
            else:
                self.items[-1].hide()
        else:
            self.close()


class TextEdit(QTextEdit):
    def __init__(self, parent=None):
        super(TextEdit, self).__init__(parent)
        self._completer = None
        self.cha = {'(': ')', '[': ']', '{': ']', '"': '"',
                    "'": "'", '"""': '"""', "'''": "'''"}
        self.lis = open('Files/wordpy','r').readlines()#[i.strip('\n') for i in ]
    def setCompleter(self, c):
        if self._completer is not None:
            self._completer.activated.disconnect()

        self._completer = c

        c.setWidget(self)
        c.setCompletionMode(QCompleter.PopupCompletion)
        c.setCaseSensitivity(Qt.CaseInsensitive)
        c.activated.connect(self.insertCompletion)

    def completer(self):
        return self._completer

    def insertCompletion(self, completion):
        if self._completer.widget() is not self:
            return

        tc = self.textCursor()
        extra = len(completion) - len(self._completer.completionPrefix())
        tc.movePosition(QTextCursor.Left)
        tc.movePosition(QTextCursor.EndOfWord)
        tc.insertText(completion[-extra:])
        self.setTextCursor(tc)

    def mergeFormatOnWordOrSelection(self, clr):
        fmt = QTextCharFormat()
        fmt.setForeground(clr)
        cursor = self.textCursor()
        cursor.select(0)
        cursor.mergeCharFormat(fmt)
        self.mergeCurrentCharFormat(fmt)

    def textUnderCursor(self):
        tc = self.textCursor()
        tc.select(QTextCursor.WordUnderCursor)

        return tc.selectedText()

    def focusInEvent(self, e):
        if self._completer is not None:
            self._completer.setWidget(self)

        super(TextEdit, self).focusInEvent(e)

    def keyPressEvent(self, e):
        if self._completer is not None and self._completer.popup().isVisible():
            if e.key() in (Qt.Key_Enter, Qt.Key_Return, Qt.Key_Escape, Qt.Key_Tab, Qt.Key_Backtab):
                e.ignore()
                return

        isShortcut = ((e.modifiers() & Qt.ControlModifier)
                      != 0 and e.text() == '$')
        if self._completer is None or not isShortcut:
            super(TextEdit, self).keyPressEvent(e)

        ctrlOrShift = e.modifiers() & (Qt.ControlModifier | Qt.ShiftModifier)
        if self._completer is None or (ctrlOrShift and len(e.text()) == 0):
            return
        completionPrefix = self.textUnderCursor()
        if len(completionPrefix) < 1:
            self._completer.popup().hide()
            return

        if completionPrefix != self._completer.completionPrefix():
            self._completer.setCompletionPrefix(completionPrefix)
            self._completer.popup().setCurrentIndex(
                self._completer.completionModel().index(0, 0))

        cr = self.cursorRect()
        cr.setWidth(self._completer.popup().sizeHintForColumn(
            0) + self._completer.popup().verticalScrollBar().sizeHint().width())
        self._completer.complete(cr)
        crsor = self.textCursor()
        txt = self.toPlainText().split("\n")[crsor.blockNumber()].rfind(" ")
        if txt == -1:
            i = 0
        else:
            i = txt+1
        if self.toPlainText().split("\n")[crsor.blockNumber()][i:]+'\n' in self.lis:
             Thread(target=self.mergeFormatOnWordOrSelection,args=(Qt.blue,)).start()
        else:
            Thread(target=self.mergeFormatOnWordOrSelection,args=(Qt.white,)).start()
        # for u in self.lis:

        #     if u == self.toPlainText()[-len(u):]:
        #         Thread(target=self.mergeFormatOnWordOrSelection,
        #                args=(Qt.green,)).start()
        #         break
        #     else:
        #         Thread(target=self.mergeFormatOnWordOrSelection,
        #                args=(Qt.white,)).start()



class Ui_Form(object):
    def setupUi(self, Form):
        screen = QApplication.primaryScreen()
        size = screen.size()
        self.w = size.width()
        self.h = size.height()
        Form.setObjectName("Form")
        Form.resize(self.w*0.682284, self.h*0.838541)
        Form.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowIcon(QIcon('icons/icon.png'))
        self.tabWidget_2 = QTabWidget(self)
        self.tabWidget_2.setGeometry(
            QRect(0, 0, self.w*0.674231, self.h*0.183593))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setGeometry(
            QRect(0, 40, self.w*0.674231, self.h*0.769531))
        self.ind, self.indi, self.fileo = 0, 0, 1
        self.setStyleSheet("QWidget{background-color: rgb(65, 65, 65);}\nQTabWidget::tab-bar {\n"
                           "     background-color: #fff;\n"
                           "    icon-position: relative;\n"
                           "}\n"
                           " QTabBar::tab {\n"
                           "    background-color:#323232;\n"
                           "    border-color: rgb(50, 50, 50);\n"
                           "    font: bold 12px \'Arial\';\n"
                           "    color: white;\n"
                           "    height:40px;\n"
                           "    width:170px;\n"
                           "\n"
                           " } \n"
                           "QTabBar::tab:!selected {\n"
                           "    background-color:rgb(50, 50, 50);\n"
                           "    color: white;\n"
                           "    icon-position: center;\n"
                           " }\n"
                           "\n"
                           "QTabBar::tab:hover {\n"
                           "    background-color: rgb(60, 60, 60);\n"
                           "    color: white;\n"
                           "    icon-position: left;\n"
                           " }\n"
                           "\n"
                           "\n"
                           " QTabWidget::pane { \n"
                           "     position: absolute;\n"
                           " }\n"
                           "\n"
                           "QTabBar::tab:selected {\n"
                           "    background-color:rgb(35, 35, 35);\n"
                           "    color: white;\n"
                           "}\n"
                           "QTabBar::close-button {\n"
                           "     image: url(icons/close.png)\n"
                           " }")
        self.tabWidget.setTabsClosable(True)
        self.tabWidget.setMovable(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget_2 = QTabWidget(self)
        self.tabWidget_2.setGeometry(
            QRect(0, 490, self.w*0.674231, self.w*5.446808))
        self.tabWidget_2.setObjectName("tabWidget_2")
        self.tabWidget_2.setTabsClosable(True)
        self.tabWidget_2.setMovable(True)
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setGeometry(
            QRect(0, 0, self.w*0.688872, self.h*0.053385))
        self.groupBox.setStyleSheet("QGroupBox {\n"
                                    "    background-color: rgb(50, 50, 50);\n"
                                    "    border: 0.5px rgb(50, 50, 50);\n"
                                    "    font: bold 12px \'Arial\';\n"
                                    "    color: white;\n"
                                    " } \n"
                                    "QPushButton:hover{color:black;background-color: black;border:5px solid  rgb(35, 35, 35);}\n"
                                    "QPushButton{color:white;background-color: rgb(55, 55, 55);border:0.3px solid  rgb(50, 50, 50);}QPushButton:pressed{color:black;background-color: rgb(79, 79, 79);;border: rgb(50, 50, 50);}\n"
                                    "\n"
                                    "")
        self.groupBox.setObjectName("groupBox")
        self.clrq = QColor(0, 0, 0)
        self.shadow = QGraphicsDropShadowEffect(
            blurRadius=100, xOffset=5, yOffset=5)
        self.shadow.setColor(self.clrq)
        self.groupBox.setGraphicsEffect(self.shadow)
        self.btn = []
        self.pushButton = QPushButton(self.groupBox)
        self.btn.append(self.pushButton)
        self.pushButton.setGeometry(QRect(900, 7, 28, 28))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(
            "QPushButton:hover{background-color:rgb(132, 0, 0);border:5px solid rgb(132, 0, 0);}\n"
            "QPushButton{background-color: rgb(50, 50, 50);border:0.3px solid  rgb(50, 50, 50);}QPushButton:pressed{background-color:rgb(170, 0, 0);border: rgb(50, 50, 50);}\n"
            "")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QPushButton(self.groupBox)
        self.btn.append(self.pushButton_2)
        self.pushButton_2.setGeometry(QRect(870, 7, 28, 28))
        font = QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(
            "QPushButton:hover{background-color:rgb(0, 118, 0);border:5px solid rgb(0, 118, 0);}\n"
            "QPushButton{background-color: rgb(50, 50, 50);border:0.3px solid  rgb(50, 50, 50);}QPushButton:pressed{background-color:rgb(0, 255, 0);border: rgb(50, 50, 50);}\n"
            "")
        self.pushButton_2.setObjectName("pushButton_2")
        self.lbl = QLabel(self.groupBox)
        self.lbl.setText('النسخة : ')
        font = QFont('abdo salem')
        font.setPointSize(25)
        font.setBold(True)
        self.lbl.setGeometry(750, 8, 90, 22)
        self.lbl.setFont(font)
        self.lbl.setStyleSheet('background-color: rgb(50, 50, 50);')
        self.doubleSpinBox = QDoubleSpinBox(self.groupBox)
        self.doubleSpinBox.setGeometry(690, 9, 56, 22)
        self.doubleSpinBox.setFont(font)
        self.doubleSpinBox.setStyleSheet("background-color: rgb(70, 70, 70);\n"
                                         "font: 75 16pt \"Audiowide\";\n"
                                         "")
        self.doubleSpinBox.setWrapping(False)
        self.doubleSpinBox.setAlignment(Qt.AlignCenter)
        self.doubleSpinBox.setDecimals(1)
        self.doubleSpinBox.setSingleStep(0.1)
        self.doubleSpinBox.setProperty("value", 3.7)
        self.doubleSpinBox.setValue(3.7)
        self.open = QPushButton(self.groupBox)
        self.btn.append(self.open)
        self.open.setGeometry(QRect(50, 8, 28, 28))
        icon = QIcon()
        icon.addPixmap(QPixmap("icons/save.png"), QIcon.Normal, QIcon.Off)
        self.open.setIcon(icon)
        self.open.setIconSize(QSize(24, 24))
        self.open.setObjectName("open")
        self.new = QPushButton(self.groupBox)
        self.btn.append(self.new)
        self.new.setGeometry(QRect(90, 8, 28, 28))
        self.new.setText("")
        icon1 = QIcon()
        icon1.addPixmap(QPixmap("icons/NEW.png"), QIcon.Normal, QIcon.Off)
        self.new.setIcon(icon1)
        self.new.setIconSize(QSize(24, 24))
        self.new.setObjectName("new")
        self.run = QPushButton(self.groupBox)
        self.btn.append(self.run)
        self.run.setGeometry(QRect(130, 9, 28, 28))
        icon2 = QIcon()
        icon2.addPixmap(QPixmap("icons/start-icosn.png"),
                        QIcon.Normal, QIcon.Off)
        self.run.setIcon(icon2)
        self.run.setIconSize(QSize(24, 24))
        self.run.setObjectName("run")
        self.start = QPushButton(self.groupBox)
        self.start.setGeometry(QRect(360, 0, 250, 45))
        self.start.setText('لنتعلم معا')
        # self.setAttribute(Qt.WA_TranslucentBackground,True)

        self.start.setStyleSheet(
            "QPushButton:hover{background-color:rgb(30, 30, 30);border:5px solid rgb(30, 30, 30);}\n"
            "QPushButton{color:white;background-color: rgb(50, 50, 50);border:0.3px solid  rgb(50, 50, 50);}QPushButton:pressed{background-color:rgb(80, 80, 80);border: rgb(80, 80, 80);}\n"
            "")
        self.start.setFont(font)
        self.start.setGraphicsEffect(self.shadow)
        self.slider = QSlider(Qt.Horizontal, self.groupBox)
        self.slider.setGeometry(QRect(180, 14, 100, 15))
        self.slider.setValue(100)
        self.slider.setStyleSheet("QSlider::groove:horizontal {\n"
                                  "    background-color:rgb(50, 50, 50);\n"
                                  "    border: 1px solid;\n"
                                  "    height: 10px;\n"
                                  "    margin: 0px;\n"
                                  "    }\n"
                                  "QSlider::handle:horizontal {\n"
                                  "    background-color:rgb(65, 65, 65);\n"
                                  "    border: 1px solid;\n"
                                  "    height: 40px;\n"
                                  "    width: 40px;\n"
                                  "    margin: -15px 0px;\n"
                                  "    }")
        self.open_2 = QPushButton(self.groupBox)
        self.btn.append(self.open_2)
        self.open_2.setGeometry(QRect(10, 8, 28, 28))
        icon3 = QIcon()
        icon3.addPixmap(QPixmap("icons/open.png"), QIcon.Normal, QIcon.Off)
        self.open_2.setIcon(icon3)
        self.open_2.setIconSize(QSize(24, 24))
        self.open_2.setObjectName("open_2")
        self.tabWidget.setCurrentIndex(0)
        self.tabWidget_2.setCurrentIndex(0)
        Form.setWindowTitle("McPython")
        self.tabWidget.setTabText(0, "Form")
        self.pushButton.setText("X")
        self.pushButton_2.setText("-")
        self.run.setEnabled(False)
        self.open.setEnabled(False)


class Frame(QWidget, Ui_Form):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.file = 1
        
        self.new.clicked.connect(self.newfile)
        self.tabWidget.tabCloseRequested.connect(self.closeCode)
        self.pushButton.clicked.connect(self.close)
        self.open_2.clicked.connect(self.openfile)
        self.open.clicked.connect(self.savefile)
        self.pushButton_2.clicked.connect(
            lambda: self.setWindowState(Qt.WindowMinimized))
        self.run.clicked.connect(self.Run)
        self.start.clicked.connect(self.StartT)
        self.det = [0, 1]
        self.az = 1
        self.cha = {'(': ')', '[': ']', '{': '}', '"': '"',
                    "'": "'", '"""': '"""', "'''": "'''"}
        self.evin = False
        self.process = None
        self.Tab = []
        self.Text = []
        self.Result = []
        self.Language = []
        self.Completer = []
        self.co = ''
        self.fileType = "Python file (*.py)"
        self.punctuation = """!$%&():"*/;<>?@[\]^_`|~"""
        self.auto = False
        self.ver = True
        open('Files/choice', 'w').truncate(0)
        for i in self.btn:
            i.setMask(QRegion(i.rect(), QRegion.Ellipse))

        self.slider.valueChanged.connect(self.opacity)
        

    def mouseReleaseEvent(self, event):
        if event.y() < 56 and self.ver:
            self.animBar(-60, 0)
            self.ver = False
        elif event.y() > 56 and self.ver is False:
            self.animBar(0, -60)
            self.ver = True
        super(Frame, self).mouseReleaseEvent(event)

    def openfile(self):
        

        fname = QFileDialog.getOpenFileName(self, 'Open file',
                                            'c:\\', "Python file (*.py) ;;Dart file (*.dart)")
        if fname[0] != "":
            file = open(fname[0], 'r').read()
            self.newfile()
            self.text.setPlainText(file)

    def savefile(self):
        if self.Language[self.tabWidget.currentIndex()].currentText() == "Python":
            self.fileType = "Python file (*.py)"
        else:
            self.fileType = "Dart file (*.dart)"
        fname = QFileDialog.getSaveFileName(self, 'Save file',
                                            'c:\\untitle_%i' % (self.tabWidget.currentIndex()+1), self.fileType)
        ind = self.tabWidget.currentIndex()
        if fname[0] != "":
            open(fname[0], 'w').write(self.Text[ind].toPlainText())

    def opacity(self):
        sl = self.slider.value()
        if sl > 10:
            self.setWindowOpacity(sl / 100)

    def animBar(self, x, y):
        self.anim = QPropertyAnimation(self.groupBox, b'geometry')
        self.anim.setDuration(300)
        self.anim.setEasingCurve(QEasingCurve.OutSine)
        self.anim.setStartValue(QRect(0, x, 941, 41))
        self.anim.setEndValue(QRect(0, y, 941, 41))
        self.anim.start()

    def closeCode(self, i):
        self.tabWidget.removeTab(i)
        self.Tab.remove(self.Tab[i])
        self.Text.remove(self.Text[i])
        self.ind -= 1
        self.groupBox.setGraphicsEffect(self.shadow)
        if len(self.Tab) == 0:
            self.run.setEnabled(False)
            self.open.setEnabled(False)
        self.closeDebug(i)

    def closeDebug(self, i):
        self.tabWidget_2.removeTab(i)
        self.indi -= 1
        self.groupBox.setGraphicsEffect(self.shadow)

    def keyReleaseEvent(self, event):
        self.det.append(event.text())
        try:
            if event.text() == '':
                self.time.stop()
            if not self.auto:
                re = self.text.toPlainText().count(':')
                if self.det[-1] == '\r' and self.det[-2] == ':':
                    self.text.insertPlainText("    " * re)
                    self.evin = True
                elif event.text() == '\r' and self.evin is True:
                    self.text.insertPlainText("    " * re)

                if event.text() in list(self.cha.keys()):
                    ind = self.tabWidget.currentIndex()
                    self.Text[ind].insertPlainText(self.cha[event.text()])
                    self.Text[ind].moveCursor(QTextCursor.Left)
                if len(self.det) == 4:
                    self.det.remove(self.det[0])

        except Exception as f:
            pass

    def newfile(self):
        self.open.setEnabled(True)
        self.run.setEnabled(True)
        self.tab_2 = QWidget()
        self.Tab.append(self.tab_2)
        self.tab_2.setObjectName("tab_2")
        self.text = TextEdit(self.tab_2)
        self.text.setFont(QFont('Roboto Light'))
        self.language = QComboBox(self.tab_2)
        font = QFont()
        font.setPointSize(15)
        self.language.setFont(font)
        self.language.addItems(["Python", "Dart"])
        self.language.setGeometry(self.w*0.600231, self.h*0.500156, 100, 30)
        self.Text.append(self.text)
        self.text.setGeometry(QRect(0, 0, self.w*0.674231, self.h*0.535156))
        self.completer = QCompleter(self)
        self.completer.setModel(self.getWord('Files/wordpy'))
        self.text.setCompleter(self.completer)
        self.Completer.append(self.completer)
        self.Language.append(self.language)
        
        
        font = QFont()
        font.setPointSize(15)
        self.text.setFont(font)
        self.text.setStyleSheet("#text{\n"
                                "color: white;\n"
                                "background-color: rgb(35, 35, 35);\n"
                                "border:0.5px rgb(35, 35, 35);\n"
                                "}")
        self.text.setObjectName("text")
        self.tabWidget.addTab(self.tab_2, "Untitle_%i" % (self.file))
        self.tabWidget.setCurrentIndex(self.ind)
        self.Language[-1].activated[str].connect(partial(self.changeL,index=self.tabWidget.currentIndex()))
        self.ind += 1
        self.file += 1
        self.tabWidget.setGraphicsEffect(self.shadow)
        self.text.setFocus(False)
        self.newDebug()


    def changeL(self, lang,index):
        if self.Language[index].currentText() == "Python":
            self.Completer[index].setModel(self.getWord('Files/wordpy'))
            self.Text[index].lis = open('Files/wordpy','r').readlines()
           
            
        else:
            self.Text[index].setText("""main(){

}""")       
            self.Text[index].moveCursor(QTextCursor.Up)
            self.completer.setModel(self.getWord('Files/worddart'))
            self.Text[index].lis = open('Files/worddart','r').readlines()
            

    def getWord(self, file):
        a = open(file, 'r').readlines()
        return QStringListModel(a, self.completer)

    @pyqtSlot()
    def RunS(self):
        self.process = QProcess()
        self.process.setProcessChannelMode(QProcess.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.WorkReply)
        self.process.finished.connect(self.WorkFinished)
        version = self.doubleSpinBox.value()
        ind = self.tabWidget.currentIndex()
        if self.Language[ind].currentText().lower() == "python":
            commande = f"{self.Language[ind].currentText().lower()[:2]} -{str(version)[:3]} Files/Run"
        else:
            commande = f"{self.Language[ind].currentText().lower()} Files/Run"
        self.process.start(commande, QIODevice.ReadWrite)
        self.process.waitForStarted()
        self.text.setFocus(True)

    @pyqtSlot()
    def WorkReply(self):
        data = self.process.readAllStandardOutput().data()
        ch = str(data, encoding="utf-8").rstrip()
        ind = self.tabWidget.currentIndex()
        self.Result[ind].setPlainText(ch)

    @pyqtSlot()
    def WorkFinished(self):
        if self.process != None:
            self.process.readyReadStandardOutput.disconnect()
            self.process.finished.disconnect()

    def newDebug(self):
        ind = self.tabWidget.currentIndex()
        self.tabWidget_2.setGraphicsEffect(self.shadow)
        self.tab = QWidget()
        self.tab.setObjectName("tab")
        self.result = QPlainTextEdit(self.tab)
        self.result.setReadOnly(True)
        font = QFont()
        font.setPointSize(12)
        self.result.setFont(font)
        self.Result.append(self.result)
        self.result.setGeometry(QRect(0, 0, self.w*0.674231, self.h*0.14453))
        self.result.setStyleSheet("#result{\n"
                                  "color: white;\n"
                                  "background-color: rgb(35, 35, 35);\n"
                                  "border:0.5px rgb(35, 35, 35);\n"
                                  "}")
        self.result.setObjectName("result")
        self.tabWidget_2.addTab(self.tab, "Untitle_%i" % (ind+1))
        self.tabWidget_2.setCurrentIndex(self.ind)
        
    def Run(self):
        ind = self.tabWidget.currentIndex()
        open('Files/Run', 'w').write(self.Text[ind].toPlainText())
        self.RunS()
        self.tabWidget_2.setCurrentIndex(ind)


    def StartT(self):
        self.gm = {"{": "'", "}": '='}
        self.start.setText('*لنتعلم معا*')
        self.start.setStyleSheet(
            'background-color:rgb(30, 30, 30);border:5px solid rgb(30, 30, 30);')
        d = StartTuto()
        self.setWindowOpacity(0.4)
        d.exec_()
        self.start.setText('لنتعلم معا')
        self.start.setStyleSheet(
            "QPushButton:hover{background-color:rgb(30, 30, 30);border:5px solid rgb(30, 30, 30);}\n"
            "QPushButton{color:white;background-color: rgb(50, 50, 50);border:0.3px solid  rgb(50, 50, 50);}QPushButton:pressed{background-color:rgb(80, 80, 80);border: rgb(80, 80, 80);}\n"
            "")
        self.setWindowOpacity(1)
        self.o = 0
        self.fil = open('Files/choice', 'r').read().rstrip()[2:]
        open('Files/choice', 'w').truncate(0)
        self.auto = True
        if self.fil == 'it':
            self.auto = False
        elif self.fil == 'me':
            self.StartT()
        else:
            self.time = QTimer()
            self.time.timeout.connect(self.tuto)
            self.time.start(300)

    def PRESS(self):
        hllDll = ctypes.WinDLL("User32.dll")
        VK_CAPITAL = 0x14
        if hllDll.GetKeyState(VK_CAPITAL) == 1:
            press('capslock')

    def tuto(self):
        if self.o == 0:
            self.newfile()
            self.text.setFocus()

        elif self.o == self.co - 1:
            self.Run()
            self.time.stop()
            self.auto = False
        self.PRESS()
        code = open('Files/%s' % (self.fil), 'r').read()
        liC = []
        for i in code:
            liC.append(i)
        liC.append(' ')
        self.co = len(liC)
        if liC[self.o] in self.punctuation:
            press('capslock')
            press(liC[self.o])
        elif liC[self.o] in ['{', '}']:
            hotkey('altright', self.gm[liC[self.o]])
        else:
            press(liC[self.o])

        self.o += 1


class StartApp(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setWindowTitle("Starting McPython")

        self.setStyleSheet('QWidget{background-color: rgb(65, 65, 65);}')
        self.setWindowIcon(QIcon('icons/icon.png'))
        lab = QLabel(self)
        lab.resize(500, 250)
        image = QImage('icons/mylogo.png')
        lab.setPixmap(QPixmap.fromImage(image))
        self.ba = QProgressBar(lab)
        self.ba.setStyleSheet("""QProgressBar
        {
        	color:#242425;
            text-align: center;
             background-color:#0068ad;
             border: 1px solid #0068ad;

        }
        QProgressBar::chunk
        {
            background-color:#f05a23;
            margin: 2.5px;
        }""")
        font = QFont('abdo salem')
        font.setPointSize(20)
        font.setBold(True)
        self.ba.setValue(2)
        self.ba.setFont(font)
        self.ba.setGeometry(-5, 200, 510, 30)
        self.val = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.ch)
        self.timer.start(30)
        self.resize(500, 250)

    def ch(self):
        self.ba.setValue(self.val)
        self.val += 1
        if self.val == 100:
            frame = Frame()
            frame.show()
            self.close()


app = QApplication([])
start = StartApp()
start.show()
app.exec_()
