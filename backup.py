# author = Astrealzero
############################################################
# 项目日志
'''
2022/4/10  V0.1
窗口无边框，加载人物gif，无边框下鼠标拖动。
2022/4/13  v0.2
创建右键菜单。
增加人物切换选项
bug：运行程序后第一个操作或多次右键呼出菜单时会导致程序崩溃
bug：菜单多次操作会导致程序崩溃
2022/4/14  v0.3
增加左键点击语音
修复bug菜单多次操作导致的崩溃
2022/4/15  V0.4
优化人物切换菜单
增加新人物，同时切换人物后人物语音不同
2022/4/20  V0.5
增加人物移动功能(PS:仅限方向键移动)
2023/2/27  重启项目
'''
############################################################
from PyQt5 import QtMultimedia
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMenu
from PyQt5.QtGui import QMovie, QCursor
from PyQt5.QtCore import Qt

import random
import sys


class M_Win(QWidget):

    def __init__(self):
        super().__init__()
        self.m_ui()

    # 窗口
    def m_ui(self):
        self.x = 1560
        self.y = 610
        self.resize(350, 484)  # 程序窗口大小
        self.move(self.x, self.y)  # 程序窗口位置
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.SplashScreen)  # 置顶，去掉边框，隐藏任务栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        # gif加载
        self.label = QLabel(self)
        movie = QMovie(r"./img/chuochong1.gif")
        self.label.setMovie(movie)
        movie.start()
        # 右键菜单声明
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)
        # 参数组
        self.ren = 1
        self.sudu = 0

    # 菜单
    def rightMenuShow(self, position):
        menu = QMenu()
        # 菜单栏
        quitAction1 = menu.addMenu("切换人物")
        renwuX1 = quitAction1.addAction("试作型1号人物")
        renwuX2 = quitAction1.addAction("试作型2号人物")
        renwuX3 = quitAction1.addAction("试作型3号人物")
        quitAction2 = menu.addAction("启动X代码")
        quitAction0 = menu.addAction("退出")
        action = menu.exec_(self.mapToGlobal(position))
        # 选项效果
        if action == quitAction0:  # 退出
            sys.exit()
        if action == renwuX1:  # 1号人物
            movie = QMovie(r"./img/chuochong1.gif")
            self.label.setMovie(movie)
            movie.start()
            self.ren = 1
        if action == renwuX2:  # 2号人物
            movie = QMovie(r"./img/chuochong2.gif")
            self.label.setMovie(movie)
            movie.start()
            self.ren = 2
        if action == renwuX3:  # 3号人物
            movie = QMovie(r"./img/alma1.gif")
            self.label.setMovie(movie)
            movie.start()
            self.ren = 3
        if action == quitAction2:
            self.Yingyue = 'music/ceva011.wav'
            self.Yingyue = QtMultimedia.QSound(self.Yingyue)
            self.Yingyue.play()

    # 鼠标按下侦测
    def mousePressEvent(self, event):  # 无边框移动,语音
        if event.button() == Qt.LeftButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标
        # 点击语音
        if event.button() == Qt.LeftButton and self.ren == 1:
            self.Yingyue = 'music/zhuochong1.wav'
            self.Yingyue = QtMultimedia.QSound(self.Yingyue)
            self.Yingyue.play()
        if event.button() == Qt.LeftButton and self.ren == 2:
            self.Yingyue = 'music/renwuyy.wav'
            self.Yingyue = QtMultimedia.QSound(self.Yingyue)
            self.Yingyue.play()
        if event.button() == Qt.LeftButton and self.ren == 3:
            suiji = random.choice(range(1, 9))
            if event.button() == Qt.LeftButton and suiji == 1:
                self.Yingyue = 'music/alma-001.wav'
                self.Yingyue = QtMultimedia.QSound(self.Yingyue)
                self.Yingyue.play()
            if event.button() == Qt.LeftButton and suiji == 2:
                self.Yingyue = 'music/alma-002.wav'
                self.Yingyue = QtMultimedia.QSound(self.Yingyue)
                self.Yingyue.play()
            if event.button() == Qt.LeftButton and suiji == 3:
                self.Yingyue = 'music/alma-003.wav'
                self.Yingyue = QtMultimedia.QSound(self.Yingyue)
                self.Yingyue.play()
            if event.button() == Qt.LeftButton and suiji == 4:
                self.Yingyue = 'music/alma-004.wav'
                self.Yingyue = QtMultimedia.QSound(self.Yingyue)
                self.Yingyue.play()
            if event.button() == Qt.LeftButton and suiji == 5:
                self.Yingyue = 'music/alma-005.wav'
                self.Yingyue = QtMultimedia.QSound(self.Yingyue)
                self.Yingyue.play()
            if event.button() == Qt.LeftButton and suiji == 6:
                self.Yingyue = 'music/alma-006.wav'
                self.Yingyue = QtMultimedia.QSound(self.Yingyue)
                self.Yingyue.play()
            if event.button() == Qt.LeftButton and suiji == 7:
                self.Yingyue = 'music/alma-007.wav'
                self.Yingyue = QtMultimedia.QSound(self.Yingyue)
                self.Yingyue.play()
            if event.button() == Qt.LeftButton and suiji == 8:
                self.Yingyue = 'music/alma-008.wav'
                self.Yingyue = QtMultimedia.QSound(self.Yingyue)
                self.Yingyue.play()

    # 鼠标按住侦测
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.m_flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()

    # 鼠标放开侦测
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))

    # 键盘侦测
    def keyPressEvent(self, event):
        if (event.key() == Qt.Key_Right):
            self.sudu = 10
            self.x += self.sudu
            self.move(self.x, self.y)  # 更改窗口位置
        if (event.key() == Qt.Key_Left):
            self.sudu = -10
            self.x += self.sudu
            self.move(self.x, self.y)  # 更改窗口位置


app = QApplication(sys.argv)
win = M_Win()
win.show()
sys.exit(app.exec_())
