SUITS = %w{S H C D}.freeze

def main
  cards = all_cards

  n = gets.to_i
  n.times do
    c = gets.split
    s, r = c[0], c[1].to_i
    cards[s].delete(r)
  end

  SUITS.each do |s|
    cards[s].each{|r| puts "#{s} #{r}" }
  end
end

def all_cards
  c = {}
  SUITS.each do |s|
    c[s] = (1..13).to_a
  end
  c
end

main
