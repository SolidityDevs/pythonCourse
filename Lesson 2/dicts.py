laptops = {
    'brand': 'hp',
    'color': 'black',
    'price': 1200,
    'model': ['windows','linux','mac']
    
}

print(laptops['model'])
print(laptops.keys())
print(laptops.get('price'))
print(laptops.values())
laptops['color'] = 'red'
laptops.update({'color': 'green'})
if 'color' in laptops:
    print(laptops['color'])
    print('yes color exist')