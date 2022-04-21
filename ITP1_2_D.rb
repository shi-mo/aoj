w, h, x, y, r = gets.split.map(&:to_i)

if (x-r) < 0 || w < (x+r)
  puts 'No'
  exit 0
end

if (y-r) < 0 || h < (y+r)
  puts 'No'
  exit 0
end

puts 'Yes'
