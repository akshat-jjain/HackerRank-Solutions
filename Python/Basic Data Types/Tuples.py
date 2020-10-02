if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

# Code credit :- Akshat Jain  # HackerRank Link :- https://www.hackerrank.com/akshat_jjain?hr_r=1
