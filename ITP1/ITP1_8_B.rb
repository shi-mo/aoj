while s = gets.chomp
  break if '0' == s
  puts s.split(//).map(&:to_i).inject(:+)
end
