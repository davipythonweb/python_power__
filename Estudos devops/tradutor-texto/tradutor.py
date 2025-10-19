from translate import Translator

# Configura a tradução #
s = Translator(from_lang="english", to_lang="pt-br")

# Traduz texto desejado #
res = s.translate("A programming language.")

# Mostra tradução #
print(res)   