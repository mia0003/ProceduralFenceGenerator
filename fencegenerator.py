import maya.cmds as cmds
from PySide6 import QtWidgets


def createFence():

    numPosts = 5
    postWidth = 1.5
    postHeight = 7
    postSpacing = 8

    railCount = 3
    railHeight = 0.5
    railDepth = 0.5
    railSpacing = 1.5
    railStartHeight = 2
    railLength = (numPosts - 1) * postSpacing

    for i in range(numPosts):
        cmds.polyCube(w=postWidth, h=postHeight, d=postWidth, name="FencePost"
                      + str(i))
        cmds.move(i * postSpacing, 3, 0)
    for i in range(railCount):
        cmds.polyCube(w=railLength, h=railHeight, d=railDepth, name="Rail" +
                      str(i))
        cmds.move(railLength / 2, railStartHeight + (i * railSpacing), 0)


class FenceGUI(QtWidgets.QWidget):
    def __init__(self):
        super(FenceGUI, self).__init__()
        self.setWindowTitle("Fence Generator")
        layout = QtWidgets.QVBoxLayout()
        self.generatebutton = QtWidgets.QPushButton("Generate Fence")
        layout.addWidget(self.generatebutton)
        self.setLayout(layout)
        self.generatebutton.clicked.connect(createFence)


win = FenceGUI()
win.show()
