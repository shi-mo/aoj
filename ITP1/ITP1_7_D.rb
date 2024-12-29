n, m, l = gets.split.map(&:to_i)

a = []
n.times do
  a << gets.split.map(&:to_i)
end

b = []
m.times do
  b << gets.split.map(&:to_i)
end

c = a.map{|ai|
  (0...l).map{|j|
    ai.map.with_index{|ak, k| ak*b[k][j] }.inject(0, &:+)
  }
}
c.each do |ci|
  puts ci.join(' ')
end
