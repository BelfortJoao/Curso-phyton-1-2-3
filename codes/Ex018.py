import math
print('Welcome to the trigonometron')
z = float(input('Chose one angle: '))
y = 'Now we have the results'
print('{:-^40} '.format(y))
x = math.radians(z)
sin = math.sin(x)
cos = math.cos(x)
tan = math.tan(x)

print(' you chose {}, in radius {:.3f}  \n cosine= {:.3f} \n sine= {:.3f} \n tangent= {:.3f} '.format(z, x, cos, sin, tan))
