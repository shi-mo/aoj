TOP = 0
FRONT = 1
RIGHT = 2

def main
  faces = [nil] + gets.chomp.split
  commands = gets.chomp.split(//)

  # top, front, right
  dice = [1, 2, 3]
  commands.each do |cmd|
    operate(dice, cmd)
  end
  puts faces[dice[TOP]]
end

def operate(dice, cmd)
  case cmd
  when 'N'
    top = dice[FRONT]
    front = opposite(dice[TOP])
    dice[TOP] = top
    dice[FRONT] = front
  when 'E'
    top = opposite(dice[RIGHT])
    right = dice[TOP]
    dice[TOP] = top
    dice[RIGHT] = right 
  when 'S'
    top = opposite(dice[FRONT])
    front = dice[TOP]
    dice[TOP] = top
    dice[FRONT] = front
  else # W
    top = dice[RIGHT]
    right = opposite(dice[TOP])
    dice[TOP] = top
    dice[RIGHT] = right
  end
end

def opposite(label)
  7 - label
end

main()
