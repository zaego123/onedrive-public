这就是说：
1、v+移动光标可以选中文本。
2、y可以复制已经选中的文本
3、p可以粘贴


复制一行则：yy
复制当前光标所在的位置到行尾：y$
复制当前光标所在的位置到行首：y^
复制三行则：3yy，即从当前光标+下两行。

剪切文本：
用v选中文本之后可以按y进行复制，如果按d就表示剪切，之后按p进行粘贴。

剪切一行：dd
剪切当前行光标所在的位置到行尾：d$
剪切当前行光标所在的位置到行首：d^
前切三行：3dd,即从当前行+下两行被剪切了。