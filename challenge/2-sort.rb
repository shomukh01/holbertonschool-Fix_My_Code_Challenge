###
#
# Sort integer arguments (ascending)
#
###

result = []
ARGV.each do |arg|
  # skip if not integer
  next unless arg.match?(/\A-?[0-9]+\z/)

  number = arg.to_i
  index = 0
  index += 1 while index < result.length && result[index] < number
  result.insert(index, number)
end

puts result
