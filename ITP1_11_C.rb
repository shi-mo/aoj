# Original code: https://qiita.com/KotaYoneda/items/cbe4e35049b6a9e038dd

class Dice
  def initialize(sequence)
    @sequence = sequence
  end
  attr_reader :sequence

  def move(code)
    code.split(//).map{|c| @sequence[c.to_i] }
  end

  def roll(commands)
    commands.split(//).each do |cmd|
      @sequence = case cmd
        when 'N'
          move('152304')
        when 'E'
          move('310542')
        when 'S'
          move('402351')
        else # W
          move('215043')
        end
    end
  end
end

class IdentDice
  def initialize(sequence)
    @candidates = all_candidates_for(sequence)
  end
  attr_reader :candidates

  def all_candidates_for(sequence)
    candidates = []
    ['', 'N', 'W', 'E', 'S', 'NN'].each do |cmd|
      dice = Dice.new(sequence)
      dice.roll(cmd)
      4.times do
        dice.roll('NES') # horizontal roll
        candidates << dice.sequence
      end
    end
    candidates
  end

  def ==(other)
    self.candidates.min == other.candidates.min
  end
end

def main
  idices = 2.times.map{ IdentDice.new(gets.chomp.split.map(&:to_i)) }
  puts (idices[0] == idices[1]) ? 'Yes' : 'No'
end

main()
