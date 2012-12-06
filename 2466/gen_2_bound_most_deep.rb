basename = '_2_bound_most_depp'

len_max = 100000
open("#{basename}.input", 'w') do |f|
  (len_max / 2).times{ f.print '(' }
  (len_max / 2).times{ f.print ')' }
  f.puts
end

open("#{basename}.output", 'w') do |f|
  f.puts ((len_max / 2) - 1).to_i
end
