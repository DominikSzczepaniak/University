# Dominik Szczepaniak 
# lista 10

class Collection
	def initialize(data)
		@data = data.dup
	end

	def swap(i, j)
		@data[i], @data[j] = @data[j], @data[i]
	end

	def length
		@data.length
	end

	def get(i)
		@data[i]
	end

	def set(i, value)
		@data[i] = value
	end

	def to_s
		@data.to_s
	end

	def to_a
		@data
	end
end

class Sorter
	#merge sort SZYBSZY
	def self.sort1(collection)
		n = collection.length
		if n <= 1
			return collection
		end
		mid = n / 2
		left = Collection.new(collection.to_a[0...mid])
		right = Collection.new(collection.to_a[mid...n])
		left = sort1(left)
		right = sort1(right)
		merge(left, right)
	end

	def self.merge(left, right)
		result = Collection.new([])
		while left.length > 0 && right.length > 0
			if left.get(0) <= right.get(0)
				result.set(result.length, left.get(0))
				left = Collection.new(left.to_a[1...left.length])
			else
				result.set(result.length, right.get(0))
				right = Collection.new(right.to_a[1...right.length])
			end
		end
		while left.length > 0
			result.set(result.length, left.get(0))
			left = Collection.new(left.to_a[1...left.length])
		end
		while right.length > 0
			result.set(result.length, right.get(0))
			right = Collection.new(right.to_a[1...right.length])
		end
		result
	end

	#insertion sort
	def self.sort2(collection)
		n = collection.length
		(1...n).each do |i|
			j = i
			while j > 0 && collection.get(j-1) > collection.get(j)
				collection.swap(j-1, j)
				j -= 1
			end
		end
		collection
	end
end

data = [64, 34, 25, 12, 22, 11, 90]

collection = Collection.new(data)
sorted_collection = Sorter.sort1(collection)
puts "Merge Sort: #{sorted_collection}"

collection = Collection.new(data)
sorted_collection = Sorter.sort2(collection)
puts "Insertion Sort: #{sorted_collection}"