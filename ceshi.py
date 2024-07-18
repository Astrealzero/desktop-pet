import sys
import os
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDir
from PyQt5.QtGui import (QIcon, QMovie, QPalette, QImage)
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QLabel, QMenuBar,
                             QToolButton, QStyle, QMenu, QAction, QScrollArea,
                             QHBoxLayout, QVBoxLayout, QSizePolicy, QGroupBox,
                             QFileDialog, QMessageBox)


class GifPlayer(QMainWindow):
    def __init__(self, parent=None):
        super(GifPlayer, self).__init__(parent)

        # 设置窗口标题
        self.setWindowTitle("实战 Qt for Python: QMovie实现一个GIF动画播放")
        # 设置窗口大小
        self.resize(500, 400)

        # 播放状态记录变量
        self.is_playing = False
        self.is_pause = False
        self.total_frame = 0
        self.cur_frame = 0

        self.initUi()

    def initUi(self):

        # 创建显示图片的窗口
        self.imgLabel = QLabel()
        self.imgLabel.setBackgroundRole(QPalette.Base)
        self.imgLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.imgLabel.setScaledContents(True)

        self.scrollArea = QScrollArea()
        self.scrollArea.setBackgroundRole(QPalette.Dark)
        self.scrollArea.setWidget(self.imgLabel)

        self.createPlayCtlr()

        mainLayout = QVBoxLayout()
        mainLayout.setContentsMargins(0, 0, 0, 0)
        mainLayout.addWidget(self.scrollArea)
        mainLayout.addWidget(self.grpButtons)

        mainWidget = QWidget()
        mainWidget.setLayout(mainLayout)
        self.setCentralWidget(mainWidget)

        self.initMenuBar()

        # 创建动画播放器
        self.movie = QMovie()
        self.movie.setCacheMode(QMovie.CacheAll)  # 支持回卷

        '''       
        self.movie = QMovie(os.path.dirname(__file__) + "/use-python.gif")
        self.movie.setScaledSize(QtCore.QSize(img_width, img_height))


        label = QLabel(self)
        label.move(20, 10)
        label.setFixedSize(img_width, img_height)
        label.setMovie(self.movie)
        self.movie.jumpToFrame(0)      
        '''

    def initMenuBar(self):
        menuBar = self.menuBar()
        menuFile = menuBar.addMenu('文件(&F)')
        menuView = menuBar.addMenu('视图(&V)')

        actionOpen = QAction('打开(&O)...', self, shortcut='Ctrl+O', triggered=self.onFileOpen)
        self.actionExport = QAction('导出(&E)...', self, shortcut='Ctrl+E', enabled=False, triggered=self.onFileExport)
        actionExit = QAction('退出(&X)', self, shortcut='Ctrl+Q', triggered=QApplication.instance().quit)

        self.actionFitToWindow = QAction('适应窗口(&F)', self, shortcut='Ctrl+F', enabled=False, checkable=True,
                                         triggered=self.onViewFitToWindow)

        menuFile.addAction(actionOpen)
        menuFile.addAction(self.actionExport)
        menuFile.addSeparator()
        menuFile.addAction(actionExit)

        menuView.addAction(self.actionFitToWindow)

    def createPlayCtlr(self):
        # 播放按钮控制部分
        self.btn_play = QToolButton()
        self.btn_play.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.btn_play.clicked.connect(lambda: self.play(100))
        # 创建三种不同速率播放的Action
        action_slow = QAction('慢速播放', self)
        action_slow.triggered.connect(lambda: self.play(25))
        action_normal = QAction('常速播放', self)
        action_normal.triggered.connect(lambda: self.play(100))
        action_fast = QAction('快速播放', self)
        action_fast.triggered.connect(lambda: self.play(400))
        # 弹出菜单
        self.popup_menu = QMenu(self)
        self.popup_menu.addAction(action_slow)
        self.popup_menu.addAction(action_normal)
        self.popup_menu.addAction(action_fast)
        self.btn_play.setPopupMode(QToolButton.MenuButtonPopup)
        self.btn_play.setAutoRaise(True)
        self.btn_play.setMenu(self.popup_menu)

        self.setPlayButtonState()

        self.btn_first = QToolButton()
        self.btn_first.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaSkipBackward))
        self.btn_first.setText("到头")
        self.btn_first.setToolTip("到第一帧")
        self.btn_first.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.btn_first.setStyleSheet('border: 0px')
        self.btn_first.clicked.connect(self.firstFrame)

        self.btn_last = QToolButton()
        self.btn_last.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaSkipForward))
        self.btn_last.setText("到尾")
        self.btn_last.setToolTip("到最后一帧")
        self.btn_last.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.btn_last.setStyleSheet('border: 0px')
        self.btn_last.clicked.connect(self.lastFrame)

        self.btn_prev = QToolButton()
        self.btn_prev.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaSeekBackward))
        self.btn_prev.setText("前帧")
        self.btn_prev.setToolTip("到前一帧")
        self.btn_prev.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.btn_prev.setStyleSheet('border: 0px')
        self.btn_prev.clicked.connect(self.prevFrame)

        self.btn_next = QToolButton()
        self.btn_next.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaSeekForward))
        self.btn_next.setText("后帧")
        self.btn_next.setToolTip("到后一帧")
        self.btn_next.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.btn_next.setStyleSheet('border: 0px')
        self.btn_next.clicked.connect(self.nextFrame)

        btnLayout = QHBoxLayout()
        btnLayout.setContentsMargins(0, 0, 0, 0)
        btnLayout.addWidget(self.btn_play)
        btnLayout.addWidget(self.btn_first)
        btnLayout.addWidget(self.btn_last)
        btnLayout.addWidget(self.btn_prev)
        btnLayout.addWidget(self.btn_next)

        self.grpButtons = QGroupBox()
        self.grpButtons.setStyleSheet('border: 0px')
        self.grpButtons.setLayout(btnLayout)

        self.grpButtons.setEnabled(False)

    # 打开文件
    def onFileOpen(self):
        filename, _ = QFileDialog.getOpenFileName(self, '打开动画', QDir.currentPath(),
                                                  'GIF Files(*.gif);;All Files(*)')

        if filename:
            self.movie.setFileName(filename)
            if not self.movie.isValid():
                QMessageBox.information(self, '动画播放', '不能加载文件%s.' % filename)
                return

            self.total_frame = self.movie.frameCount()  # 保存总帧数
            self.movie.stop()
            self.is_playing = False

            self.imgLabel.setMovie(self.movie)
            self.movie.jumpToFrame(0)

            self.actionExport.setEnabled(True)
            self.actionFitToWindow.setEnabled(True)
            self.grpButtons.setEnabled(True)

            if not self.actionFitToWindow.isChecked():
                self.imgLabel.adjustSize()

            self.play(100)
            self.setPlayButtonState()

    def onFileExport(self):
        path, _ = QFileDialog.getSaveFileName(self, '导出图像文件', '', '图像文件 (*.png)')
        if not path:
            return

        isRunning = self.movie.state()
        if isRunning:
            self.movie.setPaused(True)
        img = self.movie.currentImage()
        img.save(path, 'PNG', 100)
        if isRunning:
            self.movie.setPaused(False)

    def onViewFitToWindow(self):
        fitToWindow = self.actionFitToWindow.isChecked()
        self.scrollArea.setWidgetResizable(fitToWindow)
        if not fitToWindow:
            self.imgLabel.adjustSize()

    # 修改播放按钮的状态
    def setPlayButtonState(self):
        if self.is_playing:
            self.btn_play.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaStop))
            self.btn_play.setText("停止")
            self.btn_play.setToolTip("点击按钮停止播放")
            self.popup_menu.setEnabled(False)
        else:
            self.btn_play.setIcon(QApplication.style().standardIcon(QStyle.SP_MediaPlay))
            self.btn_play.setText("播放")
            self.btn_play.setToolTip("点击按钮开始播放")
            self.popup_menu.setEnabled(True)

    # 播放按钮的槽函数
    def play(self, speed):
        if self.is_playing:
            self.movie.stop()
            self.movie.jumpToFrame(0)  # 回到第一帧
            self.is_playing = False
        else:
            self.movie.start()
            self.movie.setSpeed(speed)
            self.is_playing = True
        self.setPlayButtonState()

    # 到设定的当前帧
    def toFrame(self):
        if self.is_playing:
            self.movie.stop()
            self.is_playing = False
            self.setPlayButtonState()
        self.movie.jumpToFrame(self.cur_frame)

    # 到第一帧
    def firstFrame(self):
        self.cur_frame = 0
        self.toFrame()

    # 到最后一帧
    def lastFrame(self):
        self.cur_frame = self.total_frame - 1
        self.toFrame()

    # 到前一帧
    def prevFrame(self):
        if self.cur_frame <= 0:
            self.cur_frame = self.total_frame - 1
        else:
            self.cur_frame = self.cur_frame - 1
        self.toFrame()

    # 到后一帧
    def nextFrame(self):
        if self.cur_frame >= self.total_frame - 1:
            self.cur_frame = 0
        else:
            self.cur_frame = self.cur_frame + 1
        self.toFrame()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = GifPlayer()
    window.show()
    sys.exit(app.exec())