basename = '_3_2_value_bound_60_10000people'

n = 10000
minutes = 60

open("#{basename}.input", 'w') do |f|
  f.puts n
  n.times{ f.puts minutes }
  f.puts '0'
end

open("#{basename}.output", 'w') do |f|
  wait = minutes * n * (n-1) / 2
  f.puts wait
end
