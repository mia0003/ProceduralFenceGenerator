import maya.cmds as cmds
from PySide6 import QtWidgets


def createFence(numPosts, railCount, postHeight, postWidth, postSpacing):

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

        self.postlabel = QtWidgets.QLabel("Number of Posts")
        self.postSpinBox = QtWidgets.QSpinBox()
        self.postSpinBox.setValue(5)

        self.railLabel = QtWidgets.QLabel("Number of  Rails")
        self.railSpinBox = QtWidgets.QSpinBox()
        self.railSpinBox.setValue(3)

        self.postHeightLabel = QtWidgets.QLabel("Post Height")
        self.postHeightSpinBox = QtWidgets.QSpinBox()
        self.postHeightSpinBox.setValue(7)

        self.postWidthLabel = QtWidgets.QLabel("Post Width")
        self.postWidthSpinBox = QtWidgets.QSpinBox()
        self.postWidthSpinBox.setValue(1.5)

        self.postSpacingLabel = QtWidgets.QLabel("Post Spacing")
        self.postSpacingSpinBox = QtWidgets.QSpinBox()
        self.postSpacingSpinBox.setValue(8)

        self.generatebutton = QtWidgets.QPushButton("Generate Fence")

        layout.addWidget(self.postlabel)
        layout.addWidget(self.postSpinBox)

        layout.addWidget(self.railLabel)
        layout.addWidget(self.railSpinBox)

        layout.addWidget(self.postHeightLabel)
        layout.addWidget(self.postHeightSpinBox)

        layout.addWidget(self.postWidthLabel)
        layout.addWidget(self.postWidthSpinBox)

        layout.addWidget(self.postSpacingLabel)
        layout.addWidget(self.postSpacingSpinBox)

        layout.addWidget(self.generatebutton)
        self.setLayout(layout)
        self.generatebutton.clicked.connect(self.generateFence)

    def generateFence(self):
        numPosts = self.postSpinBox.value()
        railCount = self.railSpinBox.value()
        postHeight = self.postHeightSpinBox.value()
        postWidth = self.postWidthSpinBox.value()
        postSpacing = self.postSpacingSpinBox.value()
        createFence(numPosts, railCount, postHeight, postWidth, postSpacing)


win = FenceGUI()
win.show()
