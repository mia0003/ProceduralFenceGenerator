import maya.cmds as cmds


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


createFence()
