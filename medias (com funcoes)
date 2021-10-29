def media_a(n1, n2):
    media = (n1 + n2) / 2
    round(media, 2)
    return media


def media_g(n1, n2):
    media = (n1 * n2) ** 0.5
    round(media, 2)
    return media


def media_h(n1, n2):
    if n1 == 0 or n2 == 0:
        media = 0.0
    else:
        media = 2 / (1 / n1 + 1 / n2)
        round(media, 2)
    return media


n1 = float(input())
n2 = float(input())
print(round(media_a(n1, n2), 2))
print(round(media_g(n1, n2), 2))
print(round(media_h(n1, n2), 2))
