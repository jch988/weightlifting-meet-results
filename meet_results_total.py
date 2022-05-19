import matplotlib.pyplot as plt


# put in csv and import rather than manual input
total = [0, 191, 194, 195, 195, 193, 0, 192, 199, 195, 203, 204, 196, 205, 210, 212]
snatch = [0, 80, 82, 82, 81, 83, 0, 80, 84, 85, 89, 86, 87, 90, 91, 92]
clean_and_jerk = [107, 111, 112, 113, 114, 110, 112, 112, 115, 110, 114, 118, 109, 115, 119, 120]
meets = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

width = 0.7

plt.style.use('fivethirtyeight')
fig, ax = plt.subplots()

sn = ax.bar(meets, snatch, width, label='Snatch')
cj = ax.bar(meets, clean_and_jerk, width, bottom=snatch, label='Clean and Jerk')

ax.set_title("Weightlifting meet performance")
ax.set_xlabel('Meet number')
ax.set_ylabel("Weight (kg)")

ax.legend()

ax.set_xticks(meets)

ax.bar_label(sn, label_type='center')
ax.bar_label(cj, label_type='center')
ax.bar_label(cj)




plt.show()