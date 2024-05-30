from tkinter import *
import random

root = Tk()
root.title("Dictionary")
root.geometry("600x400")

dictionary = {"Color" :  [
    "antiquewhite", "antiquewhite1", "antiquewhite2", "antiquewhite3", "antiquewhite4", "aqua", 
    "aquamarine1", "aquamarine2", "aquamarine3", "aquamarine4", "azure", "azure1", "azure2", "azure3", 
    "azure4", "banana", "beige", "bisque1", "bisque2", "bisque3", "bisque4", "black", "blanchedalmond", 
    "blue", "blue2", "blue3", "blue4", "blueviolet", "brick", "brown", "brown1", "brown2", "brown3", 
    "brown4", "burlywood", "burlywood1", "burlywood2", "burlywood3", "burlywood4", "burntsienna", 
    "burntumber", "cadetblue", "cadetblue1", "cadetblue2", "cadetblue3", "cadetblue4", "cadmiumorange", 
    "cadmiumyellow", "carrot", "chartreuse", "chartreuse1", "chartreuse2", "chartreuse3", "chartreuse4", 
    "chocolate", "chocolate1", "chocolate2", "chocolate3", "chocolate4", "cobalt", "cobaltgreen", "coldgrey", 
    "coral", "coral1", "coral2", "coral3", "coral4", "cornflowerblue", "cornsilk", "cornsilk1", "cornsilk2", 
    "cornsilk3", "cornsilk4", "crimson", "cyan", "cyan2", "cyan3", "cyan4", "darkgoldenrod", "darkgoldenrod1", 
    "darkgoldenrod2", "darkgoldenrod3", "darkgoldenrod4", "darkgray", "darkgreen", "darkkhaki", "darkolivegreen", 
    "darkolivegreen1", "darkolivegreen2", "darkolivegreen3", "darkolivegreen4", "darkorange", "darkorange1", 
    "darkorange2", "darkorange3", "darkorange4", "darkorchid", "darkorchid1", "darkorchid2", "darkorchid3", 
    "darkorchid4", "darksalmon", "darkseagreen", "darkseagreen1", "darkseagreen2", "darkseagreen3", 
    "darkseagreen4", "darkslateblue", "darkslategray", "darkslategray1", "darkslategray2", "darkslategray3", 
    "darkslategray4", "darkturquoise", "darkviolet", "deeppink1", "deeppink2", "deeppink3", "deeppink4", 
    "deepskyblue", "deepskyblue1", "deepskyblue2", "deepskyblue3", "deepskyblue4", "dimgray", "dodgerblue1", 
    "dodgerblue2", "dodgerblue3", "dodgerblue4", "eggshell", "emeraldgreen", "firebrick", "firebrick1", 
    "firebrick2", "firebrick3", "firebrick4", "flesh", "floralwhite", "forestgreen", "gainsboro", "ghostwhite", 
    "gold1", "gold2", "gold3", "gold4", "goldenrod", "goldenrod1", "goldenrod2", "goldenrod3", "goldenrod4", 
    "gray", "gray1", "gray10", "gray11", "gray12", "gray13", "gray14", "gray15", "gray16", "gray17", "gray18", 
    "gray19", "gray2", "gray20", "gray21", "gray22", "gray23", "gray24", "gray25", "gray26", "gray27", "gray28", 
    "gray29", "gray3", "gray30", "gray31", "gray32", "gray33", "gray34", "gray35", "gray36", "gray37", "gray38", 
    "gray39", "gray4", "gray40", "gray42", "gray43", "gray44", "gray45", "gray46", "gray47", "gray48", "gray49", 
    "gray5", "gray50", "gray51", "gray52", "gray53", "gray54", "gray55", "gray56", "gray57", "gray58", "gray59", 
    "gray6", "gray60", "gray61", "gray62", "gray63", "gray64", "gray65", "gray66", "gray67", "gray68", "gray69", 
    "gray7", "gray70", "gray71", "gray72", "gray73", "gray74", "gray75", "gray76", "gray77", "gray78", "gray79", 
    "gray8", "gray80", "gray81", "gray82", "gray83", "gray84", "gray85", "gray86", "gray87", "gray88", "gray89", 
    "gray9", "gray90", "gray91", "gray92", "gray93", "gray94", "gray95", "gray97", "gray98", "gray99", "green", 
    "green1", "green2", "green3", "green4", "greenyellow", "honeydew1", "honeydew2", "honeydew3", "honeydew4", 
    "hotpink", "hotpink1", "hotpink2", "hotpink3", "hotpink4", "indianred", "indianred1", "indianred2", 
    "indianred3", "indianred4", "indigo", "ivory1", "ivory2", "ivory3", "ivory4", "ivoryblack", "khaki", 
    "khaki1", "khaki2", "khaki3", "khaki4", "lavender", "lavenderblush1", "lavenderblush2", "lavenderblush3", 
    "lavenderblush4", "lawngreen", "lemonchiffon1", "lemonchiffon2", "lemonchiffon3", "lemonchiffon4", 
    "lightblue", "lightblue1", "lightblue2", "lightblue3", "lightblue4", "lightcoral", "lightcyan1", "lightcyan2", 
    "lightcyan3", "lightcyan4", "lightgoldenrod1", "lightgoldenrod2", "lightgoldenrod3", "lightgoldenrod4", 
    "lightgoldenrodyellow", "lightgrey", "lightpink", "lightpink1", "lightpink2", "lightpink3", "lightpink4", 
    "lightsalmon1", "lightsalmon2", "lightsalmon3", "lightsalmon4", "lightseagreen", "lightskyblue", 
    "lightskyblue1", "lightskyblue2", "lightskyblue3", "lightskyblue4", "lightslateblue", "lightslategray", 
    "lightsteelblue", "lightsteelblue1", "lightsteelblue2", "lightsteelblue3", "lightsteelblue4", "lightyellow1", 
    "lightyellow2", "lightyellow3", "lightyellow4", "limegreen", "linen", "magenta", "magenta2", "magenta3", 
    "magenta4", "manganeseblue", "maroon", "maroon1", "maroon2", "maroon3", "maroon4", "mediumorchid", 
    "mediumorchid1", "mediumorchid2", "mediumorchid3", "mediumorchid4", "mediumpurple", "mediumpurple1", 
    "mediumpurple2", "mediumpurple3", "mediumpurple4", "mediumseagreen", "mediumslateblue", "mediumspringgreen", 
    "mediumturquoise", "mediumvioletred", "melon", "midnightblue", "mint", "mintcream", "mistyrose1", "mistyrose2", 
    "mistyrose3", "mistyrose4", "moccasin", "navajowhite1", "navajowhite2", "navajowhite3", "navajowhite4", 
    "navy", "oldlace", "olive", "olivedrab", "olivedrab1", "olivedrab2", "olivedrab3", "olivedrab4", "orange", 
    "orange1", "orange2", "orange3", "orange4", "orangered1", "orangered2", "orangered3", "orangered"]}

def bg_color_change():
    random_color = random.randint(0, 478)
    print(dictionary["Color"][random_color])
    root.configure(background = dictionary["Color"][random_color])

btn = Button(root, text = "Change Color", command = bg_color_change)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)

root.mainloop()