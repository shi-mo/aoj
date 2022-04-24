w = gets.chomp
t = $stdin.read.chomp.gsub(/\n/o, ' ').split.map(&:downcase)
puts t.count(w)
