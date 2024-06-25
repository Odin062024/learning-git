shopping = {
  'Lidl'.title() : ['chleb'.title(),'bagietka'.title(),'margaryna'.title(),'kawa'.title()],
  'Biedronka'.title() : ['ziemniaki'.title(), 'mydło'.title()]
}

for shop in shopping:
  list_001 = shopping.get(shop)
  print('Idę do {} i kupuję tam {}.'.format(shop, list_001))

