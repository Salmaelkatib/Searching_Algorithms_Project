import sys
import os
from PyQt5 import QtWidgets
from GUICode import Ui_MainWindow
import networkx as nx
import matplotlib.pyplot as plt
import Algos

arr=[]

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    EXIT_CODE_REBOOT = -12345678

    def CheckDirected(self):
     if self.checkBox.isChecked():
         return True
     else:
         return False

    def __init__(self):
      QtWidgets.QMainWindow.__init__(self)
      Ui_MainWindow.__init__(self)

      self.setupUi(self)
      self.initwidgets()
      self.comboBox.currentIndexChanged.connect(self.ComboboxSelected)
      self.AddEdge_btn.clicked.connect(self.AddEdge)
      self.AddHeuristic_btn.clicked.connect(self.AddHeuristic)
      self.Done_cb.clicked.connect(self.Input_Graph_Done)
      self.AddNewGoal_btn.clicked.connect(self.AddNewGoals)
      self.GetPath_btn.clicked.connect(self.GetPath)

    def AddNewGoals(self):
        a = self.Goal_eb.text()
        arr.append(a)
        self.Goal_eb.clear()


    def initwidgets(self):
        self.Node_lbl.setEnabled(False)
        self.Node_eb.setEnabled(False)
        self.Heuristic_lbl.setEnabled(False)
        self.Heuristic_eb.setEnabled(False)
        self.AddHeuristic_btn.setEnabled(False)
        self.AddHeuristic_btn.setEnabled(False)
        self.Start_lbl.setEnabled(False)
        self.Start_ed.setEnabled(False)
        self.Goal_lbl.setEnabled(False)
        self.Goal_eb.setEnabled(False)
        self.weight_lbl.setHidden(True)
        self.weight_eb.setHidden(True)
        self.AddEdge_btn.setEnabled(False)
        self.checkBox.setEnabled(False)
        self.Draw_btn.setEnabled(False)
        self.Done_cb.setEnabled(False)

    def ComboboxSelected(self):
        selected=self.comboBox.currentIndex()
        if selected==0:   #None
            self.Node_lbl.setEnabled(False)
            self.Node_eb.setEnabled(False)
            self.Heuristic_lbl.setEnabled(False)
            self.Heuristic_eb.setEnabled(False)
            self.AddHeuristic_btn.setEnabled(False)
            self.AddHeuristic_btn.setEnabled(False)
            self.Start_lbl.setEnabled(False)
            self.Start_ed.setEnabled(False)
            self.Goal_lbl.setEnabled(False)
            self.Goal_eb.setEnabled(False)
            self.weight_lbl.setHidden(True)
            self.weight_eb.setHidden(True)
            self.AddEdge_btn.setEnabled(False)
            self.checkBox.setEnabled(False)
            self.Draw_btn.setEnabled(False)
            self.Done_cb.setEnabled(False)
        else:
            self.Start_lbl.setEnabled(True)
            self.Start_ed.setEnabled(True)
            self.Goal_lbl.setEnabled(True)
            self.Goal_eb.setEnabled(True)
            self.AddEdge_btn.setEnabled(True)
            self.checkBox.setEnabled(True)
            self.Done_cb.setEnabled(True)

            if selected==1:      #BFS
             self.Node_eb.setEnabled(False)
             self.Node_lbl.setEnabled(False)
             self.Heuristic_lbl.setEnabled(False)
             self.Heuristic_eb.setEnabled(False)
             self.AddHeuristic_btn.setEnabled(False)
             self.AddHeuristic_btn.setEnabled(False)
             self.weight_lbl.setHidden(True)
             self.weight_eb.setHidden(True)
            if selected==2:     #DFS
             self.Heuristic_lbl.setEnabled(False)
             self.Heuristic_eb.setEnabled(False)
             self.AddHeuristic_btn.setEnabled(False)
             self.AddHeuristic_btn.setEnabled(False)
             self.weight_lbl.setHidden(True)
             self.weight_eb.setHidden(True)
            if selected==3:   #UCF
             self.Heuristic_lbl.setEnabled(False)
             self.Heuristic_eb.setEnabled(False)
             self.AddHeuristic_btn.setEnabled(False)
             self.AddHeuristic_btn.setEnabled(False)
             self.weight_lbl.setHidden(False)
             self.weight_eb.setHidden(False)
            if selected==4:   #Iterative Deepining
             self.Node_lbl.setEnabled(False)
             self.Node_eb.setEnabled(False)
             self.Heuristic_lbl.setEnabled(False)
             self.Heuristic_eb.setEnabled(False)
             self.AddHeuristic_btn.setEnabled(False)
             self.AddHeuristic_btn.setEnabled(False)
             self.weight_lbl.setHidden(True)
             self.weight_eb.setHidden(True)
            if selected==5:     #Greedy
             self.Node_lbl.setEnabled(True)
             self.Node_eb.setEnabled(True)
             self.Heuristic_lbl.setEnabled(True)
             self.Heuristic_eb.setEnabled(True)
             self.AddHeuristic_btn.setEnabled(True)
             self.AddHeuristic_btn.setEnabled(True)
             self.weight_lbl.setHidden(True)
             self.weight_eb.setHidden(True)
            if selected==6:     #A star
             self.Node_lbl.setEnabled(True)
             self.Node_eb.setEnabled(True)
             self.Heuristic_lbl.setEnabled(True)
             self.Heuristic_eb.setEnabled(True)
             self.AddHeuristic_btn.setEnabled(True)
             self.AddHeuristic_btn.setEnabled(True)
             self.weight_lbl.setHidden(False)
             self.weight_eb.setHidden(False)


    G=nx.DiGraph()
    graphid = Algos.Graph(directed=True)
    graphi = Algos.Graph(directed=False)


    def Input_Graph_Done(self):
        if self.Done_cb.isChecked:
            self.Draw_btn.setEnabled(True)
            self.Draw()
            self.AddEdge_btn.setEnabled(False)
        else:
            self.Draw_btn.setEnabled(False)

    def AddEdge(self):
        if self.CheckDirected():
         self.Edges_txt.append(self.Node1_eb.text() + "->" + self.Node2_eb.text())
         self.G.add_edge(self.Node1_eb.text(),self.Node2_eb.text(),weight=self.weight_eb.text(),color="black")
         selected=self.comboBox.currentIndex()
         if selected==1:
             self.graphid.add_edge(self.Node1_eb.text(),self.Node2_eb.text())
         elif selected==2:
             self.graphid.add_edge(self.Node1_eb.text(), self.Node2_eb.text())
         elif selected==3:
             self.graphid.add_edge_ucs(self.Node1_eb.text(),self.Node2_eb.text(),int(self.weight_eb.text()))
         elif selected==4:
             self.graphid.add_edge(self.Node1_eb.text(), self.Node2_eb.text())
         elif selected==5:
             self.graphid.add_edge_g_A(self.Node1_eb.text(), self.Node2_eb.text())
         elif selected==6:
             self.graphid.add_edge_g_A(self.Node1_eb.text(), self.Node2_eb.text(),int(self.weight_eb.text()))
         elif selected==7:
             self.graphid.add_edge(self.Node1_eb.text(), self.Node2_eb.text())
         self.Node1_eb.clear()
         self.Node2_eb.clear()
         self.weight_eb.clear()
        else:
         self.Edges_txt.append(self.Node1_eb.text() + "-" + self.Node2_eb.text())
         self.G.add_edge(self.Node1_eb.text(), self.Node2_eb.text(), weight=self.weight_eb.text(), color="black")
         selected=self.comboBox.currentIndex()
         if selected == 1:
             self.graphi.add_edge(self.Node1_eb.text(), self.Node2_eb.text())
         elif selected == 2:
             self.graphi.add_edge(self.Node1_eb.text(), self.Node2_eb.text())
         elif selected == 3:
             self.graphi.add_edge_ucs(self.Node1_eb.text(), self.Node2_eb.text(), int(self.weight_eb.text()))
         elif selected == 4:
             self.graphi.add_edge(self.Node1_eb.text(), self.Node2_eb.text())
         elif selected == 5:
             self.graphi.add_edge_g_A(self.Node1_eb.text(), self.Node2_eb.text())
         elif selected == 6:
             self.graphi.add_edge_g_A(self.Node1_eb.text(), self.Node2_eb.text(), int(self.weight_eb.text()))
         elif selected==7:
             self.graphi.add_edge(self.Node1_eb.text(), self.Node2_eb.text())
        self.Node1_eb.clear()
        self.Node2_eb.clear()
        self.weight_eb.clear()

    #Store Nodes heuristics in dictionary : value=Nodes , key=heuristic
    Heursistic_set=dict()
    def AddHeuristic(self):
        H=int(self.Heuristic_eb.text())
        N=self.Node_eb.text()
        self.Heursistic_set.update({N:H})
        if self.CheckDirected():
          self.graphid.set_huristics(self.Heursistic_set)
        else:
            self.graphi.set_huristics(self.Heursistic_set)
        self.Heuristic_txt.append("Node: "+self.Node_eb.text() +"    " +"Heuristic:" + self.Heuristic_eb.text())
        self.Node_eb.clear()
        self.Heuristic_eb.clear()

    def Create_path(self,came_from,goal):
        parent = came_from[goal]
        if parent:
            self.Create_path(came_from, parent)
        else:
            self.Path_output.insertPlainText(goal);
            return
        self.Path_output.insertPlainText(' => ')
        self.Path_output.insertPlainText(goal)


    def GetPath(self):
        s = self.Start_ed.text()
        a = self.Goal_eb.text()
        arr.append(a)
        selected = self.comboBox.currentIndex()
        if self.CheckDirected():
            if selected == 1:
                traced_path, goal,visited = self.graphid.breadth_first_search(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path, goal)
                self.Path_output.append("Visited Nodes:")
                for i in visited:
                    self.Path_output.insertPlainText(str(i) + " ")
            elif selected == 2:
                traced_path, goal ,visited= self.graphid.deapth_first_search(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path, goal)
                self.Path_output.append("Visited Nodes:")
                for i in visited:
                    self.Path_output.insertPlainText(str(i) + " ")
            elif selected == 3:
                traced_path, cost, goal ,visited = self.graphid.uniform_cost_search(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path,goal)
                self.Path_output.setText( ' cost: ' + str(cost));self.Create_path(traced_path, goal)
                self.Path_output.append("Visited Nodes:")
                for i in visited:
                    self.Path_output.insertPlainText(str(i) + " ")
            elif selected == 4:
                traced_path, goal,visited = self.graphid.iterative_deepening_dfs(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path, goal)
                self.Path_output.append("Visited Nodes:")
                for i in visited:
                    self.Path_output.insertPlainText(str(i) + " ")
            elif selected == 5:
                traced_path, cost, goal,visited = self.graphid.greedy_search(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path,goal)
                self.Path_output.append("Visited Nodes:")
                for i in visited:
                    self.Path_output.insertPlainText(str(i) + " ")
            elif selected == 6:
                traced_path, cost, goal,visited = self.graphid.aStarSearch(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path,goal)
                self.Path_output.append("Visited Nodes:")
                for i in visited:
                    self.Path_output.insertPlainText(str(i) + " ")

        else:
            if selected == 1:
                traced_path, goal ,visited= self.graphi.breadth_first_search(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path, goal)
                self.Path_output.append("Visited Nodes:")
                for i in visited:
                    self.Path_output.insertPlainText(str(i) + " ")
            elif selected == 2:
                traced_path,goal,visited= self.graphi.deapth_first_search(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path, goal)
                self.Path_output.append("Visited Nodes:")
                for i in visited:
                    self.Path_output.insertPlainText(str(i)+" ")
            elif selected == 3:
                traced_path, cost, goal,visited = self.graphi.uniform_cost_search(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path, goal)
                self.Path_output.insertPlainText(' cost: ' + str(cost))
                self.Path_output.append("Visited Nodes:")
                for i in visited:
                    self.Path_output.insertPlainText(str(i) + " ")
            elif selected==4:
                traced_path, goal ,visited= self.graphi.iterative_deepening_dfs(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path, goal)
                self.Path_output.append("Visited Nodes:")
                for i in visited:
                    self.Path_output.insertPlainText(str(i) + " ")
            elif selected == 5:
                traced_path, cost, goal ,visited= self.graphi.greedy_search(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path,goal)
                self.Path_output.append("Visited Nodes:")
                for i in visited:
                    self.Path_output.insertPlainText(str(i) + " ")
            elif selected == 6:
                traced_path, cost, goal ,visited= self.graphi.aStarSearch(s, arr)
                if (traced_path): self.Path_output.setText(""); self.Create_path(traced_path, goal)
                self.Path_output.append("Visited Nodes:")
                for i in visited:
                    self.Path_output.insertPlainText(str(i) + " ")


    def Draw(self):
        selected=self.comboBox.currentIndex()
        if selected==1:
            self.State = self.CheckDirected()
            nx.draw_circular(self.G,with_labels=True,arrows=self.State)
            plt.savefig("img.png")
        elif selected==2:
            self.State = self.CheckDirected()
            nx.draw_circular(self.G,with_labels=True, arrows=self.State)
            plt.savefig("img.png")
        elif selected==3:
            self.State = self.CheckDirected()
            pos=nx.spring_layout(self.G)
            weights=nx.get_edge_attributes(self.G, 'weight')
            nx.draw_networkx(self.G,pos, with_labels=True, arrows=self.State)
            nx.draw_networkx_edge_labels(self.G,pos,edge_labels=weights)
            plt.savefig("img.png")
        elif selected==4:
            self.State = self.CheckDirected()
            nx.draw_circular(self.G, with_labels=True, arrows=self.State)
            plt.savefig("img.png")
        elif selected==5:
            self.State = self.CheckDirected()
            nx.draw_circular(self.G, with_labels=True, arrows=self.State)
            plt.savefig("img.png")
        elif  selected==6:
            self.State = self.CheckDirected()
            pos = nx.spring_layout(self.G)
            weights = nx.get_edge_attributes(self.G, 'weight')
            nx.draw_networkx(self.G, pos, with_labels=True, arrows=self.State)
            nx.draw_networkx_edge_labels(self.G, pos, edge_labels=weights)
            plt.savefig("img.png")
        elif  selected==7:
            self.State = self.CheckDirected()
            nx.draw_circular(self.G, with_labels=True, arrows=self.State)
            plt.savefig("img.png")


if __name__ == "__main__":
    currentExitCode = MainWindow.EXIT_CODE_REBOOT
    while currentExitCode == MainWindow.EXIT_CODE_REBOOT:
        app = QtWidgets.QApplication(sys.argv)
        window = MainWindow()
        window.show()
        currentExitCode = app.exec_()
        app = None





