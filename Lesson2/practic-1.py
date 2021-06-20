class ChangeTime:

    def __init__(self, line):
        self.line = line

    def find_time(self):
        words = self.line.split()
        answer = []
        for i in range(len(words) - 1):

            if '12345678901112'.count(words[i]) >= 1 and ((words[i+1] == 'утра') or (words[i+1] == 'вечера') or
                                                          (words[i+1] == 'дня') or (words[i+1] == 'ночи')):
                if words[i+1] == 'утра' or words[i+1] == 'ночи':
                    new_time = str(int(words[i])) + ':00'
                elif words[i+1] == 'вечера' or words[i+1] == 'дня':
                    new_time = str(int(words[i]) + 12) + ':00'
                answer.append(new_time)

            if (words[i].count(':00') >= 1) and (words[i][len(words[i]) - 5] > '2') and (words[i][len(words[i]) - 4] > '4'):
                return '-'
        return answer


ct = ChangeTime('Жду тебя в 18:20')
print(*ct.find_time())
