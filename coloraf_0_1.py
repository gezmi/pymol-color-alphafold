from pymol import cmd


def coloraf(selection="all"):

    """
    AUTHOR
    Christian Balbin

    DESCRIPTION
    Colors Alphafold structures by pLDDT

    USAGE
    coloraf sele

    PARAMETERS

    sele (string)
    The name of the selection/object to color by pLDDT. Default: all
    """

    cmd.color("blue", f"({selection}) and b > 0.9")
    cmd.color("cyan", f"({selection}) and b < 0.9 and b > 0.7")
    cmd.color("yellow", f"({selection}) and b < 0.7 and b > 0.5")
    cmd.color("orange", f"({selection}) and b < 0.5")


cmd.extend("coloraf", coloraf)
cmd.auto_arg[0]["coloraf"] = [cmd.object_sc, "object", ""]
