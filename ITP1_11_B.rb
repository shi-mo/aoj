def main
  right_of = init_right_table()

  faces = [nil] + gets.chomp.split
  label_of = faces.map.with_index{|f, i| { f => i } }.inject({}, &:merge)

  n = gets.to_i
  n.times do
    top, front = gets.chomp.split.map{|f| label_of[f] }
    puts faces[ right_of[top][front] ]
  end
end

# table[top][front] -> right
def init_right_table
  table = Array.new(7){ Array.new(7) }
  table[1][2] = 3
  table[1][3] = 5
  table[1][4] = 2
  table[1][5] = 4
  table[2][1] = 4
  table[2][3] = 1
  table[2][4] = 6
  table[2][6] = 3
  table[3][1] = 2
  table[3][2] = 6
  table[3][5] = 1
  table[3][6] = 5
  table[4][1] = 5
  table[4][2] = 1
  table[4][5] = 6
  table[4][6] = 2
  table[5][1] = 3
  table[5][3] = 6
  table[5][4] = 1
  table[5][6] = 4
  table[6][2] = 4
  table[6][3] = 2
  table[6][4] = 5
  table[6][5] = 3
  table
end

main
