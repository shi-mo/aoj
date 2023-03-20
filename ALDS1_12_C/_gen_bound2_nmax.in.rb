n = 10000

open('bound2_nmax.in', 'w') do |f|
  f.puts n
  n.times do |i|
    if 50 <= i
      f.puts "#{i} 0"
      next
    end
    f.print "#{i} #{n-1}"
    n.times do |j|
      next if j == i
      f.print " #{j} 100000"
    end
    f.puts
  end
end
