import maya.cmds as cmds


def createFencePost():
    cmds.polyCube(w=1, h=6, d=1, name="FencePost")


createFencePost()
