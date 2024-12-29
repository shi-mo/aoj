r, c = gets.split.map(&:to_i)

a = []
r.times do |i|
  row = gets.split.map(&:to_i)
  row << row.inject(0, &:+)
  a << row
end

s = []
(c+1).times do |j|
  col = (0...r).map{|i| a[i][j] }
  s << col.inject(0, &:+)
end
a << s

a.each do |row|
  puts row.join(' ')
end
