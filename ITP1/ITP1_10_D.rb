require 'bigdecimal'

n = gets.to_i
x, y = 2.times.map {
  gets.chomp.split.map{|v| BigDecimal(v) }
}

d1 = (0...n).map{|i| (x[i] - y[i]).abs }.inject(BigDecimal(0), :+)
d2 = (0...n).map{|i| (x[i] - y[i]) ** 2 }.inject(BigDecimal(0), :+).sqrt(8)
d3 = (0...n).map{|i| (x[i] - y[i]).abs ** 3 }.inject(BigDecimal(0), :+) ** (BigDecimal(1) / BigDecimal(3))
dinf = (0...n).map{|i| (x[i] - y[i]).abs }.max

printf ("%.06f\n"*4), d1, d2, d3, dinf
