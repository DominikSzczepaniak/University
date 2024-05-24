class Node
	attr_accessor :value, :next, :prev

	def initialize(value)
		@value = value
		@next = nil
		@prev = nil
	end
end

class Kolekcja
	attr_reader :head, :tail

	def initialize
		@head = nil
		@tail = nil
	end

	def insert(value)
		new_node = Node.new(value)
		if @head.nil?
			@head = new_node
			@tail = new_node
		else
			current = @head
			current = current.next while current.next && current.value < value
			if current == @tail && current.value < value
				current.next = new_node
				new_node.prev = current
				@tail = new_node
			else
				new_node.next = current
				new_node.prev = current.prev
				current.prev.next = new_node unless current.prev.nil?
				current.prev = new_node
				@head = new_node if current == @head && new_node.value < current.value
			end
		end
	end

	def to_a
		elements = []
		current = @head
		while current
			elements << current.value
			current = current.next
		end
		elements
	end
end

class Wyszukiwanie
	def self.binary_search(collection, target)
		array = collection.to_a
		left, right = 0, array.length - 1

		while left <= right
			mid = (left + right) / 2
			return mid if array[mid] == target

			if array[mid] < target
				left = mid + 1
			else
				right = mid - 1
			end
		end

		-1
	end

	def self.interpolation_search(collection, target)
		array = collection.to_a
		low, high = 0, array.size - 1

		while low <= high && target >= array[low] && target <= array[high]
			pos = low + ((high - low) * (target - array[low]) / (array[high] - array[low]))
			return pos if array[pos] == target

			if array[pos] < target
				low = pos + 1
			else
				high = pos - 1
			end
		end

		-1
	end
end

kolekcja = Kolekcja.new
kolekcja.insert(5)
kolekcja.insert(3)
kolekcja.insert(8)
kolekcja.insert(1)
kolekcja.insert(4)

puts "Elementy kolekcji: #{kolekcja.to_a.join(', ')}"

index = Wyszukiwanie.binary_search(kolekcja, 4)
puts "Index znalezionego elementu (binarnie): #{index}"

index = Wyszukiwanie.interpolation_search(kolekcja, 8)
puts "Index znalezionego elementu (interpolacyjnie): #{index}"
