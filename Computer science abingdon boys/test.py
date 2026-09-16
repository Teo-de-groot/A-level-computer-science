

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']  
vowels = ('a', 'e', 'i', 'o', 'u')
fruits_with_more_than_two_vowels = [fruit for fruit in fruits if sum(1 for letter in fruit if letter in vowels) >= 2]
print(fruits_with_more_than_two_vowels)   \

