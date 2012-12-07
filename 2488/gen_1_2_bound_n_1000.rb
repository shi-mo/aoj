basename = '_1_2_bound_n_1000'

n = 1000
open("#{basename}.input", 'w') do |f|
  f.puts n
  n.times do |i|
    f.puts "#{n-i} #{i+1}"
  end
end
