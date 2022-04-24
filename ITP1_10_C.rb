require 'bigdecimal'

while line = gets
  line.chomp!
  break if '0' == line

  n = line.to_i
  s = gets.split.map{|r| BigDecimal(r) }

  m = s.inject(BigDecimal(0), :+) / n
  var = s.map{|si| (si - m)**2 }.inject(BigDecimal(0), :+) / n
  puts var.sqrt(2).truncate(8).to_s('F')
end
