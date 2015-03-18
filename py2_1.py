from typograf import RemoteTypograf
rt = RemoteTypograf(p=True, br=True)
print(rt.process_text('"Вы все еще кое-как верстаете в "Ворде"? - Тогда мы идем к вам!"'))
