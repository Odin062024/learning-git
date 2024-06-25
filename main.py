shopping = {
  'Lidl'.title() : ['chleb'.title(),'bagietka'.title(),'margaryna'.title(),'kawa'.title()],
  'Biedronka'.title() : ['ziemniaki'.title(), 'mydło'.title()]
}

for shop in shopping:
  list_001 = shopping.get(shop)
  print('Idę do {} i kupuję tam {}.'.format(shop, list_001))

print('W sumie kupuję {} produktów'.format(len(shopping['Lidl'] + shopping['Biedronka'])))

print('Hiszpańska Inkwizycja to najlepszy skecz grupy Monthy Python')
