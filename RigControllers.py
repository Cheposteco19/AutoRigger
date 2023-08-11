from maya import cmds

#Get chain of selected skeleton
newchain = cmds.ls (sl=True, type = "joint")

#Set a prevous null controller
oldcircle=None

for obj in newchain:
    
    #Create the zero group as a parent constrain
    cmds.select(clear=True)
    newzerogroup = cmds.group(em=True, n="ZERO_%s"%obj)
    temporalconstrain = cmds.parentConstraint (obj, newzerogroup,mo=0)
    cmds.delete(temporalconstrain)
    
    #Create the contoler parented to the zero group and constrained to the joint
    newcircle=cmds.circle( nr=(1, 0, 0), c=(0, 0, 0), r=10, n="%s_CON"%obj)
    cmds.parent(newcircle, newzerogroup, r=True)
    cmds.parentConstraint(newcircle,obj,mo=0,w=1)
    cmds.select(obj)
    if oldcircle:
        #Naming convention
        parentobj = cmds.pickWalk(d='up')
        parentcirclename = "%s_CON"%parentobj
        parentcirclename = parentcirclename.replace("[","")
        parentcirclename = parentcirclename.replace("]","")
        parentcirclename = parentcirclename.replace("'","")
        
        #Parent zero group to the correct controller
        parentcircle = cmds.select(parentcirclename)
        cmds.parent(newzerogroup,parentcircle)
        
    #Set old circle
    oldcircle = newcircle