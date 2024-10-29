import random
import sys
import time

from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QMovie, QCursor, QMouseEvent
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QMenu, qApp

from role import mdxshujv
from role import zxskdshujv


class M_Win(QWidget):

    def __init__(self):
        super().__init__()

        #  参数组
        self.label = QLabel(self)
        # 窗体坐标
        self.y = 610
        self.x = 1560
        # 人物编号
        self.ren = 1
        # 标签flag
        # 人物方向标签
        self.flag1 = 0
        # 鼠标左键标签
        self.flag2 = False
        self.flag3 = False

        #  动作模块
        self.image = QLabel(self)

        #  初始状态
        self.init_RenWu()
        self.petNormalAction()
        self.petNormalAction3()

    #  初始状态
    def init_RenWu(self):
        # 人物模型
        self.renwumoxing = zxskdshujv
        # 人物状态
        self.zhuangtai = 0
        # 人物方向，左true，右false
        self.renwufangxiang = True
        self.renwul = self.renwumoxing.renwul
        self.renwur = self.renwumoxing.renwur
        #  语言模块
        self.yycn = True
        self.yycnshuzu = self.renwumoxing.yycnshuzu

        self.yyjp = False
        self.yyjpshuzu = self.renwumoxing.yyjpshuzu

        #  调用窗口
        self.M_ui()

    # 窗口
    def M_ui(self):
        self.resize(300, 300)  # 程序窗口大小
        self.move(self.x, self.y)  # 程序窗口位置
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint | Qt.SplashScreen)  # 置顶，去掉边框，隐藏任务栏
        self.setAttribute(Qt.WA_TranslucentBackground)  # 窗体背景透明
        # 初始化
        movie = QMovie(self.renwul[self.zhuangtai])  # r"./img/zxskd/zxskdzdl.gif"
        self.label.setMovie(movie)
        movie.start()
        # 右键菜单声明
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.RightMenuShow)

        # 人物正常待机随机方向

    def petNormalAction(self):
        # 每隔一段时间换个方向
        # 定时器设置
        self.timer1 = QTimer()
        # 时间到了自动执行
        self.timer1.timeout.connect(self.petNormalAction2)
        self.timer1.timeout.connect(self.Renwudongzuo)
        # 动作时间切换设置,每5分钟换一次
        self.timer1.start(300000)


    def petNormalAction2(self):
        self.renwufangxiang = not self.renwufangxiang

    # 人物正常待机随机动作
    def petNormalAction3(self):
        # 每隔一段时间随机动作
        # 定时器设置
        self.timer2 = QTimer()
        # 时间到了自动执行
        self.timer2.timeout.connect(self.petNormalAction4)
        # 动作时间切换设置,每10分钟换一次
        self.timer2.start(360000)

    def petNormalAction4(self):
        random_list = [0, 2]
        random_list2 = random.choice(random_list)
        if self.renwufangxiang:
            movie = QMovie(self.renwul[random_list2])
        else:
            movie = QMovie(self.renwur[random_list2])
        self.zhuangtai = random_list2
        # 将动画添加到label中
        self.label.setMovie(movie)
        # 开始播放动画
        movie.start()
        # 宠物状态设置为正常待机
        self.flag1 = 0

    # 右键菜单交互菜单
    def RightMenuShow(self, position):
        menu = QMenu()
        # 菜单栏
        # 动作菜单
        quitAction2 = menu.addMenu("动作")
        # 动作子菜单
        dongzuo1 = quitAction2.addAction("站立状态")
        dongzuo2 = quitAction2.addAction("悬坐状态")
        dongzuo3 = quitAction2.addAction("战斗状态")
        # 人物菜单
        quitAction3 = menu.addMenu("切换人物")
        # 人物子菜单
        mdx = quitAction3.addAction("迷迭香")
        zxskd = quitAction3.addAction("浊心斯卡蒂")
        quitAction0 = menu.addAction("退出")
        action = menu.exec_(self.mapToGlobal(position))
        # 选项效果
        # 人物切换模块
        if action == mdx:
            self.Renwuqiehuan(mdxshujv)
        elif action == zxskd:
            self.Renwuqiehuan(zxskdshujv)

        if action == dongzuo1:
            self.Renwudongzuoqihuan(0)
        elif action == dongzuo2:
            self.Renwudongzuoqihuan(1)
        elif action == dongzuo3:
            self.Renwudongzuoqihuan(4)

        # 退出
        if action == quitAction0:  # 退出
            self.Tuichu()

    # 退出
    def Tuichu(self):
        self.close()
        sys.exit()

    #  人物动作切换模块
    def Renwudongzuo(self):
        # flag1记录宠物状态，宠物状态为0时，代表正常待机
        if not self.flag1:
            # 读取特殊状态图片路径 flag1 == 0
            if self.renwufangxiang:
                movie = QMovie(self.renwul[self.zhuangtai])
            else:
                movie = QMovie(self.renwur[self.zhuangtai])
            # 将动画添加到label中
            self.label.setMovie(movie)
            # 开始播放动画
            movie.start()
            self.flag1 = 0
        # flag1不为0，转为切换特有的动作，实现宠物的点击反馈
        # 这里可以通过else-if语句往下拓展做更多的交互功能
        if (self.flag1 == 1):
            # 读取特殊状态图片路径 flag1 == 1
            if self.renwufangxiang:
                movie = QMovie(self.renwul[1])
            else:
                movie = QMovie(self.renwur[1])
            # 将动画添加到label中
            self.label.setMovie(movie)
            # 开始播放动画
            movie.start()
            # 宠物状态设置为正常待机
            self.flag1 = 0


    #  菜单人物动作切换模块
    def Renwudongzuoqihuan(self, dongzuobianhao):
        # 切换人物右动作
        if self.renwufangxiang:
            movie = QMovie(self.renwul[dongzuobianhao])
            self.label.setMovie(movie)
            movie.start()
            self.zhuangtai = dongzuobianhao
        # 切换人物左动作
        else:
            movie = QMovie(self.renwur[dongzuobianhao])
            self.label.setMovie(movie)
            movie.start()
            self.zhuangtai = dongzuobianhao

    # 载入人物数据，进行人物切换
    def Renwuqiehuan(self, mdxshujv):
        self.renwumoxing = mdxshujv
        self.yycnshuzu = self.renwumoxing.yycnshuzu
        self.yyjpshuzu = self.renwumoxing.yyjpshuzu
        self.renwul = self.renwumoxing.renwul
        self.renwur = self.renwumoxing.renwur
        if self.renwufangxiang:
            movie = QMovie(self.renwul[self.zhuangtai])
        else:
            movie = QMovie(self.renwur[self.zhuangtai])
        self.label.setMovie(movie)
        movie.start()

    # 鼠标左键按下时, 宠物将和鼠标位置绑定
    def mousePressEvent(self, event):  # 无边框移动,语音

        if event.button() == Qt.LeftButton:
            self.flag2 = True
        # globalPos() 事件触发点相对于桌面的位置
        # pos() 程序相对于桌面左上角的位置，实际是窗口的左上角坐标
        # self.mouse_drag_pos = event.globalPosition().toPoint() - self.pos()
        # event.accept()
        # pyqt5鼠标位置和相对窗口位置做差值
        self.mouse_pos = self.mapToGlobal(event.pos()) - self.pos()
        event.accept()
        # 拖动时鼠标图形的设置
        self.setCursor(QCursor(Qt.OpenHandCursor))

        # 鼠标点击时效果
        self.flag3 = self.zhuangtai
        self.zhuangtai = 3
        if self.renwufangxiang:
            movie = QMovie(self.renwul[self.zhuangtai])
        else:
            movie = QMovie(self.renwur[self.zhuangtai])
        self.label.setMovie(movie)
        movie.start()
        self.timer3 = QTimer()
        # 时间到了自动执行
        self.timer3.timeout.connect(self.Mousetime)
        # 动作时间切换设置
        self.timer3.start(1500)

    # 鼠标移动时调用，实现宠物随鼠标移动
    def mouseMoveEvent(self, event):
        # 更改人物状态为点击
        self.flag1 = 1
        # 即刻加载宠物点击动画
        self.Renwudongzuo()
        # 如果鼠标左键按下，且处于绑定状态
        if Qt.LeftButton and self.flag2:
            # 宠物随鼠标进行移动，鼠标位置和差值
            self.move(self.mapToGlobal(event.pos()) - self.mouse_pos)
            # self.move(self.x, self.y)
            # 设置窗体新的位置
        event.accept()

    # 鼠标释放调用，取消绑定
    def mouseReleaseEvent(self, event):
        self.flag2 = False
        # 更改人物状态为点击
        self.flag1 = 0
        # 即刻加载宠物点击动画
        self.Renwudongzuo()
        # 鼠标图形设置为箭头
        self.setCursor(QCursor(Qt.ArrowCursor))
        # self.timer.start()

    # 鼠标移进时调用
    def enterEvent(self, event):
        # 设置鼠标形状 Qt.ClosedHandCursor   非指向手
        self.setCursor(Qt.ClosedHandCursor)

    # 鼠标点击时动作计时器执行效果
    def Mousetime(self):
        self.zhuangtai = self.flag3
        if self.renwufangxiang:
            movie = QMovie(self.renwul[self.zhuangtai])
        else:
            movie = QMovie(self.renwur[self.zhuangtai])
        self.label.setMovie(movie)
        movie.start()


app = QApplication(sys.argv)
win = M_Win()
win.show()
sys.exit(app.exec())
