if 2 != ARGV.size
  warn "usage: ruby #{__FILE__} 100 1_3_sets_100"
  exit 1
end

n = ARGV[0].to_i
basename = ARGV[1]

open("#{basename}.input", 'w') do |f|
  f.puts n.to_s
  n.times do
    f.puts '3 4 5'
  end
end

open("#{basename}.output", 'w') do |f|
  n.times do
    f.puts 'YES'
  end
end
