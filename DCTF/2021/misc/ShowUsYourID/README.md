## Description

<p align="center">
<img src="Image/image-20210518205835512.png">
</p>

## Hint

<p align="center">
<img src="Image/image-20210518205848669.png">
</p>

## Solution

Same thing as [Don't let it Run](https://github.com/CHOOCS/CTF-Writeups/tree/master/DCTF/2021/misc/DontLetItRun) challenge, after download the pdf and we will run [pdf-parser](https://en.wikipedia.org/wiki/Pdf-parser) to analyze the object.

After some inspection, nothing special shows up.

But, there is a parameter in this tool which is `-c`

> -c - display the content for objects without streams or with streams without filters

`pdf-parser -c nyan.pdf`

After running this command we will get all the info of the objects without stream.

Since the title of the challenge says show us your id, we might as well try to grep the id out

`pdf-parser -c nyan.pdf | grep id=`

<p align="center">
<img src="Image/image-20210518210323304.png">
</p>

`id="646374667b3362306261347d"`

We got the ID, we can put the value to [cyberchef](https://gchq.github.io/CyberChef) to decrypt it

<p align="center">
<img src="Image/image-20210518210441422.png">
</p>