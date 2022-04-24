num = {}
('a'..'z').each{|c| num[c] = 0 }
$stdin.read.gsub(/[^a-zA-Z]+/o, '').downcase.each_char{|c| num[c] += 1 }
num.each{|c, n| puts "#{c} : #{n}" }
