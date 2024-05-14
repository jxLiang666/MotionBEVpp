#!/usr/bin/env python3
# Developed by jxLiang
from colorizePrint import colorizePrint

cp = colorizePrint("This is demo.py")
cp.cprint("-" * 9 + "fgc" + "-" * 9)
cp("Default   :hello world!")
cp("Black     :hello world!", fgc="Black")
cp("Green     :hello world!", fgc="Green")
cp("Yellow    :hello world!", fgc="Yellow")
cp("Blue      :hello world!", fgc="Blue")
cp("Magenta   :hello world!", fgc="Magenta")
cp("Cyan      :hello world!", fgc="Cyan")
cp("White     :hello world!", fgc="White")
cp("\n")

cp.cprint("-" * 9 + "bgc" + "-" * 9)
cp.cprint("Default   :hello world!")
cp.cprint("Black     :hello world!", bgc="Black")
cp.cprint("Red       :hello world!", bgc="Red")
cp.cprint("Green     :hello world!", bgc="Green")
cp.cprint("Yellow    :hello world!", bgc="Yellow")

cp.cprint("Blue      :hello world!", bgc="Blue")
cp.cprint("Magenta   :hello world!", bgc="Magenta")
cp.cprint("Cyan      :hello world!", bgc="Cyan")
cp.cprint("White     :hello world!", fgc="Black", bgc="White")
cp("\n")

cp("-" * 8 + "fontsetting" + "-" * 8)
cp("Default         :hello world!", fontsetting="Default", fgc="Green")
cp("Highlight       :hello world!", fontsetting="Highlight", fgc="Green")
cp("Halfhighlight   :hello world!", fontsetting="Halfhighlight", fgc="Green")
cp("Italic          :hello world!", fontsetting="Italic", fgc="Green")
cp("Underline       :hello world!", fontsetting="Underline", fgc="Green")

cp("-" * 8 + "specialusing" + "-" * 8)
cp.redp("Red       :helloworld")
cp.yellowp("Yellow    :helloworld")
cp.greenp("Green     :helloworld")
cp.bluep("Blue      :helloworld")
cp.warning("This is warning!")
cp.error("This is error!")
cp.greenhp("Green Highlight   :helloworld")
cp.redhp("Red Highlight     :helloworld")
cp.bluehp("Blue Highlight    :helloworld")
cp.yellowhp("Yellow Highlight  :helloworld")
