newchain = cmds.ls (sl=True, type = "joint")

oldcircle=None



for obj in newchain:
    cmds.select(clear=True)
    newzerogroup = cmds.group(em=True, n="ZERO_%s"%obj)
    temporalconstrain = cmds.parentConstraint (obj, newzerogroup,mo=0)
    cmds.delete(temporalconstrain)
    newcircle=cmds.circle( nr=(1, 0, 0), c=(0, 0, 0), r=10, n="%s_CON"%obj)
    cmds.parent(newcircle, newzerogroup, r=True)
    cmds.parentConstraint(newcircle,obj,mo=0,w=1)
    cmds.select(obj)
    if oldcircle:
        parentobj = cmds.pickWalk(d='up')
        #parentobjectname = cmds.attributeName(parentobj)
        parentcirclename = "%s_CON"%parentobj
        parentcirclename = parentcirclename.replace("[","")
        parentcirclename = parentcirclename.replace("]","")
        parentcirclename = parentcirclename.replace("'","")
        parentcircle = cmds.select(parentcirclename)
        cmds.parent(newzerogroup,parentcircle)
        oldcircle = newcircle
        continue
    else:
        oldcircle = newcircle
        continue