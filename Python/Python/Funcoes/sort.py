# Crie uma função "sort()" que recebe 
# uma lista, ordena ela do menor para o 
# maior e retorna ela ordenada

def quick_sort(numbers: list) -> list:
    if len(numbers) <= 1:
        return numbers
    
    pivot = numbers.pop()
    low, high = [], []
    for number in numbers:
        if number > pivot:
            high.append(number)
        else:
            low.append(number)
    return quick_sort(low) + [pivot] + quick_sort(high)
    

# def sort(numbers: list) -> list:
#     for i in range(len(numbers)):
#         for j in range(len(numbers) - 1):
#             if numbers[j] > numbers[j + 1]:
#                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    
#     return numbers

a = [7,5,10,1,9]
a = quick_sort(a)
print(a)