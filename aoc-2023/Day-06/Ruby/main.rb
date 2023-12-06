# Testing with ChatGPT
def g(a, b)
    a - 1 - 2 * ((a - Math.sqrt(a * a - 4 * b)) / 2).to_i
end

data = []

2.times do
    data << gets.split(/:\s+/)[1].split(/\s+/)
end

p = 1
a = ''
b = ''

data[0].each_with_index do |x, i|
    y = data[1][i]
    p *= g(x.to_i, y.to_i)
    a += x
    b += y
end

puts "Part 1: #{p}"
puts "Part 2: #{g(a.to_i, b.to_i)}"