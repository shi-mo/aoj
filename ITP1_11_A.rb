def main
  face_ids = [nil] + gets.chomp.split
  commands = gets.chomp.split(//)

  # top, S, E (, N, W, bottom)
  faces = [1, 2, 3]
  commands.each do |cmd|
    operate(faces, cmd)
  end
  puts face_ids[faces[0]]
end

def operate(faces, cmd)
  case cmd
  when 'N'
    top = faces[1]
    s = opposite(faces[0])
    faces[0] = top
    faces[1] = s
  when 'E'
    top = opposite(faces[2])
    e = faces[0]
    faces[0] = top
    faces[2] = e
  when 'S'
    top = opposite(faces[1])
    s = faces[0]
    faces[0] = top
    faces[1] = s
  else # W
    top = faces[2]
    e = opposite(faces[0])
    faces[0] = top
    faces[2] = e
  end
end

def opposite(face)
  7 - face
end

main()
