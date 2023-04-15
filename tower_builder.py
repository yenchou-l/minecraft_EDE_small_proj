def world2List(aPos):
    aPos = str(aPos).split(" ")
    rsltPos = []
    for i in range(len(aPos)):
        rsltPos.append(int(aPos[i]))
    return rsltPos

def towerBuilder(startPos, width, length, floorNum, floorThick, floorHeight, material, ceilingMat):
    startPosList = world2List(startPos)
    for f in range(floorNum):
        endPosX = startPosList[0] + width -1
        endPosY = startPosList[1] + (floorHeight+floorThick) -1
        endPosZ = startPosList[2] + length -1
        ceilingStartPosY = startPosList[1] + floorHeight
        blocks.fill(material, world(startPosList[0], startPosList[1], startPosList[2]), world(endPosX, endPosY, endPosZ), FillOperation.DESTROY)
        blocks.fill(AIR, world(startPosList[0]+1, startPosList[1], startPosList[2]+1), world(endPosX-1, endPosY, endPosZ-1), FillOperation.REPLACE)
        blocks.fill(ceilingMat, world(startPosList[0]+1, ceilingStartPosY, startPosList[2]+1), world(endPosX-1, endPosY, endPosZ-1), FillOperation.DESTROY)
        startPosList[1] = endPosY + 1
        if f == floorNum -1 :
            blocks.fill(material, world(startPosList[0], startPosList[1], startPosList[2]), world(startPosList[0] + width -1, startPosList[1], startPosList[2] + length -1), FillOperation.DESTROY)
            blocks.fill(AIR, world(startPosList[0]+1, startPosList[1], startPosList[2]+1), world(startPosList[0] + width -2, startPosList[1], startPosList[2] + length -2), FillOperation.REPLACE)

curPos = positions.add(player.position(), world(1,0,1))
towerBuilder(curPos, 5, 7, 8, 1, 4, STONE_BRICKS, PLANKS_OAK)