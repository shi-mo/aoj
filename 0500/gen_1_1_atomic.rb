basename = '_1_1_atomic'

open("#{basename}.input", 'w') do |f|
  (0..9).each do |i|
    (0..9).each do |j|
      f.puts '1'
      f.puts "#{i} #{j}"
    end
  end
  f.puts '0'
end
open("#{basename}.output", 'w') do |f|
  (0..9).each do |i|
    (0..9).each do |j|
      if i == j
        f.puts "#{i} #{j}"
        next
      end
      if i < j
        f.puts "0 #{i+j}"
        next
      end
      if j < i
        f.puts "#{i+j} 0"
        next
      end
      raise 'must not happen'
    end
  end
end
