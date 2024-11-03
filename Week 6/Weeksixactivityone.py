import matplotlib.pyplot as plt

days = ['Monday', 'Tuesday', 'Thursday', 'Friday']

youtube = [2, 1, 6, 3]
twitter = [1, 1, 0, 2]
whatsapp = [3, 1, 2, 1]
raid_shadow_legends = [0, 4, 3, 3]
tiktok = [3, 0, 0, 2]


# plt.ylim(bottom=0, top=10)


plt.plot(days, youtube, label='YouTube', marker='o')
plt.plot(days, twitter, label='Twitter', marker='o')
plt.plot(days, whatsapp, label='Whatsapp', marker='o')
plt.plot(days, raid_shadow_legends, label='Raid: Shadow Legends', marker='o')
plt.plot(days, tiktok, label='TikTok', marker='o')


plt.title('Screen-time Usage Over the Week')
plt.xlabel('Day of the week')
plt.ylabel('Screen time')
plt.legend()

plt.show()