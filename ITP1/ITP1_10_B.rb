a, b, c = gets.split.map(&:to_i)

theta = (Math::PI * c) / 180
h = Math.sin(theta) * b
s = h * a / 2
d = Math.sqrt(a*a + b*b - (2*a*b*Math.cos(theta)))

printf ("%.5f\n"*3), s, (d+a+b), h
