scores = [0, 0]

n = gets.to_i
n.times do
  a, b = gets.chomp.split
  if a == b
    scores[0] += 1
    scores[1] += 1
    next
  end
  winner = (a < b) ? 1 : 0
  scores[winner] += 3
end

puts scores.map(&:to_s).join(' ')
