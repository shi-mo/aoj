def line_for(tile, w)
  (0...w).map{|j| tile[j%2] }.join
end

while s = gets
    h, w = s.split.map(&:to_i)
    exit 0 if 0 == h && 0 == w

    lines = []
    lines[0] = line_for('#.', w)
    lines[1] = line_for('.#', w)
    h.times do |i|
      puts lines[i%2]
    end
    puts
end
