import matplotlib.pyplot as plt

def fibonacci():
    num = int(input("Up to what number would you like to generate?: "))
    values = []
    if num == 0:
        return 0
    elif num == 1:
        values = [1]
    elif num == 2:
        values = [1,1]
    else:
        values = [1,1]
        i = 1
        while i < (num-1):
            values.append(values[i] + values[i-1])
            i += 1
    return values


y_values = fibonacci()
x_values = list(range(0,len(y_values)))


plt.xlabel("Number in Sequence")
plt.ylabel("Value")
plt.plot(x_values, y_values)
plt.show()