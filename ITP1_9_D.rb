str = gets.chomp

q = gets.to_i
q.times do
  cmd, *args = gets.chomp.split
  a, b = args[0..1].map(&:to_i)

  case cmd
  when 'reverse'
    str[a..b] = str[a..b].reverse
  when 'replace'
    str[a..b] = args[2]
  else # print
    puts str[a..b]
  end
end
