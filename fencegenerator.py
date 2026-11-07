import maya.cmds as cmds


def createFencePost():
    for i in range(5):
        cmds.polyCube(w=1, h=6, d=1, name="FencePost" + str(i))
        cmds.move(i * 8, 3, 0)
    cmds.polyCube(w=32, h=0.5, d=0.5, name="RailTop")
    cmds.move(16, 5, 0)
    cmds.polyCube(w=32, h=0.5, d=0.5, name="RailMiddle")
    cmds.move(16, 3.5, 0)
    cmds.polyCube(w=32, h=0.5, d=0.5, name="RailBottom")
    cmds.move(16, 2, 0)


createFencePost()
