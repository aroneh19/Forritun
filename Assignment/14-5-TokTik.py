def main():
    n = int(input())
    tok = {}

    for _ in range(n):
        tik, views = input().split()
        views = int(views)
        if tik in tok:
            tok[tik] += views
        else:
            tok[tik] = views

    most_popular = max(tok, key=tok.get)
    print(most_popular)

if __name__ == "__main__":
    main()
