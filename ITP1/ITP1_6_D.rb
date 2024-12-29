n, m = gets.split.map(&:to_i)

a = []
n.times do
  a << gets.split.map(&:to_i)
end

b = []
m.times do
  b << gets.to_i
end

c = a.map{|ai|
  ai.map.with_index{|aj, j| aj*b[j] }.inject(0, &:+)
}
c.each do |ci|
  puts ci
end
