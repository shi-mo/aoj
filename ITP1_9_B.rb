class Deck
  def initialize(deck)
    @deck = deck
  end

  def shuffle(h)
    @deck = @deck[h..-1] + @deck[0,h]
  end

  def to_s
    @deck.clone
  end
end

def main
  deck = nil
  while s = gets.chomp
    break if '-' == s

    deck = Deck.new(s)
    n = gets.to_i
    n.times do
      deck.shuffle(gets.to_i)
    end
    puts deck
  end
end

main
