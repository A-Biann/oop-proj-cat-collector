properties = [[1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], 
              [1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1], 
              [1, 0, 0, 1, 0, 1, 0, 0, 1, 0, 0, 0, 1],
              [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0],
              [1, 0, 1, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0], 
              [1, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0], 
              [1, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0], 
              [1, 0, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1], 
              [1, 0, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1], 
              [1, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0], 
              [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 0, 1], 
              [1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0], 
              [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1], 
              [0, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1], 
              [0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1], 
              [0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 1], 
              [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 0], 
              [0, 1, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1], 
              [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0], 
              [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1], 
              [0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0], 
              [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 1], 
              [0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 0, 1], 
              [0, 1, 0, 1, 1, 0, 0, 0, 1, 0, 0, 1, 1], 
              [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0], 
              [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 0], 
              [0, 1, 1, 0, 0, 0, 1, 0, 1, 0, 0, 1, 0], 
              [0, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0], 
              [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 0, 1], 
              [0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 0, 1, 1], 
              [0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 1, 1, 1], 
              [0, 1, 0, 1, 1, 0, 0, 1, 0, 0, 1, 0, 1], 
              [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1], 
              [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 0, 1, 1], 
              [0, 1, 1, 0, 1, 0, 0, 1, 0, 1, 0, 1, 1], 
              [0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0, 1], 
              [0, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 0]]

breeds = [['Abyssinian', '阿比西尼亞貓'], ['Bengal', '孟加拉貓'], 
        ['Birman', '伯曼貓'], ['Bombay', '孟買貓'], ['British Shorthair', '英國短毛貓'], 
        ['Egyptian Mau', '埃及貓'], ['Maine Coon', '緬因貓'], ['Persian cat', '波斯貓'], 
        ['Ragdoll', '布偶貓'], ['Russian Blue', '俄羅斯藍貓'], ['Siamese cat', '暹羅貓'], 
        ['Sphynx', '斯芬克斯貓'], ['American Bulldog', '美國鬥牛犬'], 
        ['American Pit Bull Terrier', '美國比特鬥牛犬'], ['Basset Hound', '巴吉度獵犬'], 
        ['Beagle', '小獵犬'], ['Boxer', '拳師狗'], ['Chihuahua', '吉娃娃'], ['English Cocker Spaniel', '英國可卡犬'], 
        ['English Setter', '英國塞特犬'], ['German Shorthaired', '德國短毛指示犬'], 
        ['Great Pyrenees', '庇里牛斯山犬'], ['Havanese', '哈瓦那犬'], ['Japanese Chin', '狆'], 
        ['Keeshond', '凱斯犬'], ['Leonberger', '蘭伯格犬'], ['Miniature Pinscher', '迷你杜賓犬'], 
        ['Newfoundland', '紐芬蘭犬'], ['Pomeranian', '博美犬'], ['Pug', '巴哥犬'], 
        ['Saint Bernard', '聖伯納犬'], ['Samoyed', '薩摩耶犬'], ['Scottish Terrier', '蘇格蘭㹴犬'], 
        ['Shiba Inu', '柴犬'], ['Staffordshire Bull Terrier', '斯塔福郡鬥牛㹴'], 
        ['Wheaten Terrier', '軟毛小麥梗'], ['Yorkshire Terrier', '約克夏㹴']]


# print
print(len(properties), len(properties[0]))