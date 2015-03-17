# Typograf
client for artlebedev typograf webservice

<p>&laquo;Вы&nbsp;все еще кое-как верстаете в&nbsp;&bdquo;Ворде&ldquo;? &mdash;&nbsp;Тогда мы&nbsp;идем к&nbsp;вам!&raquo;<br />
</p>
---
Python2 not Unicode
================
```python
# -*- encoding: windows-1251 -*-
from RemoteTypograf import RemoteTypograf

rt = RemoteTypograf('windows-1251')

rt.htmlEntities()
rt.br(1)
rt.p(1)
rt.nobr(3)
print rt.processText(u'"Âû âñå åùå êîå-êàê âåðñòàåòå â "Âîðäå"? - Òîãäà ìû èäåì ê âàì!"')
```

```html
<p>&laquo;Вы&nbsp;все еще кое-как верстаете в&nbsp;&bdquo;Ворде&ldquo;? &mdash;&nbsp;Тогда мы&nbsp;идем к&nbsp;вам!&raquo;<br />
</p>
```

Python2 Unicode
=============
```python
# -*- encoding: utf-8 -*-
from RemoteTypograf import RemoteTypograf

rt = RemoteTypograf() # UTF-8

rt.htmlEntities()
rt.br(1)
rt.p(1)
rt.nobr(3)
print rt.processText(u'"Вы все еще кое-как верстаете в "Ворде"? - Тогда мы идем к вам!"')
```

```html
<p>&laquo;Вы&nbsp;все еще кое-как верстаете в&nbsp;&bdquo;Ворде&ldquo;? &mdash;&nbsp;Тогда мы&nbsp;идем к&nbsp;вам!&raquo;<br />
</p>
```

Python3
======
```python
from RemoteTypograf import RemoteTypograf

rt = RemoteTypograf()

rt.htmlEntities()
rt.br(1)
rt.p(1)
rt.nobr(3)
print(rt.processText('"Вы все еще кое-как верстаете в "Ворде"? - Тогда мы идем к вам!"'))
```

```html
<p>&laquo;Вы&nbsp;все еще кое-как верстаете в&nbsp;&bdquo;Ворде&ldquo;? &mdash;&nbsp;Тогда мы&nbsp;идем к&nbsp;вам!&raquo;<br />
</p>
```
