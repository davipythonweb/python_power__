from instruments_12 import Guitar, Flute, InstrumentKind, EletricGuitar

gianini = Guitar(name="Gianini", kind=InstrumentKind.string, colors=["green"])
print(gianini.play())  # Output: Trom Trom
print(gianini.colors)  # Output: ['green']

yamaha = Flute(name="Yamaha", kind=InstrumentKind.wind, colors=["silver", "gold"])
print(yamaha.play())   # Output: Tooooot
print(yamaha.colors)   # Output: ['silver', 'gold']

lespaul = EletricGuitar(name="Lespaul m3")
print(lespaul.play())  # Output: wah~~~~wah~~~~wah
