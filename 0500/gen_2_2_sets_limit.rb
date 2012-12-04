limit = 10000
basename = '_2_2_sets_limit'

open("#{basename}.input", 'w') do |f|
  f.puts limit.to_s
  limit.times do
    f.puts '9 8'
  end
  f.puts '0'
end

open("#{basename}.output", 'w') do |f|
  f.puts "#{limit * 17} 0"
end
