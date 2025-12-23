from instruments_12 import Guitar, Flute, InstrumentKind

gianini = Guitar(name="Gianini", kind=InstrumentKind.string)
print(gianini.play())  # Output: Trom Trom
print(gianini.colors)  # Output: []

yamaha = Flute(name="Yamaha")
print(yamaha.play())   # Output: Tooooot
print(yamaha.colors)   # Output: []

