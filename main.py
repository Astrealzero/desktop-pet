import sys
import time

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QMovie, QCursor
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMenu

import mdxshujv
import zxskdshujv


class M_Win(QWidget):

    def __init__(self):
        super().__init__()

        #  参数组
        self.label = QLabel(self)
        self.y = 610
        self.x = 1560
        self.ren = 1
        self.sudu = 0
        self.m_flag = False
        self.TXFC = 0
        self.TXFCTF = False

        #  动作模块
        #  初始状态
        self.renwumoxing = zxskdshujv
        self.zhuangtai = self.renwumoxing.zhuangtai
        self.fxleft = True
        self.renwul = self.renwumoxing.renwul
        self.fxright = False
        self.renwur = self.renwumoxing.renwur
        #  语言模块
        self.yycn = True
        self.yycnshuzu = self.renwumoxing.yycnshuzu

        self.yyjp = False
        self.yyjpshuzu = self.renwumoxing.yyjpshuzu

        #  调用窗口
        self.m_ui()
        print(1)

    # 窗口
    def m_ui(self):
        self.resize(300, 300)  # 程序窗口大小
        self.move(self.x, self.y)  # 程序窗口位置
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.SplashScreen)  # 置顶，去掉边框，隐藏任务栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        # 初始化
        movie = QMovie(self.zhuangtai)  # r"./img/zxskd/zxskdzdl.gif"
        self.label.setMovie(movie)
        movie.start()
        # 右键菜单声明
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)
        print(2)

    # 菜单
    def rightMenuShow(self, position):
        menu = QMenu()
        # 菜单栏
        # quitAction1 = menu.addMenu("切换人物方向")
        # renwuX1 = quitAction1.addAction("left")
        # renwuX2 = quitAction1.addAction("right")
        quitAction2 = menu.addMenu("动作")
        dongzuo3 = quitAction2.addAction("站立状态")
        dongzuo2 = quitAction2.addAction("悬坐状态")
        dongzuo1 = quitAction2.addAction("特殊状态")
        # jporcn = menu.addMenu("语言切换")
        # cnzh = jporcn.addAction("中文")
        # jpzh = jporcn.addAction("日文")
        quitAction3 = menu.addMenu("切换人物")
        mdx = quitAction3.addAction("迷迭香")
        zxskd = quitAction3.addAction("浊心斯卡蒂")
        quitAction0 = menu.addAction("退出")
        action = menu.exec_(self.mapToGlobal(position))
        # 选项效果
        # 人物切换模块
        if action == mdx:
            self.renwumoxing = mdxshujv
            self.renwuqiehuan()
        elif action == zxskd:
            self.renwumoxing = zxskdshujv
            self.renwuqiehuan()

        if action == quitAction0:  # 退出
            sys.exit()
        # 人物方向切换模块
        # if action == renwuX1:  # 向左
        #     self.fxleft = True
        #     self.fxright = False
        #     for iiii in self.renwur:
        #         if self.zhuangtai == iiii:
        #             sumiiii = self.renwur.index(iiii)
        #             movie = QMovie(self.renwul[sumiiii])
        #             self.label.setMovie(movie)
        #             movie.start()
        #             self.zhuangtai = self.renwul[sumiiii]
        #             break
        # if action == renwuX2:  # 向右
        #     self.fxleft = False
        #     self.fxright = True
        #     for iiii in self.renwul:
        #         if self.zhuangtai == iiii:
        #             sumiiii = self.renwul.index(iiii)
        #             movie = QMovie(self.renwur[sumiiii])
        #             self.label.setMovie(movie)
        #             movie.start()
        #             self.zhuangtai = self.renwur[sumiiii]
        #             break
        # #  语言切换模块
        # if action == cnzh:
        #     self.yycn = True
        #     self.yyjp = False
        # if action == jpzh:
        #     self.yycn = False
        #     self.yyjp = True
        #  人物动作切换模块
        if action == dongzuo1:
            if self.fxright:
                movie = QMovie(self.renwur[4])
                self.label.setMovie(movie)
                movie.start()
                self.zhuangtai = self.renwur[4]
            elif self.fxleft:
                movie = QMovie(self.renwul[4])
                self.label.setMovie(movie)
                movie.start()
                self.zhuangtai = self.renwul[4]
        if action == dongzuo2:
            if self.fxright:
                movie = QMovie(self.renwur[1])
                self.label.setMovie(movie)
                movie.start()
                self.zhuangtai = self.renwur[1]
            elif self.fxleft:
                movie = QMovie(self.renwul[1])
                self.label.setMovie(movie)
                movie.start()
                self.zhuangtai = self.renwul[1]
        if action == dongzuo3:
            if self.fxright:
                movie = QMovie(self.renwur[0])
                self.label.setMovie(movie)
                movie.start()
                self.zhuangtai = self.renwur[0]
            elif self.fxleft:
                movie = QMovie(self.renwul[0])
                self.label.setMovie(movie)
                movie.start()
                self.zhuangtai = self.renwul[0]

        print(3)

    # 人物模型切换
    def renwuqiehuan(self):
        self.yycnshuzu = self.renwumoxing.yycnshuzu
        self.yyjpshuzu = self.renwumoxing.yyjpshuzu
        self.zhuangtai = self.renwumoxing.zhuangtai
        self.renwul = self.renwumoxing.renwul
        self.renwur = self.renwumoxing.renwur
        movie = QMovie(self.zhuangtai)
        self.label.setMovie(movie)
        movie.start()

    # 鼠标按下侦测
    def mousePressEvent(self, event):  # 无边框移动,语音
        if event.button() == Qt.MidButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标
        # if event.button() == Qt.LeftButton:
        #     self.TXFCTF = True
        #     if self.fxright:
        #         movie = QMovie(self.renwur[3])
        #         self.label.setMovie(movie)
        #         self.TXFC = movie.frameCount()
        #         movie.start()
        #
        #     elif self.fxleft:
        #         movie = QMovie(self.renwul[3])
        #         self.label.setMovie(movie)
        #         self.TXFC = movie.frameCount()
        #         movie.start()
        #     self.countdown(0.2)

        print(4)

    # 鼠标按住侦测
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.MidButton and self.m_flag:
            if self.fxright:
                movie = QMovie(self.renwur[2])
                self.label.setMovie(movie)
                movie.start()
            elif self.fxleft:
                movie = QMovie(self.renwul[2])
                self.label.setMovie(movie)
                movie.start()
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()
        print(5)

    # 鼠标放开侦测
    def mouseReleaseEvent(self, QMouseEvent):
        # if self.m_flag == True:
        #     if self.fxright == True:
        #         movie = QMovie(self.zhuangtai)
        #         self.label.setMovie(movie)
        #         movie.start()
        #     elif self.fxleft == True:
        #         movie = QMovie(self.zhuangtai)
        #         self.label.setMovie(movie)
        #         movie.start()
        #     self.m_flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
        print(6)

    def countdown(self, t):
        start_time = time.time()
        while time.time() - start_time < t:
            pass
        movie = QMovie(self.zhuangtai)
        self.label.setMovie(movie)
        movie.start()

    # 键盘侦测
    # def keyPressEvent(self, event):
    #     if (event.key() == Qt.Key_Right):
    #         self.sudu = 10
    #         self.x += self.sudu
    #         self.move(self.x, self.y)  # 更改窗口位置
    #     if (event.key() == Qt.Key_Left):
    #         self.sudu = -10
    #         self.x += self.sudu
    #         self.move(self.x, self.y)  # 更改窗口位置
    # def yymokuai(self):
    #     suiji = random.choice(range(0, 10))
    #     if self.yycn == True:
    #         self.Yingyue = self.yycnshuzu[suiji]
    #         self.Yingyue = QtMultimedia.QSound(self.Yingyue)
    #         self.Yingyue.play()
    #     if self.yyjp == True:
    #         self.Yingyue = self.yyjpshuzu[suiji]
    #         self.Yingyue = QtMultimedia.QSound(self.Yingyue)
    #         self.Yingyue.play()


app = QApplication(sys.argv)
win = M_Win()
win.show()
sys.exit(app.exec_())
