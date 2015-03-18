# Typograf
[![Build Status](https://travis-ci.org/Samael500/typograf.svg?branch=master)](#)

client for artlebedev typograf webservice

<p>&laquo;Вы&nbsp;все еще кое-как верстаете в&nbsp;&bdquo;Ворде&ldquo;? &mdash;&nbsp;Тогда мы&nbsp;идем к&nbsp;вам!&raquo;<br />
</p>
---
Python2 not Unicode
================
```python
# -*- encoding: windows-1251 -*-
from typograf import RemoteTypograf

rt = RemoteTypograf('windows-1251', p=True, br=True)
rt.html_entities()

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
from typograf import RemoteTypograf

rt = RemoteTypograf(p=True, br=True) # UTF-8
rt.html_entities()

print rt.processText(u'"Вы все еще кое-как верстаете в "Ворде"? - Тогда мы идем к вам!"')
```

```html
<p>&laquo;Вы&nbsp;все еще кое-как верстаете в&nbsp;&bdquo;Ворде&ldquo;? &mdash;&nbsp;Тогда мы&nbsp;идем к&nbsp;вам!&raquo;<br />
</p>
```

Python3
======
```python
from typograf import RemoteTypograf

rt = RemoteTypograf(p=True, br=True)
rt.html_entities()

print(rt.processText('"Вы все еще кое-как верстаете в "Ворде"? - Тогда мы идем к вам!"'))
```

```html
<p>&laquo;Вы&nbsp;все еще кое-как верстаете в&nbsp;&bdquo;Ворде&ldquo;? &mdash;&nbsp;Тогда мы&nbsp;идем к&nbsp;вам!&raquo;<br />
</p>
```
