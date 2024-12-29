n = 10000

open('bound2_nmax.out', 'w') do |f|
  f.puts '0 0'
  1.upto(n-1) do |i|
    f.puts "#{i} 100000"
  end
end
