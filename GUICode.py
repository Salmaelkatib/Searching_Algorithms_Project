import SecondWindow
from PyQt5 import QtCore, QtGui,QtWidgets
from PyQt5.QtGui import QPixmap
from SecondWindow import Ui_SecondWindow

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000,800)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.Choose_lbl = QtWidgets.QLabel(self.centralwidget)
        self.Choose_lbl.setObjectName("Choose_lbl")
        self.verticalLayout.addWidget(self.Choose_lbl)
        self.Choose_lbl.setFont(QtGui.QFont("Arial", weight=QtGui.QFont.Bold))
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("None")
        self.comboBox.addItem("Bredth First Algorithm")
        self.comboBox.addItem("Depth First Algorithm")
        self.comboBox.addItem("Uniform Cost Algorithm")
        self.comboBox.addItem("Iterative Depeeneing Algorithm")
        self.comboBox.addItem("Greedy Algorithm")
        self.comboBox.addItem("A* Star Algorithm")
        self.verticalLayout.addWidget(self.comboBox)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.Draw_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Draw_btn.setStyleSheet("background-color :black; color :white ")
        self.Draw_btn.setFont(QtGui.QFont("Arial", weight=QtGui.QFont.Bold))
        self.Draw_btn.setObjectName("Draw_btn")
        self.horizontalLayout_4.addWidget(self.Draw_btn)
        self.Enlarge_btn = QtWidgets.QPushButton(self.centralwidget)
        self.Enlarge_btn.setStyleSheet("background-color :black; color :white ")
        self.Enlarge_btn.setFont(QtGui.QFont("Arial", weight=QtGui.QFont.Bold))
        self.Enlarge_btn.setObjectName("Enlarge_btn")
        self.horizontalLayout_4.addWidget(self.Enlarge_btn)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 6, 2, 1, 2)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.AddHeuristic_btn = QtWidgets.QPushButton(self.centralwidget)
        self.AddHeuristic_btn.setObjectName("AddHeuristic_btn")
        self.Heuristic_txt = QtWidgets.QTextEdit(self.centralwidget, placeholderText="Node    Heuristic")
        self.Heuristic_txt.setObjectName("Heuristic_txt")
        self.verticalLayout_5.addWidget(self.AddHeuristic_btn)
        self.AddHeuristic_btn.setStyleSheet("background-color :black; color :white ")
        self.AddHeuristic_btn.setFont(QtGui.QFont("Arial", weight=QtGui.QFont.Bold))
        self.verticalLayout_5.addWidget(self.Heuristic_txt)
        self.verticalLayout_6.addLayout(self.verticalLayout_5)
        self.gridLayout_4.addLayout(self.verticalLayout_6, 4, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_3.addWidget(self.checkBox)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 0, 1, 1, 1)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.Edges_txt=QtWidgets.QTextEdit(self.centralwidget, placeholderText="Added Edges")
        self.Edges_txt.setObjectName("Edge_txt")
        self.verticalLayout_8.addWidget(self.Edges_txt)
        self.gridLayout_4.addLayout(self.verticalLayout_8, 0, 2, 2, 2)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.Start_lbl = QtWidgets.QLabel(self.centralwidget)
        self.Start_lbl.setObjectName("Start_lbl")
        self.Start_lbl.setFont(QtGui.QFont("Arial", weight=QtGui.QFont.Bold))
        self.gridLayout_3.addWidget(self.Start_lbl, 0, 0, 1, 1)
        self.Start_ed = QtWidgets.QLineEdit(self.centralwidget)
        self.Start_ed.setObjectName("Start_ed")
        self.gridLayout_3.addWidget(self.Start_ed, 0, 1, 1, 1)
        self.Goal_lbl = QtWidgets.QLabel(self.centralwidget)
        self.Goal_lbl.setObjectName("Goal_lbl")
        self.Goal_lbl.setFont(QtGui.QFont("Arial", weight=QtGui.QFont.Bold))
        self.gridLayout_3.addWidget(self.Goal_lbl, 1, 0, 1, 1)
        self.Goal_eb = QtWidgets.QLineEdit(self.centralwidget)
        self.Goal_eb.setObjectName("Goal_eb")
        self.gridLayout_3.addWidget(self.Goal_eb, 1, 1, 1, 1)
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.GetPath_btn = QtWidgets.QPushButton(self.centralwidget)
        self.GetPath_btn.setStyleSheet("background-color :black; color :white ")
        self.GetPath_btn.setFont(QtGui.QFont("Arial", weight=QtGui.QFont.Bold))
        self.GetPath_btn.setObjectName("GetPath_btn")
        self.verticalLayout_7.addWidget(self.GetPath_btn)
        self.AddNewGoal_btn = QtWidgets.QPushButton(self.centralwidget)
        self.AddNewGoal_btn.setObjectName("AddNewGoal_btn")
        self.AddNewGoal_btn.setStyleSheet("background-color :black; color :white ")
        self.AddNewGoal_btn.setFont(QtGui.QFont("Arial", weight=QtGui.QFont.Bold))
        self.verticalLayout_7.addWidget(self.AddNewGoal_btn)
        self.Path_output = QtWidgets.QTextBrowser(self.centralwidget)
        self.Path_output.setObjectName("Path_output")
        self.verticalLayout_7.addWidget(self.Path_output)
        self.gridLayout_3.addLayout(self.verticalLayout_7, 2, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 5, 0, 2, 1)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.Heuristic_lbl = QtWidgets.QLabel(self.centralwidget)
        self.Heuristic_lbl.setObjectName("Heuristic_lbl")
        self.Heuristic_lbl.setFont(QtGui.QFont("Arial", weight=QtGui.QFont.Bold))
        self.gridLayout_2.addWidget(self.Heuristic_lbl, 0, 1, 1, 1)
        self.Heuristic_eb = QtWidgets.QLineEdit(self.centralwidget)
        self.Heuristic_eb.setObjectName("Heuristic_eb")
        self.gridLayout_2.addWidget(self.Heuristic_eb, 1, 1, 1, 1)
        self.Node_lbl = QtWidgets.QLabel(self.centralwidget)
        self.Node_lbl.setObjectName("Node_lbl")
        self.Node_lbl.setFont(QtGui.QFont("Arial", weight=QtGui.QFont.Bold))
        self.gridLayout_2.addWidget(self.Node_lbl, 0, 0, 1, 1)
        self.Node_eb = QtWidgets.QLineEdit(self.centralwidget)
        self.Node_eb.setObjectName("Node_eb")
        self.gridLayout_2.addWidget(self.Node_eb, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_2, 3, 0, 1, 1)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.Node1_eb = QtWidgets.QLineEdit(self.centralwidget)
        self.Node1_eb.setObjectName("Node2_eb_2")
        self.gridLayout.addWidget(self.Node1_eb, 1, 0, 1, 1)
        self.Node1_lbl = QtWidgets.QLabel(self.centralwidget)
        self.Node1_lbl.setObjectName("Node1_lbl")
        self.Node1_lbl.setFont(QtGui.QFont("Arial", weight=QtGui.QFont.Bold))
        self.gridLayout.addWidget(self.Node1_lbl, 0, 0, 1, 1)
        self.weight_lbl = QtWidgets.QLabel(self.centralwidget)
        self.weight_lbl.setObjectName("weight_lbl")
        self.weight_lbl.setFont(QtGui.QFont("Arial", weight=QtGui.QFont.Bold))
        self.gridLayout.addWidget(self.weight_lbl, 0, 2, 1, 1)
        self.weight_eb = QtWidgets.QLineEdit(self.centralwidget)
        self.weight_eb.setObjectName("weight_eb")
        self.gridLayout.addWidget(self.weight_eb, 1, 2, 1, 1)
        self.Node2_eb = QtWidgets.QLineEdit(self.centralwidget)
        self.Node2_eb.setObjectName("Node2_eb")
        self.gridLayout.addWidget(self.Node2_eb, 1, 1, 1, 1)
        self.Node2_lbl = QtWidgets.QLabel(self.centralwidget)
        self.Node2_lbl.setFont(QtGui.QFont("Arial", weight=QtGui.QFont.Bold))
        self.Node2_lbl.setObjectName("Node2_lbl")
        self.gridLayout.addWidget(self.Node2_lbl, 0, 1, 1, 1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.AddEdge_btn = QtWidgets.QPushButton(self.centralwidget)
        self.AddEdge_btn.setStyleSheet("background-color :black; color :white ")
        self.AddEdge_btn.setFont(QtGui.QFont("Arial", weight=QtGui.QFont.Bold))
        self.AddEdge_btn.setObjectName("AddEdge_btn")
        self.verticalLayout_3.addWidget(self.AddEdge_btn)
        self.Done_cb = QtWidgets.QCheckBox(self.centralwidget)
        self.Done_cb.setObjectName("Done_cb")
        self.verticalLayout_3.addWidget(self.Done_cb)
        self.gridLayout.addLayout(self.verticalLayout_3, 0, 3, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.Graph_Viewer = QtWidgets.QGraphicsView(self.centralwidget)
        self.Graph_Viewer.setObjectName("Graph_Viewer")
        self.verticalLayout_10.addWidget(self.Graph_Viewer)
        self.gridLayout_4.addLayout(self.verticalLayout_10, 2, 1, 4, 3)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 527, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Searching Algorithms"))
        self.Choose_lbl.setText(_translate("MainWindow", "Choose Search Algorithm"))
        self.Draw_btn.setText(_translate("MainWindow", "Draw"))
        self.Enlarge_btn.setText(_translate("MainWindow", "Enlarge"))
        self.AddHeuristic_btn.setText(_translate("MainWindow", "Enter"))
        self.checkBox.setText(_translate("MainWindow", "Directed Nodes"))
        self.Start_lbl.setText(_translate("MainWindow", "Start Node"))
        self.Goal_lbl.setText(_translate("MainWindow", "Goal Nodes"))
        self.GetPath_btn.setText(_translate("MainWindow", "Get Path"))
        self.Heuristic_lbl.setText(_translate("MainWindow", "Heuristic"))
        self.Node_lbl.setText(_translate("MainWindow", "Node"))
        self.AddHeuristic_btn.setText(_translate("MainWindow", "Add Heuristic"))
        self.Node1_lbl.setText(_translate("MainWindow", "Node 1"))
        self.weight_lbl.setText(_translate("MainWindow", "Weight"))
        self.Node2_lbl.setText(_translate("MainWindow", "Node 2"))
        self.AddEdge_btn.setText(_translate("MainWindow", "Add Edge"))
        self.AddNewGoal_btn.setText(_translate("MainWindow","Add New Goal"))
        self.Done_cb.setText(_translate("MainWindow", "Done"))
        self.Draw_btn.pressed.connect(lambda: self.Graph("Draw"))
        self.Enlarge_btn.pressed.connect(lambda: self.openWindow())


    def openWindow(self):
            self.window=QtWidgets.QMainWindow()
            self.ui = Ui_SecondWindow()
            self.ui.setupUi(self.window)
            self.window.show()



    def Graph(self, x):
            scene = QtWidgets.QGraphicsScene(self)
            pixmap = QPixmap("img.png")
            item = QtWidgets.QGraphicsPixmapItem(pixmap)
            if x == "Draw":
                scene.addItem(item)
                self.Graph_Viewer.setScene(scene)
                self.Graph_Viewer.fitInView(item)
                self.Done_cb.setEnabled(False)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
