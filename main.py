#  author = Astrealzero
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
2023/3/2   V0.6
更改了新的主要人物gif，封存旧人物gif
改进了语言模块
新增人物朝向控制选项
删除了人物按键移动功能
2023/3/3  v0.7
完善了人物朝向控制
修复了改变人物时方向未继承的情况
加入了鼠标拖动人物时的动作
修改了模块加载相关代码
修改了人物数组存储和调用的方式
增加更换人物功能
2023/3/7  v0.8
将鼠标左键移动修改为鼠标中间移动
暂时关闭语音功能（语音功能会导致点击人物时发生短暂卡顿）
正在修复点击人物后人物继续循环播放的bug
'''
############################################################
from PyQt5 import QtMultimedia
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMenu
from PyQt5.QtGui import QMovie, QCursor
from PyQt5.QtCore import Qt

import random
import sys

import mdxshujv
import zxskdshujv


class M_Win(QWidget):

    def __init__(self):
        super().__init__()

        #  参数组
        self.ren = 1
        self.sudu = 0
        self.m_flag = False
        self.TXFC = 0
        self.TXFCTF = False
        #  语言模块
        self.yycn = False
        self.yycnshuzu = zxskdshujv.yycnshuzu

        self.yyjp = True
        self.yyjpshuzu = zxskdshujv.yyjpshuzu
        #  动作模块
        #  当前状态
        self.zhuangtai = zxskdshujv.zhuangtai

        self.fxleft = True
        self.renwul = zxskdshujv.zxskdrenwul
        self.fxright = False
        self.renwur = zxskdshujv.zxskdrenwur
        #  调用窗口
        self.m_ui()
        print(1)
    # 窗口
    def m_ui(self):
        self.x = 1560
        self.y = 610
        self.resize(300, 300)  # 程序窗口大小
        self.move(self.x, self.y)  # 程序窗口位置
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.SplashScreen)  # 置顶，去掉边框，隐藏任务栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        # 初始化
        self.label = QLabel(self)
        movie = QMovie(self.zhuangtai)  # r"./img/zxskd/zxskdzdl.gif"
        self.label.setMovie(movie)
        movie.start()
        self.zhuangtai = self.zhuangtai  # r"./img/zxskd/zxskdzdl.gif"
        # gif加载
        # movie = QMovie(self.zhuangtai)
        # self.label.setMovie(movie)
        # movie.start()
        # 右键菜单声明
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.rightMenuShow)
        print(2)
    # 菜单
    def rightMenuShow(self, position):
        menu = QMenu()
        # 菜单栏
        quitAction1 = menu.addMenu("切换人物方向")
        renwuX1 = quitAction1.addAction("left")
        renwuX2 = quitAction1.addAction("right")
        quitAction2 = menu.addMenu("动作")
        dongzuo3 = quitAction2.addAction("站立状态")
        dongzuo2 = quitAction2.addAction("悬坐状态")
        dongzuo1 = quitAction2.addAction("特殊状态")
        jporcn = menu.addMenu("语言切换")
        cnzh = jporcn.addAction("中文")
        jpzh = jporcn.addAction("日文")
        quitAction3 = menu.addMenu("切换人物")
        mdx = quitAction3.addAction("迷迭香")
        zxskd = quitAction3.addAction("浊心斯卡蒂")
        quitAction0 = menu.addAction("退出")
        action = menu.exec_(self.mapToGlobal(position))
        # 选项效果
        # 人物切换模块
        if action == mdx:
            self.yycnshuzu = mdxshujv.yycnshuzu
            self.yyjpshuzu = mdxshujv.yyjpshuzu
            self.zhuangtai = mdxshujv.zhuangtai
            self.renwul = mdxshujv.mdxrenwul
            self.renwur = mdxshujv.mdxrenwur
            movie = QMovie(self.zhuangtai)
            self.label.setMovie(movie)
            movie.start()
        if action == zxskd:
            self.yycnshuzu = zxskdshujv.yycnshuzu
            self.yyjpshuzu = zxskdshujv.yyjpshuzu
            self.zhuangtai = zxskdshujv.zhuangtai
            self.renwul = zxskdshujv.zxskdrenwul
            self.renwur = zxskdshujv.zxskdrenwur
            movie = QMovie(self.zhuangtai)
            self.label.setMovie(movie)
            movie.start()
        if action == quitAction0:  # 退出
            sys.exit()
        # 人物方向切换模块
        if action == renwuX1:  # 向左
            self.fxleft = True
            self.fxright = False
            for iiii in self.renwur:
                if self.zhuangtai == iiii:
                    sumiiii = self.renwur.index(iiii)
                    movie = QMovie(self.renwul[sumiiii])
                    self.label.setMovie(movie)
                    movie.start()
                    self.zhuangtai = self.renwul[sumiiii]
                    break
        if action == renwuX2:  # 向右
            self.fxleft = False
            self.fxright = True
            for iiii in self.renwul:
                if self.zhuangtai == iiii:
                    sumiiii = self.renwul.index(iiii)
                    movie = QMovie(self.renwur[sumiiii])
                    self.label.setMovie(movie)
                    movie.start()
                    self.zhuangtai = self.renwur[sumiiii]
                    break
        #  语言切换模块
        if action == cnzh:
            self.yycn = True
            self.yyjp = False
        if action == jpzh:
            self.yycn = False
            self.yyjp = True
        #  人物动作切换模块
        if action == dongzuo2:
            if self.fxright == True:
                movie = QMovie(self.renwur[1])
                self.label.setMovie(movie)
                movie.start()
                self.zhuangtai = self.renwur[1]
            elif self.fxleft == True:
                movie = QMovie(self.renwul[1])
                self.label.setMovie(movie)
                movie.start()
                self.zhuangtai = self.renwul[1]
        if action == dongzuo3:
            if self.fxright == True:
                movie = QMovie(self.renwur[0])
                self.label.setMovie(movie)
                movie.start()
                self.zhuangtai = self.renwur[0]
            elif self.fxleft == True:
                movie = QMovie(self.renwul[0])
                self.label.setMovie(movie)
                movie.start()
                self.zhuangtai = self.renwul[0]
        if action == dongzuo1:
            if self.fxright == True:
                movie = QMovie(self.renwur[4])
                self.label.setMovie(movie)
                movie.start()
                self.zhuangtai = self.renwur[4]
            elif self.fxleft == True:
                movie = QMovie(self.renwul[4])
                self.label.setMovie(movie)
                movie.start()
                self.zhuangtai = self.renwul[4]
        print(3)
    # 鼠标按下侦测
    def mousePressEvent(self, event):  # 无边框移动,语音
        if event.button() == Qt.MidButton:
            self.m_flag = True
            self.m_Position = event.globalPos() - self.pos()  # 获取鼠标相对窗口的位置
            event.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))  # 更改鼠标图标
        if event.button() == Qt.LeftButton:
            self.TXFCTF = True
            if self.fxright == True:
                movie = QMovie(self.renwur[3])
                self.label.setMovie(movie)
                self.TXFC = movie.frameCount()
                movie.start()

            elif self.fxleft == True:
                movie = QMovie(self.renwul[3])
                self.label.setMovie(movie)
                self.TXFC = movie.frameCount()
                movie.start()
        print(4)
    # 鼠标按住侦测
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.MidButton and self.m_flag:
            if self.fxright == True:
                movie = QMovie(self.renwur[2])
                self.label.setMovie(movie)
                movie.start()
            elif self.fxleft == True:
                movie = QMovie(self.renwul[2])
                self.label.setMovie(movie)
                movie.start()
            self.move(QMouseEvent.globalPos() - self.m_Position)  # 更改窗口位置
            QMouseEvent.accept()
        print(5)
    # 鼠标放开侦测
    def mouseReleaseEvent(self, QMouseEvent):
        if self.m_flag == True:
            if self.fxright == True:
                movie = QMovie(self.zhuangtai)
                self.label.setMovie(movie)
                movie.start()
            elif self.fxleft == True:
                movie = QMovie(self.zhuangtai)
                self.label.setMovie(movie)
                movie.start()
            self.m_flag = False
            self.setCursor(QCursor(Qt.ArrowCursor))
        print(6)
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
    def yymokuai(self):
        suiji = random.choice(range(0, 10))
        if self.yycn == True:
            self.Yingyue = self.yycnshuzu[suiji]
            self.Yingyue = QtMultimedia.QSound(self.Yingyue)
            self.Yingyue.play()
        if self.yyjp == True:
            self.Yingyue = self.yyjpshuzu[suiji]
            self.Yingyue = QtMultimedia.QSound(self.Yingyue)
            self.Yingyue.play()


app = QApplication(sys.argv)
win = M_Win()
win.show()
sys.exit(app.exec_())
