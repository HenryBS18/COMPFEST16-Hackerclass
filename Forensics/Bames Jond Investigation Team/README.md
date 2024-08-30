# Title
Bames Jond Investigation Team (500 points)

# Flag
COMPFEST16{Windows-7_MicrosoftEdge-MicrosoftPaint-WindowsMediaPlayer_Definetly Tugas Sekolah_Java-Python}

# Description
Few days ago, You have just received an invitation to Bames Jond Investigatiom Team to work there for 3 months. As a firsk task of your intern there, The Boss have command you to investigate RAM Capture file and retreive important intel. Written on a sticky notes stuck to your laptop screen, The Boss pointed out which information is needed to be retreived.

1. The operating system that the machine runs. Write in **[OperatingSystem]-[Version]**. For example, **Windows-7** or **Ubuntu-20.07**
2. Application(s) that is currently opened by the user excluding file explorer. Write in **[ApplicationOne]-[ApplicationTwo]**. For example, **MicrosoftPowerPoint-MicrosoftWord-Notepad**.
3. File/folder(s) that is contained inside "Tugas Sekolah" folder. Write in in their original name without their extension in this format, **[File/Folder 1]-[File/Folder 2]**. For example, **Important Folder-Melon Cat**
4. Programming language that the user are using inside that machine. Write in **[Language1]-[Language2]**. For example, **C-C++-Java**

For multiple answer questions, write the answer in lexicographic order. Concantenate all the information received and put them in this format **COMPFEST16{[answer1]_[answer2]_[answer3]_[answer4]}**. So from the examples above, the answer would be,
```COMPFEST16{Windows-7_MicrosoftPowerPoint-MicrosoftWord-Notepad_Important Folder-Melon Cat_C-C++-Java}```

On the sticky notes, the boss adds,

You can try volatility to analyze this memory image. Ignore the RamCapture64 process as that is the application we used to capture the memory image. Best of luck to you.
Regards,

Bames Jond

As this is your first step diving into Memory Analysis, you, are filled with determination to get this task done.

https://drive.google.com/file/d/181HJuIx_nEF-CSLcf6P3sxCWrW3MmtD8/view?usp=sharing

# Author
houseoforion

# Solution
given memory dump file.

analyze it with volatility3 https://github.com/volatilityfoundation/volatility3.
volatility3 need python 3.7.3 or higher.

example use:
```bash
py -3.7 vol.py -h
```

```bash
py -3.7 vol.py -f 20221126.mem windows.info
```

i also use strings to get information
```bash
strings 20221126.mem | grep -i 'Tugas Sekolah' | uniq
```

information i got:
1. OS-Version
windows-7, Windows-10, windows-NT

2. Application currently opened by user:
MicrosoftEdge, WindowsMediaPlayer, MSPaint

3. File/Folder inside 'Tugas Sekolah' directory:
Definetly Tugas Sekolah

4. Programming language that user use inside the machine:
python, java, cpp, javascript, php

from the information i got, i just try all the combinations until got the right one.
and dont forget to use lexicographic order.