basename = '_1_2_sets_bound_10000'

n = 10000

open("#{basename}.input", 'w') do |f|
  f.puts n
  n.times{ f.puts '1' }
  f.puts '0'
end

open("#{basename}.output", 'w') do |f|
  wait = n * (n-1) / 2
  f.puts wait
end
