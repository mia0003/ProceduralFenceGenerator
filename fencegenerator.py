import maya.cmds as cmds
from PySide6 import QtWidgets


def createPosts(numPosts, postWidth, postHeight, postSpacing, fenceParts):
    for i in range(numPosts):
        post = cmds.polyCube(w=postWidth, h=postHeight, d=postWidth,
                             name="FencePost" + str(i))[0]
        cmds.polyBevel(post, offset=0.15)
        cmds.move(i * postSpacing, postHeight / 2, 0)
        fenceParts.append(post)


def createRails(railCount, railLength, railHeight, railDepth, railStartHeight,
                railSpacing, fenceParts):
    for i in range(railCount):
        rail = cmds.polyCube(w=railLength, h=railHeight, d=railDepth,
                             name="Rail" + str(i))[0]
        cmds.polyBevel(rail, offset=0.1)
        cmds.move(railLength / 2, railStartHeight + (i * railSpacing), 0)
        fenceParts.append(rail)


def createFence(numPosts, railCount, postHeight, postWidth, postSpacing,
                fenceStyle):
    if cmds.objExists("Fence_GRP"):
        cmds.delete("Fence_GRP")

    railHeight = 0.5

    if fenceStyle == "Decorative":
        postWidth *= 0.75
        railDepth = 0.25
    elif fenceStyle == "Heavy Duty":
        postWidth *= 1.5
        railDepth = 1.0
    else:
        railDepth = 0.5

    fenceParts = []

    railLength = (numPosts - 1) * postSpacing

    railStartHeight = postHeight * 0.2
    topRailHeight = postHeight * 0.7

    if railCount > 1:
        railSpacing = (topRailHeight - railStartHeight) / (railCount - 1)
    else:
        railSpacing = 0

    createPosts(numPosts, postWidth, postHeight, postSpacing, fenceParts)
    createRails(railCount, railLength, railHeight, railDepth, railStartHeight,
                railSpacing, fenceParts)

    cmds.group(fenceParts, name="Fence_GRP")


class FenceGUI(QtWidgets.QWidget):
    def __init__(self):
        super(FenceGUI, self).__init__()
        self.setWindowTitle("Fence Generator")
        self.setFixedSize(350, 400)

        self.createWidgets()

    def createWidgets(self):
        layout = QtWidgets.QVBoxLayout()

        self.postLabel = QtWidgets.QLabel("Number of Posts (2-20)")
        self.postSpinBox = QtWidgets.QSpinBox()
        self.postSpinBox.setMinimum(2)
        self.postSpinBox.setMaximum(20)
        self.postSpinBox.setValue(5)

        self.railLabel = QtWidgets.QLabel("Number of  Rails (1-4)")
        self.railSpinBox = QtWidgets.QSpinBox()
        self.railSpinBox.setMinimum(1)
        self.railSpinBox.setMaximum(4)
        self.railSpinBox.setValue(3)

        self.styleLabel = QtWidgets.QLabel("Fence Style")
        self.styleComboBox = QtWidgets.QComboBox()

        self.styleComboBox.addItem("Standard")
        self.styleComboBox.addItem("Decorative")
        self.styleComboBox.addItem("Heavy Duty")

        self.postHeightLabel = QtWidgets.QLabel("Post Height (4-15)")
        self.postHeightSpinBox = QtWidgets.QSpinBox()
        self.postHeightSpinBox.setMinimum(4)
        self.postHeightSpinBox.setMaximum(15)
        self.postHeightSpinBox.setValue(7)

        self.postWidthLabel = QtWidgets.QLabel("Post Width (0.5-5)")
        self.postWidthSpinBox = QtWidgets.QDoubleSpinBox()
        self.postWidthSpinBox.setMinimum(0.5)
        self.postWidthSpinBox.setMaximum(5.0)
        self.postWidthSpinBox.setValue(1.5)

        self.postSpacingLabel = QtWidgets.QLabel("Post Spacing (4-20)")
        self.postSpacingSpinBox = QtWidgets.QSpinBox()
        self.postSpacingSpinBox.setMinimum(4)
        self.postSpacingSpinBox.setMaximum(20)
        self.postSpacingSpinBox.setValue(8)

        self.generatebutton = QtWidgets.QPushButton("Generate Fence")

        layout.addWidget(self.postLabel)
        layout.addWidget(self.postSpinBox)

        layout.addWidget(self.railLabel)
        layout.addWidget(self.railSpinBox)

        layout.addWidget(self.styleLabel)
        layout.addWidget(self.styleComboBox)

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
        fenceStyle = self.styleComboBox.currentText()
        postHeight = self.postHeightSpinBox.value()
        postWidth = self.postWidthSpinBox.value()
        postSpacing = self.postSpacingSpinBox.value()
        createFence(numPosts, railCount, postHeight, postWidth, postSpacing,
                    fenceStyle)


win = FenceGUI()
win.show()
