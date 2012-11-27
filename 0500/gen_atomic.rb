(0..9).each do |i|
  (0..9).each do |j|
    basename = "1_#{i}#{j}_atomic"
    open("#{basename}.input", 'w') do |f|
      f.puts '1'
      f.puts "#{i} #{j}"
      f.puts '0'
    end
    open("#{basename}.output", 'w') do |f|
      if i == j
        f.puts "#{i} #{j}"
        break
      end
      if i < j
        f.puts "0 #{i+j}"
        break
      end
      if j < i
        f.puts "#{i+j} 0"
        break
      end
      raise 'must not happen'
    end
  end
end
