require 'bigdecimal'
x1,y1,x2,y2 = gets.split.map{|r| BigDecimal(r) }
d = ((x2-x1)**2 + (y2-y1)**2).sqrt(2)
puts d.truncate(8).to_s('F')
